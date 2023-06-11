from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CategoryForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.

#def homePageView(request):
#   return render(request, 'index.html', {'name': 'Artur'})

class LikeView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, id=pk)
        user = request.user

        if user.is_authenticated:
            if post.likes.filter(id=user.id).exists():
                post.likes.remove(user)  # Unlike the post
            else:
                post.likes.add(user)  # Like the post

        redirect_url = request.META.get('HTTP_REFERER')  # Get the referring URL

        if reverse('post_detail', kwargs={'pk': pk}) in redirect_url:
            return HttpResponseRedirect(redirect_url)  # Stay on the post_detail page

        return redirect('home')  # Redirect to home page if not on the post_detail page


class HomePageView(ListView):
    model = Post
    template_name = "index.html"
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' ')).order_by('-post_date')
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})


class PostDetailView(DetailView):
    model = Post
    template_name = "detail_post.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["liked"] = False

        if self.request.user.is_authenticated:
            post = self.get_object()
            if post.likes.filter(id=self.request.user.id).exists():
                context["liked"] = True

        return context

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    #fields = '__all__'

class CreateCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'create_comment.html'
    #fields = '__all__'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})


class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create_category.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

