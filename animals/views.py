from django.shortcuts import render
from animals.models import Animal


def index(request):
    if request.method == 'POST':
        sought_animal = request.POST['buscar']
        animals = Animal.objects.all().filter(name__icontains=sought_animal)
        context = {'animals': animals}
        return render(request, 'animals/index.html', context)
    else:
        return render(request, 'animals/index.html')
