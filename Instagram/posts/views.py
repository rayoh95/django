from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User

# Create your views here.

# 전체 게시글(내 게시글, 팔로우 게시글) list 페이지 (Read)
def posts(request):
    posts = Post.objects.all()

    context = { 'posts' : posts }
    return render(request, 'posts/list.html', context)


# 게시글 작성 (Create)
def create_post(request):

    user = request.user
    # print('request', request, dir(request))
    # print(request.user)
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect('posts:posts')

    form = PostForm()
    context = { 'form' : form }
    return render(request, 'posts/create_post.html', context)
    
        
# 게시글 읽기 (Read)
def read_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    context = { 'post' : post }
    return render(request, 'posts/post.html', context)


# 게시글 수정 (Update)
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:read_post', pk=pk)
    
    form = PostForm(instance=post)
    context = {'form' : form}
    return render(request, 'posts/update_post.html', context)


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts: posts')


def create_comment():
    return

