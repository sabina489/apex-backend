from django.test import TestCase

from courses.models import Course, CourseCategory


class CourseTestCase(TestCase):
    """Models test for Courses."""

    def CourseNew(self, name="test", status="course", price="0.0"):
        courseCategory = CourseCategory.objects.create(name="category")
        return Course.objects.create(
            name=name, status=status, price=price, category=courseCategory
        )

    def test_Course_creation(self):
        courseNew = self.CourseNew()
        self.assertEqual(courseNew.__str__(), courseNew.name)


class CourseCategoryTestCase(TestCase):
    """Models tests for CourseCategory."""

    def CategoryNew(self, name="course"):
        return CourseCategory.objects.create(name=name)

    def test_Category_creation(self):
        category = self.CategoryNew()
        self.assertEqual(category.__str__(), category.name)
