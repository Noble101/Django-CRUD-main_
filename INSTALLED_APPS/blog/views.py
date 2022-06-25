from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.views import Post
from django.views import reverse_lazy

class PostListView(generic.ListView):
    model = Post

class  PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class  PostDetailView(generic.DetailView):
    model = Post

class  PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class  PostDeleteView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")