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
    project_text = RichTextField(config_name='default')
    order = models.IntegerField(default=1)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.project_title

    class Meta:
        ordering = ['order']

    def image_list(self):
        return Image.objects.filter(project=self, is_plan=False)

    def plan_list(self):
        return Image.objects.filter(project=self, is_plan=True)

    def main_image(self):
        return self.image_list()[0]

class Image(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images", default=None)
    is_plan = models.BooleanField(default=False)
    order = models.IntegerField(default=1)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['is_plan', 'order']

class Publication(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(default=0)
    publication_text = models.TextField(max_length=2000)

    def __str__(self):
        if self.year == 0:
            return self.title
        else:
            return self.title + ', ' + str(self.year)

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
