import random
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from course_app.models import Lecturer, Course


@receiver(pre_delete, sender=Lecturer)
def my_handler(sender, instance, **kwargs):
    courses = Course.objects.filter(creator=instance.user)

    other_lecturers = Lecturer.objects.exclude(id=instance.id).all()

    for course in courses:
        new_lecturer = random.choice(other_lecturers)
        course.creator = new_lecturer.user
        course.save()