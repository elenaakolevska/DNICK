from django import forms

from real_estate_app.models import RealEstate


class RealEstateForm(forms.ModelForm):
    characteristics = forms.CharField(
        label='Characteristics',
        widget = forms.TextInput(attrs={'class':'form-control'}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super (RealEstateForm, self).__init__(*args,**kwargs)
        for field_name, field in self.fields.items():
            if not isinstance(field.widget,forms.CheckboxInput):
                field.widget.attrs['class']='form-control'

    class Meta:
        model=RealEstate
        fields="__all__"
        widgets={
            'date':forms.DateInput(attrs={'class':'form-control','type':'date'})
        }