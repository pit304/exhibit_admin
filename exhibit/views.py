from django.views import generic
from django.utils import timezone

from .models import Project

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