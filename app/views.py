from email.mime import image
import profile
from xml.etree.ElementTree import Comment
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import *
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User




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


    
@login_required
def index(request):
    images = Image.objects.all().order_by('id').reverse()
    comments = Comment.objects.all()
    
    
    return render(request, 'index.html', {"images": images, "comments": comments}) 
    

@login_required
def SearchResults(request):
    

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        user_id = User.objects.get(username=search_term)
        searched_profile = Profile.search_by_profile(user_id.id)
        message = f"{search_term}"
        print(searched_profile)
        return render(request, 'search.html', {"message": message, "profile": searched_profile,})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message })


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            # prevents post get redirect pattern. sends a get request instead of post request
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,

    }
    return render(request, 'profile.html', context)


@login_required
def user_profile(request):
    profile = Profile.objects.all()
    images = Image.objects.all().order_by('id').reverse()
    return render(request, 'user-profile.html', {'profile': profile, 'images': images})


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Image
    fields = ['image', 'captions']
    template_name = 'new_image.html'
    success_url = '/'

    #   ↓        ↓ method of the CreatePostView
    def form_valid(self, form):
        form.instance.profile = self.request.user
        return super().form_valid(form)

    #   ↓              ↓ method of the CreatePostView
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['tag_line'] = 'Create new post'
        return data

def like(request,image_id,profile_id):
    image = Image.objects.get(id=image_id)
    profile = Profile.objects.get(id=profile_id)
    like = Like(image=image, profile=profile)
    like.save()
    return redirect ('list')