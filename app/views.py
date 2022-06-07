from email.mime import image
import profile
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import Profile, Image
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin



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


class ImageList(LoginRequiredMixin, ListView):
    model = Image
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.all()
        return context
    

# @login_required
# def new_image(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewImageForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user = current_user
#             profile.save()
#         return redirect ('list')
#     else:
#         form = NewImageForm()
#     return render(request, 'new_image.html', {'form': form})

@login_required
def SearchResults(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Image.search_by_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "profiles": searched_profile})

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
    return render(request, 'user-profile.html', {'profile': profile})


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
