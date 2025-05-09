from django import forms
from event_app.models import Event




class EventForm(forms.ModelForm):

    def __init__(self, *args ,**kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):
                # if isinstance(field.widget, forms.DateTimeInput):
                #     field.widget.input_type = 'date'
                field.widget.attrs['class'] = 'form-control'
    class Meta:
        exclude = ('user',)
        model = Event
        widgets = {
        'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})}