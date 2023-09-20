from django.shortcuts import render

bears = [
    {'species': 'Black Bear', 'Latin Name': 'Ursus americanus', 'color': 'black'},
    {'species': 'Polar Bear', 'Latin Name': 'Ursus arctos', 'color': 'white'},
    {'species': 'Brown Bear', 'Latin Name': 'Ursus maritimus', 'color': 'brown'},
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