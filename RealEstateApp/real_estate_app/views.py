from tkinter.font import names

from django.shortcuts import render, get_object_or_404, redirect

from real_estate_app.forms import RealEstateForm
from real_estate_app.models import RealEstate, CharacteristicsRealEstate, Characteristics


# Create your views here.

def index(request):
    real_estates = RealEstate.objects.filter(area__gte=100000, is_sold=False)
    real_estate_context = []
    for estate in real_estates:
        sum = 0
        estate_chars = CharacteristicsRealEstate.objects.filter(real_estate=estate)

        for estate_char in estate_chars:
            sum += estate_char.characteristics.price
        real_estate_context.append({'real_estate': estate, "price": sum})

    return render(request, 'index.html', {'real_estates': real_estate_context})

def edit_estate(request, estate_id):
    estate = get_object_or_404(RealEstate, pk=estate_id)

    if request.method=='POST':
        form = RealEstateForm(request.POST,request.FILES,instance=estate)
        if form.is_valid():
            estate=form.save()
            estate.save()

            chars_raw = form.cleaned_data['characteristics']
            chars_names = [name.strip() for name in chars_raw.split(',') if name.strip()]

            for name in chars_names:
                char_obj, created = Characteristics.objects.get_or_create(name=name)
                CharacteristicsRealEstate.objects.create(real_estate=estate, characteristics=char_obj)

            form.save()
        return  redirect('index')

    else:
        existing_chars = CharacteristicsRealEstate.objects.filter(real_estate=estate).values_list(
            'characteristics__name', flat=True)
        chars_string = ', '.join(existing_chars)
        form = RealEstateForm(instance=estate, initial={'characteristics': chars_string})

    return render(request, "edit_estate.html", context={'form': form, 'estate_id': estate_id})