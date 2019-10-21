from .models import Project, Image, Plan, Atelier, Competition, Publication
from rest_framework import serializers

class AtelierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atelier
        fields = ['id', 'atelier_text']

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image_title', 'order', 'active']

class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'plan_title', 'order', 'active']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    plans = PlanSerializer(many=True,read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_title', 'project_text', 'order', 'active', 'images', 'plans']

class ProjectListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_title', 'project_text', 'order', 'active']

class PublicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'title', 'year', 'publication_text']
        
class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Competition
        fields = ['id', 'title', 'year', 'competition_text']
