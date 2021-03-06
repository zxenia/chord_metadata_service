import json
import jsonschema
import jsonschema.exceptions
import os
import uuid

from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.renderers import BaseRenderer
from rest_framework.response import Response

from chord_lib.schemas.chord import CHORD_INGEST_SCHEMA
from chord_lib.responses import errors
from chord_lib.workflows import get_workflow, get_workflow_resource, workflow_exists

from .ingest import METADATA_WORKFLOWS, WORKFLOWS_PATH, WORKFLOW_INGEST_FUNCTION_MAP
from .models import Table


class WDLRenderer(BaseRenderer):
    media_type = "text/plain"
    format = "text"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data.encode(self.charset)


@api_view(["GET"])
@permission_classes([AllowAny])
def workflow_list(_request):
    return Response(METADATA_WORKFLOWS)


@api_view(["GET"])
@permission_classes([AllowAny])
def workflow_item(_request, workflow_id):
    if not workflow_exists(workflow_id, METADATA_WORKFLOWS):
        return Response(errors.not_found_error(f"No workflow with ID {workflow_id}"), status=404)

    return Response(get_workflow(workflow_id, METADATA_WORKFLOWS))


@api_view(["GET"])
@permission_classes([AllowAny])
@renderer_classes([WDLRenderer])
def workflow_file(_request, workflow_id):
    if not workflow_exists(workflow_id, METADATA_WORKFLOWS):
        return Response(status=404, data="Not found")

    wdl_path = os.path.join(WORKFLOWS_PATH, get_workflow_resource(workflow_id, METADATA_WORKFLOWS))
    with open(wdl_path, "r") as wf:
        return Response(wf.read())


# Mounted on /private/, so will get protected anyway; this allows for access from WES
# TODO: Ugly and misleading permissions
@api_view(["POST"])
@permission_classes([AllowAny])
def ingest(request):
    # Private ingest endpoints are protected by URL namespace, not by Django permissions.

    # TODO: Schema for OpenAPI doc
    # TODO: Use serializers with basic objects and maybe some more complex ones too (but for performance, this might
    #  not be optimal...)

    try:
        jsonschema.validate(request.data, CHORD_INGEST_SCHEMA)
    except jsonschema.exceptions.ValidationError:
        return Response(errors.bad_request_error("Invalid ingest request body"), status=400)  # TODO: Validation errors

    table_id = request.data["table_id"]

    if not Table.objects.filter(ownership_record_id=table_id).exists():
        return Response(errors.bad_request_error(f"Table with ID {table_id} does not exist"), status=400)

    table_id = str(uuid.UUID(table_id))  # Normalize dataset ID to UUID's str format.

    workflow_id = request.data["workflow_id"].strip()
    workflow_outputs = request.data["workflow_outputs"]

    if not workflow_exists(workflow_id, METADATA_WORKFLOWS):  # Check that the workflow exists
        return Response(errors.bad_request_error(f"Workflow with ID {workflow_id} does not exist"), status=400)

    try:
        with transaction.atomic():
            # Wrap ingestion in a transaction, so if it fails we don't end up in a partial state in the database.
            WORKFLOW_INGEST_FUNCTION_MAP[workflow_id](workflow_outputs, table_id)

    except KeyError:
        # Tried to access a non-existant workflow output
        # TODO: More precise error (which key?)
        return Response(errors.bad_request_error("Missing workflow output"), status=400)

    except json.decoder.JSONDecodeError as e:
        return Response(errors.bad_request_error(f"Invalid JSON provided for ingest document (message: {e})"),
                        status=400)

    except ValidationError as e:
        return Response(errors.bad_request_error(
            "Encountered validation errors during ingestion",
            *(e.error_list if hasattr(e, "error_list") else e.error_dict.items()),
        ))

    # TODO: Schema validation
    # TODO: Rollback in case of failures
    return Response(status=204)
