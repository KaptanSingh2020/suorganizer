from django.shortcuts import render, get_object_or_404
from django.views.generic import View 

from .models import Post

# This function view is replaced with a class-based view.
def post_list(request):
    return render(request, 'blog/post_list.html', {'post_list': Post.objects.all()})

def post_detail(request, year, month, slug):
    post = get_object_or_404(
        Post,
        pub_date__year=year,
        pub_date__month=month,
        slug=slug
        )
    return render(request, 
        'blog/post_detail.html', 
        {'post': post})

# This code creates class-based views. 
class PostList(View):

    def get(self, request):
        return render(request, 
            'blog/post_list.html', 
            {'post_list': Post.objects.all()})
