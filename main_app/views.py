from django.shortcuts import render

bears = [
    {'species': 'Black Bear', 'latin_name': 'Ursus americanus', 'weight': '200-600 pounds','size': '5-6 feet', 'color': 'black', 'baby_picture': 'https://d.newsweek.com/en/full/2009842/black-bear.webp?w=900&f=b124736e21eb43fd3a79d3dee215633a'},
    {'species': 'Polar Bear', 'latin_name': 'Ursus arctos', 'weight': '900-1600 pounds','size': '7.25-8 feet', 'color': 'white', 'baby_picture': 'https://www.usatoday.com/gcdn/media/USATODAY/USATODAY/2013/03/29/ap-orphaned-polar-bear-cub-16_9.jpg?width=1320&height=746&fit=crop&format=pjpg&auto=webp'},
    {'species': 'Brown Bear', 'latin_name': 'Ursus maritimus', 'weight': '700 pounds','size': '5-8 feet', 'color': 'brown', 'baby_picture': 'https://nhpbs.org/wild/images/brownbearusfwstevehilldebrand1.jpg'},
]

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
    return render(request, 'bears/bears_index.html', {
        'bears': bears
    })