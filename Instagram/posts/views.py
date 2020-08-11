from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.

# 전체 게시글(내 게시글, 팔로우 게시글) list 페이지 (Read)
def posts(request):
    posts = Post.objects.all()

    context = { 'posts' : posts }
    return render(request, 'posts/list.html', context)


# 게시글 작성 (Create)
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('posts:posts')

    post = PostForm()
    context = { 'post' : post } 
    return render(request, 'posts/create_post.html', context)
    
        
# 게시글 읽기 (Read)
def read_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    context = { 'post' : post }
    return render(request, 'posts/post.html', context)
