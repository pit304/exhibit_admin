from datetime import datetime, timedelta

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Project

class ProjectModelTests(TestCase):

    def test_was_published_recently_with_future_project(self):
        """
        was_published_recently() returns False for projects whose pub_date
        is in the future.
        """
        time = timezone.now() + timedelta(days=30)
        future_project = Project(pub_date=time)
        self.assertIs(future_project.was_published_recently(), False)

    def test_was_published_recently_with_old_project(self):
        """
        was_published_recently() returns False for projects whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - timedelta(days=1, seconds=1)
        old_project = Project(pub_date=time)
        self.assertIs(old_project.was_published_recently(), False)

    def test_was_published_recently_with_recent_project(self):
        """
        was_published_recently() returns True for projects whose pub_date
        is within the last day.
        """
        time = timezone.now() - timedelta(hours=23, minutes=59, seconds=59)
        recent_project = Project(pub_date=time)
        self.assertIs(recent_project.was_published_recently(), True)

def create_project(project_title, days):
    """
    Create a project with the given `project_title` and published the
    given number of `days` offset to now (negative for projects published
    in the past, positive for projects that have yet to be published).
    """
    time = timezone.now() + timedelta(days=days)
    return Project.objects.create(project_title=project_title, pub_date=time)

class ProjectIndexViewTests(TestCase):
    def test_no_projects(self):
        """
        If no projects exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('exhibit:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No projects are available.")
        self.assertQuerysetEqual(response.context['latest_project_list'], [])

    def test_past_project(self):
        """
        Projects with a pub_date in the past are displayed on the
        index page.
        """
        create_project(project_title="Past project.", days=-30)
        response = self.client.get(reverse('exhibit:index'))
        self.assertQuerysetEqual(
            response.context['latest_project_list'],
            ['<Project: Past project.>']
        )

    def test_future_project(self):
        """
        Projects with a pub_date in the future aren't displayed on
        the index page.
        """
        create_project(project_title="Future project.", days=30)
        response = self.client.get(reverse('exhibit:index'))
        self.assertContains(response, "No projects are available.")
        self.assertQuerysetEqual(response.context['latest_project_list'], [])

    def test_future_project_and_past_project(self):
        """
        Even if both past and future projects exist, only past projects
        are displayed.
        """
        create_project(project_title="Past project.", days=-30)
        create_project(project_title="Future project.", days=30)
        response = self.client.get(reverse('exhibit:index'))
        self.assertQuerysetEqual(
            response.context['latest_project_list'],
            ['<Project: Past project.>']
        )

    def test_two_past_projects(self):
        """
        The projects index page may display multiple projects.
        """
        create_project(project_title="Past project 1.", days=-30)
        create_project(project_title="Past project 2.", days=-5)
        response = self.client.get(reverse('exhibit:index'))
        self.assertQuerysetEqual(
            response.context['latest_project_list'],
            ['<Project: Past project 2.>', '<Project: Past project 1.>']
        )

class ProjectDetailViewTests(TestCase):
    def test_future_project(self):
        """
        The detail view of a project with a pub_date in the future
        returns a 404 not found.
        """
        future_project = create_project(project_title='Future project.', days=5)
        url = reverse('exhibit:detail', args=(future_project.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_project(self):
        """
        The detail view of a project with a pub_date in the past
        displays the project's text.
        """
        past_project = create_project(project_title='Past project.', days=-5)
        url = reverse('exhibit:detail', args=(past_project.id,))
        response = self.client.get(url)
        self.assertContains(response, past_project.project_title)