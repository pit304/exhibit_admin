from django.views import generic
from django.utils import timezone
from rest_framework import viewsets

from .models import Project, Atelier, Competition
from .serializers import ProjectSerializer, AtelierSerializer, CompetitionSerializer

class IndexView(generic.ListView):
    template_name = 'exhibit/index.html'
    context_object_name = 'latest_project_list'

    def get_queryset(self):
        """
        Return the last five published projects (not including those set to be
        published in the future).
        """
        return Project.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Project
    template_name = 'exhibit/detail.html'
        
    def get_queryset(self):
        """
        Excludes any projects that aren't published yet.
        """
        return Project.objects.filter(pub_date__lte=timezone.now())

# REST API views
class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = Project.objects.all().order_by('-pub_date')
    serializer_class = ProjectSerializer


class AtelierViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows atelier to be viewed or edited.
    """
    queryset = Atelier.objects.all()
    serializer_class = AtelierSerializer

class CompetitionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows atelier to be viewed or edited.
    """
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer