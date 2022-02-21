from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.views.generic import ListView

from main.models import Post, Category

class ShowPost(ListView):

    model = Post
    template_name = 'main/index.html'
    context_object_name = 'posts'
    queryset = get_list_or_404(Post, is_published=True)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        return context

