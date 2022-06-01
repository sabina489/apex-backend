from django.test import TestCase
from django.urls import reverse

# from courses.models import Course, CourseCategory


class CourseListAPIView(TestCase):
    """Views test for listing courses"""

    # def create_Course(self, name="course"):
    #     courseCategory = CourseCategory.objects.create(name="course")
    #     course = Course.objects.create(name="course1", category=courseCategory)

    def test_Course(self):
        url = reverse("course-list")
        response = self.client.get(url)
        self.assertEqual(len(response.data), 0)


class CourseCreateAPIView(TestCase):
    """View tests for creating courses."""

    def test_Course(self):
        url = reverse("course-create")
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)


class CourseRetrieveAPIView(TestCase):
    """View tests for retrieving courses."""

    def test_Retrieve(self):
        url = reverse("course-retrieve", args=[1])
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)


class CourseUpdateAPIView(TestCase):
    """View tests for updating courses."""

    def test_Update(self):
        url = reverse("course-update", args=[100])
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)


class CourseDeleteAPIVIew(TestCase):
    def test_Delete(self):
        """View tests for deleting courses."""
        url = reverse("course-delete", args=[500])
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)


class CourseCategoryListAPIView(TestCase):
    """View tests listing course category."""

    def test_List(self):
        url = reverse("category-list")
        response = self.client.get(url)
        self.assertEqual(len(response.data), 0)


class CourseCategoryCreateAPIView(TestCase):
    """View tests for creating coursecategory."""

    def test_create(self):
        url = reverse("category-create")
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)


class CourseCategoryRetrieveAPIView(TestCase):
    """View tests for retrieving coursecategory."""

    def test_retrieve(self):
        url = reverse("category-retrieve", args=[5])
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)


class CourseCategoryUpdateAPIView(TestCase):
    """View tests for updating coursecategory."""

    def test_update(self):
        url = reverse("category-update", args=[400])
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)


class CourseDeleteAPIView(TestCase):
    """View tests for deleting coursecategory."""

    def test_delete(self):
        url = reverse("category-delete", args=[7])
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
