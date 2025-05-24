from django.shortcuts import render, get_object_or_404, redirect

from course_app.forms import CourseForm
from course_app.models import Course, LecturerCourse, Lecturer


# Create your views here.

def index(request):
    courses = Course.objects.filter(creator=request.user).prefetch_related('lecturercourse_set__lecturer')
    context = {'course_list': courses, 'app_name': 'course_app'}
    return render(request, 'index.html', context)


def courseform(request, course_id=None):

    if course_id:
        course = get_object_or_404(Course, pk=course_id)

    else:
        course = None

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            course = form.save()
            course.creator = request.user
            course.save()

            lecturers_raw = form.cleaned_data['lecturers']
            lecturers_names = [name.strip() for name in lecturers_raw.split(',') if name.strip()]

            for name in lecturers_names:
                lecturer, created = Lecturer.objects.get_or_create(name=name)
                LecturerCourse.objects.create(course=course, lecturer=lecturer)
            form.save()

        return redirect('index')

    form = CourseForm(instance=course)
    return render(request, "courseform.html", context={'form': form, 'course_id': course_id})