from django.shortcuts import render
from .models import Bear

home_images = [
    {'image': 'https://www.boredpanda.com/blog/wp-content/uploads/2016/09/mother-bear-cubs-animal-parenting-21-57e3a2161d7f7__880.jpg'},
    {'image': 'https://images.squarespace-cdn.com/content/v1/5848371cbebafb36c2914af1/1665073119879-303UF17HAFS17Z2WFNOQ/unsplash-image-y421kXlUOQk.jpg?format=2500w'},
    {'image': 'https://www.boredpanda.com/blog/wp-content/uploads/2016/09/mother-bear-cubs-animal-parenting-45-57e3c999e1c30__880.jpg'},
    {'image': 'https://metro.co.uk/wp-content/uploads/2016/02/552982725.jpg?quality=90&strip=all&zoom=1&resize=644%2C427'},

]
# Create your views here.
def home(request):
    return render(request, 'home.html',{
        'photos': home_images
        })

def about(request):
    return render(request, 'about.html')

def bears_index(request):
    bears = Bear.objects.all()
    return render(request, 'bears/bears_index.html', {
        'bears': bears
    })

def bears_detail(request, bear_id):
    bear = Bear.objects.get(id=bear_id)
    return render(request, 'bears/bears_detail.html', {
        'bear': bear
    })