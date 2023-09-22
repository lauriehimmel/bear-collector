from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Bear, Food
from .forms import FeedingForm

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
    id_list = bear.food.all().values_list('id')
    food_bear_doesnt_have = Food.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'bears/bears_detail.html', {
        'bear': bear, 'feeding_form': feeding_form,
        'food': food_bear_doesnt_have
    })

class BearCreate(CreateView):
    model = Bear
    fields = ['species', 'latin_name', 'weight_bottom', 'weight_top', 'size','color']

class BearUpdate(UpdateView):
    model = Bear
    fields = '__all__'

class BearDelete(DeleteView):
    model = Bear
    success_url = '/bears'

def add_feeding(request, bear_id):
  # create a ModelForm instance using 
  # the data that was submitted in the form
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # We want a model instance, but
    # we can't save to the db yet
    # because we have not assigned the
    # cat_id FK.
    new_feeding = form.save(commit=False)
    new_feeding.bear_id = bear_id
    new_feeding.save()
  return redirect('bears_detail', bear_id=bear_id)

class FoodList(ListView):
  model = Food

class FoodDetail(DetailView):
  model = Food

class FoodCreate(CreateView):
  model = Food
  fields = '__all__'

class FoodUpdate(UpdateView):
  model = Food
  fields = ['name', 'info']

class FoodDelete(DeleteView):
  model = Food
  success_url = '/food'


def assoc_food(request, bear_id, food_id):
  Bear.objects.get(id=bear_id).food.add(food_id)
  return redirect('bears_detail', bear_id=bear_id)