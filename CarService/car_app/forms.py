from django import forms

from car_app.models import Service


class ServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Service
        exclude = ["user"]