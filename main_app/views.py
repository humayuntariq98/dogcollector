from django.shortcuts import render

dogs = [
  {'name': 'Cleo', 'breed': 'German Shephard', 'description': 'great for protection', 'age': 3},
  {'name': 'Clover', 'breed': 'Husky', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    return render(request, 'dogs/index.html', {
      'dogs': dogs  
    })