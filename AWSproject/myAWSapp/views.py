from django.shortcuts import render, get_object_or_404
from .models import Cars
from .carform import CarForm
from django.shortcuts import redirect

def index(request):
    cars = Cars.objects.all()
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'homepage.html', {'cars': cars, 'form': form})

def edit_car(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CarForm(instance=car)
    return render(request, 'car_edit.html', {'form': form})

def delete_car(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    if request.method == "POST":
        car.delete()
        return redirect('index')
    return render(request, 'car_delete.html', {'car': car})

def car_detail(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    return render(request, 'car_details.html', {'car': car})
