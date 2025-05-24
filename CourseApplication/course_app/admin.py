from django.contrib import admin, messages
from django.db.models import Count


from course_app.models import Course, LecturerCourse, Lecturer


# Register your models here.

class LecturerCourseInline(admin.TabularInline):
    model = LecturerCourse
    extra = 0

class LecturerCourseAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):

        # Проверка: предавач не може да има повеќе од 3 курса
        if not change and obj.lecturer.courses.all().count() >= 3:
            messages.warning(request, "This lecturer can't have more than 3 courses")
            return  # НЕ зачувува, туку враќа

        if not change and obj.course.lecturercourse_set.count() + 1 >= 5:
            messages.warning(request, "This course has more than 5")
            return

        existing_courses = LecturerCourse.objects.select_related('course') \
            .filter(lecturer=obj.lecturer).exclude(course=obj.course)

        total_days = sum(
            (cl.course.end_date - cl.course.start_date).days
            for cl in existing_courses
            if cl.course.start_date and cl.course.end_date
        )

        new_course_duration = (
                    obj.course.end_date - obj.course.start_date).days if obj.course.start_date and obj.course.end_date else 0

        if total_days + new_course_duration > 365:
            messages.error(request,
                           f"Вкупната должина на курсевите за предавачот не смее да надмине 365 дена. Сега е: {total_days + new_course_duration}")
            return
        # Ако е OK, зачувај го објектот
        super().save_model(request, obj, form, change)


class CourseAdmin(admin.ModelAdmin):
    exclude = ('creator',)
    inlines = [LecturerCourseInline,]

    def has_add_permission(self, request):
        lecturer = Lecturer.objects.filter(user=request.user).first()
        if lecturer:
            return lecturer.academic_title == "P"
        return False

    def has_change_permission(self, request, obj=None):
        return obj and  obj.creator == request.user

    def has_delete_permission(self, request, obj=None):
        return obj and  obj.creator == request.user

    def get_queryset(self, request):
        return Course.objects.filter(creator=request.user)

    def has_view_permission(self, request, obj=None):
        return True

    def save_model(self, request, obj, form, change):
        obj.creator = request.user

        if not change and Course.objects.filter(name=obj.name).exists():
            messages.warning(request, "Course with this name already exists.")
            return

        # Прво го зачувуваме објектот, за да добие ID
        super().save_model(request, obj, form, change)




class LecturerAdmin(admin.ModelAdmin):

    exclude = ('user',)

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super(LecturerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.annotate(courses_count=Count('courses')).filter(courses_count__lt=2)
        return qs

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(LecturerAdmin, self).save_model(request, obj, form, change)


admin.site.register(Course, CourseAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(LecturerCourse, LecturerCourseAdmin)

