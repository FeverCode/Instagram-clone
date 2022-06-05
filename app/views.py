from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Profile, Image

# Create your views here.
class ImageList(ListView):
    model = Image
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        return context
    
class ImageCreate(CreateView):
    model = Image
    fields = ['image', 'name', 'captions', 'profile', 'likes', 'comments']
    
    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)