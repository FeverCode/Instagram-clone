from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Profile, Image
from .forms import NewImageForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext


# Create your views here.


def register(request):
    if request.user.is_authenticated:
        raise Http404
    else:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(
                    request, f'Your account has been created. Log in now!')
                return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'registration/register.html', {'form': form})



class ImageList(ListView):
    model = Image
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        return context
    

@login_required
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
        return redirect ('login')
    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {'form': form})





