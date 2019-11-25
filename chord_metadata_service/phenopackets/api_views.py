from rest_framework import viewsets, pagination
from .serializers import *
from .models import *
from rest_framework.settings import api_settings
from chord_metadata_service.restapi.api_renderers import (
	PhenopacketsRenderer, BiosampleFHIRRenderer,
	PhenotypicFeatureFHIRRenderer, ProcedureFHIRRenderer)


class LargeResultsSetPagination(pagination.PageNumberPagination):
	page_size = 25
	page_size_query_param = 'page_size'
	max_page_size = 10000


class PhenotypicFeatureViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing phenotypic features

	post:
	Create a new phenotypic feature

	"""
	queryset = PhenotypicFeature.objects.all()
	serializer_class = PhenotypicFeatureSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer, PhenotypicFeatureFHIRRenderer, )


class ProcedureViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing procedures

	post:
	Create a new procedure

	"""
	queryset = Procedure.objects.all()
	serializer_class = ProcedureSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer, ProcedureFHIRRenderer)


class HtsFileViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing HTS files

	post:
	Create a new HTS file

	"""
	queryset = HtsFile.objects.all()
	serializer_class = HtsFileSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer,)


class GeneViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing genes

	post:
	Create a new gene

	"""
	queryset = Gene.objects.all()
	serializer_class = GeneSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer,)


class VariantViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing variants

	post:
	Create a new variant

	"""
	queryset = Variant.objects.all()
	serializer_class = VariantSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer,)
	# TODO filtering
	# filter_backends = (DjangoFilterBackend,)
	# filter_class = VariantFilter


class DiseaseViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing diseases

	post:
	Create a new disease

	"""
	queryset = Disease.objects.all()
	serializer_class = DiseaseSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer,)


class ResourceViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing resources

	post:
	Create a new resource

	"""
	queryset = Resource.objects.all()
	serializer_class = ResourceSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer,)


class MetaDataViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing metadata records

	post:
	Create a new metadata record

	"""
	queryset = MetaData.objects.all()
	serializer_class = MetaDataSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer,)


class BiosampleViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing biosamples

	post:
	Create a new biosample
	"""
	queryset = Biosample.objects.all()
	serializer_class = BiosampleSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer, BiosampleFHIRRenderer, )


class PhenopacketViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing phenopackets

	post:
	Create a new phenopacket

	"""
	queryset = Phenopacket.objects.all()
	serializer_class = PhenopacketSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer,)


class GenomicInterpretationViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing genomic interpretations

	post:
	Create a new genomic interpretation

	"""
	queryset = GenomicInterpretation.objects.all()
	serializer_class = GenomicInterpretationSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer,)


class DiagnosisViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing diagnoses

	post:
	Create a new diagnosis

	"""
	queryset = Diagnosis.objects.all()
	serializer_class = DiagnosisSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer,)


class InterpretationViewSet(viewsets.ModelViewSet):
	"""
	get:
	Return a list of all existing interpretations

	post:
	Create a new interpretation

	"""
	queryset = Interpretation.objects.all()
	serializer_class = InterpretationSerializer
	pagination_class = LargeResultsSetPagination
	renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES
		) + (PhenopacketsRenderer,)
