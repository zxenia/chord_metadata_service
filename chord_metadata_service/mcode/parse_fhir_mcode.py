import uuid
import json

from .mappings.mappings import *
from .mappings.mcode_profiles import *
from chord_metadata_service.restapi.schemas import FHIR_BUNDLE_SCHEMA
from chord_metadata_service.restapi.fhir_ingest import _check_schema
from chord_metadata_service.restapi.fhir_utils import patient_to_individual


def get_ontology_value(resource, codeable_concept_property):
    """
    The function covers the most encountered use cases.
     """
    try:
        ontology_value = {}
        if "system" in resource[codeable_concept_property]['coding'][0]:
            ontology_value["id"] = f"{resource[codeable_concept_property]['coding'][0]['system']}:" \
                                   f"{resource[codeable_concept_property]['coding'][0]['code']}"
        else:
            ontology_value["id"] = f"{resource[codeable_concept_property]['coding'][0]['code']}"

        if "display" in resource[codeable_concept_property]['coding'][0]:
            ontology_value["label"] = f"{resource[codeable_concept_property]['coding'][0]['display']}"
        else:
            ontology_value["label"] = f"{resource[codeable_concept_property]['coding'][0]['code']}"
        return ontology_value
    # will be raised if there is no "code" in Coding element
    except KeyError as e:
        raise KeyError(e)


def observation_to_labs_vital(resource):
    """ Observation with tumor marker to LabsVital. """
    labs_vital = {
        "id": resource["id"]
    }
    if "code" in resource:
        labs_vital["tumor_marker_code"] = get_ontology_value(resource, "code")
    if "valueCodeableConcept" in resource:
        labs_vital["tumor_marker_data_value"] = get_ontology_value(resource, "valueCodeableConcept")
    if "subject":
        labs_vital["individual"] = resource["subject"]["reference"].split("uuid:")[-1]
    return labs_vital


def observation_to_tnm_staging(resource):
    """ Observation with tnm staging to TNMStaging. """
    tnm_staging = {
        "id": resource["id"],
        "tnm_staging_value": {}
    }
    if "valueCodeableConcept" in resource:
        tnm_staging["tnm_staging_value"]["data_value"] = get_ontology_value(resource, "valueCodeableConcept")
    if "method" in resource:
        tnm_staging["tnm_staging_value"]["staging_system"] = get_ontology_value(resource, "method")
    # reference to Condition
    if "focus" in resource:
        tnm_staging["cancer_condition"] = resource["focus"][0]["reference"].split("/")[-1]
    return tnm_staging


def procedure_to_crprocedure(resource):
    """ Procedure to Cancer related Procedure. """

    cancer_related_procedure = {
        "id": resource["id"]
    }
    if "code" in resource:
        cancer_related_procedure["code"] = get_ontology_value(resource, "code")
    if "bodySite" in resource:
        cancer_related_procedure["body_site"] = get_ontology_value(resource, "bodySite")
    if "reasonCode" in resource:
        codes = []
        for code in resource["reasonCode"]["coding"]:
            reason_code = {
                "id": f"{code['system']}:{code['code']}",
                "label": f"{code['display']}"
            }
            codes.append(reason_code)
        cancer_related_procedure["reason_code"] = codes
    if "reasonReference" in resource:
        cancer_conditions = [cc["reference"].split("uuid:")[-1] for cc in resource["reasonReference"]]
        cancer_related_procedure["reason_reference"] = cancer_conditions
    # TODO add laterality
    return cancer_related_procedure


def get_medication_statement(resource):
    """ Medication Statement to Medication Statement. """
    medication_statement = {
        "id": resource["id"]
    }
    if "medicationCodeableConcept" in resource:
        medication_statement["medication_code"] = get_ontology_value(resource, "medicationCodeableConcept")
    # TODO the rest
    return medication_statement


def _get_tnm_staging_property(resource: dict, profile_urls: list, category_type=None):
    """" Retrieve Observation based on its profile. """
    for profile in profile_urls:
        if profile in resource["meta"]["profile"]:
            property_value = observation_to_tnm_staging(resource)
            if category_type:
                property_value["category_type"] = category_type
            return property_value


def _get_profiles(resource: dict, profile_urls: list):
    try:
        resource_profiles = resource["meta"]["profile"]
        for p in profile_urls:
            if p in resource_profiles:
                return True
    except KeyError as e:
        raise KeyError(e)


def condition_to_cancer_condition(resource):
    """ FHIR Condition to Mcode Cancer Condition. """

    cancer_condition = {
        "id": resource["id"]
    }
    # condition = cond.Condition(resource)
    if "clinicalStatus" in resource:
        cancer_condition["clinical_status"] = get_ontology_value(resource, "clinicalStatus")
    if "verificationStatus" in resource:
        cancer_condition["verification_status"] = get_ontology_value(resource, "verificationStatus")
    if "code" in resource:
        cancer_condition["code"] = get_ontology_value(resource, "code")
    if "recordedDate" in resource:
        cancer_condition["date_of_diagnosis"] = resource["recordedDate"]
    if "bodySite" in resource:
        cancer_condition["body_site"] = []
        for item in resource["bodySite"]['coding']:
            coding = {
                "id": f"{item['system']}:{item['code']}",
                "label": f"{item['display']}",
            }
            cancer_condition["body_site"].append(coding)
    if "laterality" in resource:
        cancer_condition["laterality"] = get_ontology_value(resource, "laterality")
    if "histologyMorphologyBehavior" in resource:
        cancer_condition["histology_morphology_behavior"] = get_ontology_value(resource, "histologyMorphologyBehavior")
    return cancer_condition


def parse_bundle(bundle):
    """
    Parse fhir Bundle and extract all relevant profiles.
    :param bundle: FHIR resourceType Bundle object
    :return: mcodepacket object
    """
    _check_schema(FHIR_BUNDLE_SCHEMA, bundle, 'bundle')
    mcodepacket = {
        "id": str(uuid.uuid4())
    }
    tumor_markers = []
    # all tnm_stagings
    tnm_stagings = []
    # dict that maps tnm_staging value to its member
    staging_to_members = {}
    # all tnm staging members
    tnm_staging_members = []
    # all procedure
    cancer_related_procedures = []
    cancer_conditions = []
    for item in bundle["entry"]:
        resource = item["resource"]
        # get Patient data
        if resource["resourceType"] == "Patient":
            # patient = patient_to_individual(resource)
            mcodepacket["subject"] = {
                "id": resource["id"]
            }
        # get Patient's Cancer Condition
        if resource["resourceType"] == "Condition":
            resource_profiles = resource["meta"]["profile"]
            cancer_conditions_profiles = [MCODE_PRIMARY_CANCER_CONDITION, MCODE_SECONDARY_CANCER_CONDITION]
            for cc in cancer_conditions_profiles:
                if cc in resource_profiles:
                    cancer_condition = condition_to_cancer_condition(resource)
                    for key, value in MCODE_PROFILES_MAPPING["cancer_condition"]["profile"].items():
                        if cc == value:
                            cancer_condition["condition_type"] = key
                            cancer_conditions.append(cancer_condition)
                            # mcodepacket["cancer_condition"] = cancer_condition

        # get TNM staging stage category
        if resource["resourceType"] == "Observation" and "meta" in resource:
            resource_profiles = resource["meta"]["profile"]
            stage_groups = [MCODE_TNM_CLINICAL_STAGE_GROUP, MCODE_TNM_PATHOLOGIC_STAGE_GROUP]
            for sg in stage_groups:
                if sg in resource_profiles:
                    tnm_staging = {"id": resource["id"]}
                    tnm_stage_group = observation_to_tnm_staging(resource)
                    tnm_staging["cancer_condition"] = tnm_stage_group["cancer_condition"]
                    tnm_staging["stage_group"] = tnm_stage_group["tnm_staging_value"]
                    for key, value in MCODE_PROFILES_MAPPING["tnm_staging"]["properties_profile"]["stage_group"].items():
                        if sg == value:
                            tnm_staging["tnm_type"] = key
                    if "hasMember" in resource:
                        members = []
                        for member in resource["hasMember"]:
                            member_observation_id = member["reference"].split('/')[-1]
                            members.append(member_observation_id)
                        # collect all members of this staging in a dict
                        staging_to_members[resource["id"]] = members
                    tnm_stagings.append(tnm_staging)

        # get all TNM staging members
        if resource["resourceType"] == "Observation" and "meta" in resource:
            primary_tumor_category = _get_tnm_staging_property(resource,
                                                               [MCODE_TNM_CLINICAL_PRIMARY_TUMOR_CATEGORY,
                                                                MCODE_TNM_PATHOLOGIC_PRIMARY_TUMOR_CATEGORY],
                                                               'primary_tumor_category')
            regional_nodes_category = _get_tnm_staging_property(resource,
                                                                [MCODE_TNM_CLINICAL_REGIONAL_NODES_CATEGORY,
                                                                 MCODE_TNM_PATHOLOGIC_REGIONAL_NODES_CATEGORY],
                                                                'regional_nodes_category')
            distant_metastases_category = _get_tnm_staging_property(resource,
                                                                    [MCODE_TNM_CLINICAL_REGIONAL_NODES_CATEGORY,
                                                                     MCODE_TNM_PATHOLOGIC_REGIONAL_NODES_CATEGORY],
                                                                    'distant_metastases_category')

            for category in [primary_tumor_category, regional_nodes_category, distant_metastases_category]:
                if category:
                    tnm_staging_members.append(category)

        # get Cancer Related Procedure
        if resource["resourceType"] == "Procedure" and "meta" in resource:
            resource_profiles = resource["meta"]["profile"]
            procedure_profiles = [MCODE_CANCER_RELATED_RADIATION_PROCEDURE, MCODE_CANCER_RELATED_SURGICAL_PROCEDURE]
            for pp in procedure_profiles:
                if pp in resource_profiles:
                    procedure = procedure_to_crprocedure(resource)
                    for key, value in MCODE_PROFILES_MAPPING["cancer_related_procedure"]["profile"].items():
                        if pp == value:
                            procedure["procedure_type"] = key
                    cancer_related_procedures.append(procedure)

        # get tumor marker
        if resource["resourceType"] == "Observation" and "meta" in resource:
            if MCODE_TUMOR_MARKER in resource["meta"]["profile"]:
                labs_vital = observation_to_labs_vital(resource)
                tumor_markers.append(labs_vital)

        # get Medication Statement
        if resource["resourceType"] == "MedicationStatement" and "meta" in resource:
            if MCODE_MEDICATION_STATEMENT in resource["meta"]["profile"]:
                mcodepacket["medication_statement"] = get_medication_statement(resource)

        # get Cancer Disease Status
        if resource["resourceType"] == "Observation" and "meta" in resource:
            if MCODE_CANCER_DISEASE_STATUS in resource["meta"]["profile"]:
                # TODO change refactor observation conversion
                mcodepacket["cancer_disease_status"] = observation_to_labs_vital(resource)["tumor_marker_data_value"]

    # annotate tnm staging with its members
    for tnm_staging_item in tnm_stagings:
        for member in tnm_staging_members:
            if member["id"] in staging_to_members[tnm_staging_item["id"]]:
                tnm_staging_item[member["category_type"]] = member["tnm_staging_value"]

    if cancer_conditions:
        mcodepacket["cancer_condition"] = cancer_conditions
    # mcodepacket["tnm_staging"] = tnm_stagings
    mcodepacket["tumor_marker"] = tumor_markers
    mcodepacket["cancer_related_procedures"] = cancer_related_procedures

    # TODO add nested tnm_stagings to cancer_condition
    for tnms in tnm_stagings:
        if tnms["cancer_condition"] == mcodepacket["cancer_condition"]["id"]:
            mcodepacket["cancer_condition"]["tnm_staging"] = tnm_stagings

    return mcodepacket

