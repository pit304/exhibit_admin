from django.views import generic
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Project, Atelier, Competition, Publication
from .serializers import ProjectSerializer, ProjectListSerializer, AtelierSerializer, CompetitionSerializer, PublicationSerializer

class IndexView(generic.ListView):
    template_name = 'exhibit/index.html'
    context_object_name = 'project_list'

    def get_queryset(self):
        """
        Return the last five published projects (not including those set to be
        published in the future).
        """
        return Project.objects.filter(active=True).order_by('order')


class DetailView(generic.DetailView):
    model = Project
    template_name = 'exhibit/detail.html'
        
    def get_queryset(self):
        """
        Excludes any projects that aren't published yet.
        """
        return Project.objects.filter(active=True)

# REST API views
class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('order')
    serializer_class = ProjectSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        active = str(self.request.query_params.get('active')).lower()
        if active in ['true', '1', 'yes']:
            queryset = queryset.filter(active=True)
        elif active in ['false', '0', 'no']:
            queryset = queryset.filter(active=False)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProjectListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class AtelierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows atelier to be viewed or edited.
    """
    queryset = Atelier.objects.all()
    serializer_class = AtelierSerializer

class CompetitionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows competitions to be viewed or edited.
    """
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

class PublicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows publications to be viewed or edited.
    """
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer