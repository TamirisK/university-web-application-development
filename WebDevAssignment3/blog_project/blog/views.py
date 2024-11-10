# cleaner & more structured version
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post, Comment, Category
from .forms import UserProfileForm, PostForm, CommentForm, SearchForm


# Views for User Profile

@login_required
def edit_profile(request):
    """View to edit the user profile"""
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'blog/profile.html', {'form': form})

def profile_view(request):
    """Simple view to display user profile"""
    return render(request, 'registration/profile.html')


# Views for Post Handling (CRUD)

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5 

    def get_queryset(self):
        queryset = Post.objects.all()

        if self.request.user.is_authenticated:
            if self.request.GET.get('filter_by_author'):
                queryset = queryset.filter(author=self.request.user)

        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            )

        category_filter = self.request.GET.get('category', None)
        if category_filter:
            queryset = queryset.filter(categories__id=category_filter)

        sort_order = self.request.GET.get('sort', 'published_date')
        queryset = queryset.order_by(sort_order)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PostDetailView(DetailView):
    """View to display post details"""
    model = Post
    template_name = 'blog/post_detail.html'

def post_create(request):
    """View to create a new post with multiple categories"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save() 
            form.save_m2m()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    """View to update an existing post with multiple categories"""
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            form.save_m2m()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form})

class PostCreateView(LoginRequiredMixin, CreateView):
    """Class-based view for creating a post"""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """Class-based view for updating a post"""
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """Class-based view for deleting a post"""
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')


# Views for Comment Handling (CRUD)

@login_required
def add_comment(request, post_id):
    """View to add a comment to a post"""
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})

@login_required
def edit_comment(request, comment_id):
    """View to edit a comment"""
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.author:
        return redirect('post_detail', pk=comment.post.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})