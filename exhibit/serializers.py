from .models import Project, Atelier, Competition
from rest_framework import serializers


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_title', 'project_text', 'pub_date', 'active']


class AtelierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atelier
        fields = ['id', 'atelier_text']

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competition
        fields = ['id', 'title', 'year', 'competition_text']