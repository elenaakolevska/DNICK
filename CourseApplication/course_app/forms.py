from django import forms

from course_app.models import Course


class CourseForm(forms.ModelForm):
    lecturers = forms.CharField(
        label='Lecturers (comma-separated)',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Course
        exclude = ['creator']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
