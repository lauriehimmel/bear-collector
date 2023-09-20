from django.shortcuts import render

bears = [
    {'species': 'Black Bear', 'latin_name': 'Ursus americanus', 'color': 'black'},
    {'species': 'Polar Bear', 'latin_name': 'Ursus arctos', 'color': 'white'},
    {'species': 'Brown Bear', 'latin_name': 'Ursus maritimus', 'color': 'brown'},
]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def bears_index(request):
    return render(request, 'bears/bears_index.html', {
        'bears': bears
    })