from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.views.generic import DetailView, FormView,UpdateView
from django.contrib.auth import views as auth_views
from django.http import JsonResponse
# Forms
from users.form import  SignupForm

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile,Follow
# Create your views here.

class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        if request.user.is_authenticated:
            return redirect('posts:feed')
        return super().get(request, args, kwargs)

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logged_out.html'

class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:profile', kwargs={'username': username})

class UserDetailView(LoginRequiredMixin,DetailView):
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        context['followers'] = Follow.objects.filter(following=user.profile).count()
        context['following'] = Follow.objects.filter(follower=user).count()
        context['followed'] = Follow.objects.filter(following=user.profile,follower=self.request.user).exists()
        return context

def follow(request):
    user = User.objects.get(username=request.POST['user'])
    user1 = User.objects.get(username=request.POST['profile'])
    profile = user1.profile
    foll = Follow(following=profile,follower=user)
    foll.save()
    return JsonResponse({'message':'ok'})

def unfollow(request):
    user = User.objects.get(username=request.POST['user'])
    user1 = User.objects.get(username=request.POST['profile'])
    foll = Follow.objects.get(following = user1.profile , follower= user)
    if foll:
        foll.delete()
        return JsonResponse({'message':'ok'})
    return JsonResponse({'message':'error'})
    