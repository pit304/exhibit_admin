from django.db import models
from django.utils import timezone
from datetime import datetime    

class Atelier(models.Model):
    atelier_text = models.CharField(max_length=2000)

    def __str__(self):
        return self.atelier_text

class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.project_title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Publication(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    publication_title = models.CharField(max_length=200)
    publication_text = models.CharField(max_length=2000)
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.publication_text

class Competition(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    competition_text = models.CharField(max_length=2000)
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.competition_text