from rest_framework.test import APITestCase

from .models import Student, Subject


class StudentListViewTests(APITestCase):
    def test_root_lists_students_with_their_subjects(self):
        student = Student(
            email="student@example.com",
            first_name="Sample",
            last_name="Student",
            roll_number="GV04-TEST",
        )
        student.set_unusable_password()
        student.save()
        Subject.objects.create(
            student=student,
            name="Mathematics",
            code="GV04TEST",
            description="A sample subject.",
        )

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["email"], "student@example.com")
        self.assertEqual(response.data[0]["subjects"][0]["name"], "Mathematics")
