from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView, CreateView
from django.http import JsonResponse

from posts.forms import PostForm
from posts.models import Post, Like
from users.models import Follow
from django.contrib.auth.models import User


class PostsFeedView(LoginRequiredMixin,ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created')
    paginate_by = 30
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        followeds = list(Follow.objects.filter(follower = self.request.user))
        if(followeds):
            context['posts']  =  list(Post.objects.filter(profile=followeds[0].following))
            followeds.pop(0)
            for followed in followeds:
                context['posts'] = context['posts'] + list(Post.objects.filter(profile=followed.following))
        else:
            context['posts'] = list(Post.objects.all().order_by('-created')[:10])

        auxposts = []
        for posted in context['posts']:
            liked = False
            like = Like.objects.filter(user=self.request.user,post=posted).exists()
            if like :
                liked = True
            post = {
                'post': posted,
                'liked': liked
            }
            auxposts.append(post);
        context['posts'] = auxposts
        return context


class PostDetailView(LoginRequiredMixin,DetailView):
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']
        liked = Like.objects.filter(user=self.request.user,post=post).exists()
        context['post']={
            'post':post,
            'liked':liked
        }
        return context



class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post"""

    model = Post
    template_name = 'posts/new.html'
    # form_class = PostForm
    fields = ['title', 'photo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile

        form.save()
        return super(CreatePostView, self).form_valid(form)

    def get_success_url(self):
        return reverse('posts:feed')

def like(request):
    user = User.objects.get(username=request.POST['user'])
    post = Post.objects.get(pk=request.POST['post'])
    like = Like(user=user,profile=user.profile,post=post)
    like.save()
    post.likes = post.likes + 1
    post.save()
    return JsonResponse({'message':'ok'})

def dislike(request):
    user = User.objects.get(username=request.POST['user'])
    post = Post.objects.get(pk=request.POST['post'])
    like = Like.objects.get(user=user,profile=user.profile,post=post)
    if like:
        like.delete()
        post.likes = post.likes - 1
        post.save()
        return JsonResponse({'message':'ok'})
    return JsonResponse({'message':'error'})