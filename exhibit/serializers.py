from .models import Project, Atelier, Competition, Publication
from rest_framework import serializers


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_title', 'project_text', 'order', 'active']


class AtelierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atelier
        fields = ['id', 'atelier_text']

class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competition
        fields = ['id', 'title', 'year', 'competition_text']

class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'title', 'year', 'publication_text']