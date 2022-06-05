from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Profile, Image
from .forms import NewImageForm

# Create your views here.
class ImageList(ListView):
    model = Image
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        return context
    
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
        return redirect ('/')
    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {'form': form})