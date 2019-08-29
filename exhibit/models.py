from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta   
from ckeditor.fields import RichTextField

class Atelier(models.Model):
    atelier_text = RichTextField(config_name='default')

    def abstract(self):
        return 'Atelier text ' + str(self.id)

    def __str__(self):
        return 'Atelier text ' + str(self.id)

    class Meta:
        ordering = ['-id']

class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_text = models.TextField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.project_title

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    
    class Meta:
        ordering = ['-id']

class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=200)
    image = models.ImageField(default=None)
    active = models.BooleanField(default=True)

class Plan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    plan_title = models.CharField(max_length=200)
    image = models.ImageField(default=None)
    active = models.BooleanField(default=True)

class Publication(models.Model):
    publication_title = models.CharField(max_length=200)
    publication_text = models.TextField(max_length=2000)
    year = models.IntegerField(default=0)

    def __str__(self):
        return self.publication_text

    class Meta:
        ordering = ['-id']

class Competition(models.Model):
    title = models.CharField(max_length=200, default='No title')
    year = models.IntegerField(default=0)
    competition_text = models.TextField(max_length=2000)

    def __str__(self):
        if self.year == 0:
            return self.title
        else:
            return self.title + ', ' + str(self.year)
    
    class Meta:
        ordering = ['-id']
