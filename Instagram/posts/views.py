from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q

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
    comments = post.comment_set.all()

    context = { 'post' : post, 'comments' : comments  }
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

# 게시글 삭제 (Delete)
def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts: posts')

# 댓글 작성 (Create)
def create_comment(request, pk):
    
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        message = request.POST.get('message')

        if not message:
            return HttpResponse('댓글 내용을 입력하세요', status=400)
        
        Comment.objects.create( post=post, author=request.user, message=message)
        return redirect('posts:read_post', pk=pk)
    
    form = CommentForm()
    context = { 'form' : form }
    return render(request, 'posts/create_comment.html', context)

# 댓글 수정 (Update)
def update_comment(request, post_id, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            comment.save()
            return redirect('posts:read_post', pk=post_id)
    else:
        form = CommentForm(instance=comment)
    context = { 'form' : form }
    return render(request, 'posts/update_comment.html', context)

# 댓글 삭제 (Delete)
def delete_comment(request, post_id, comment_id):

    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    
    return redirect('posts:read_post', post_id)

# 검색 기능
def search_post(request):

    if request.method == "POST":
        keyword = request.POST.get('keyword',"")  
        
        if keyword:
            posts = Post.objects.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(author__username__icontains=keyword)).order_by("-id")
            context = {'posts':posts, 'keyword':keyword}
            return render(request, 'posts/search_post.html', context)

    return render(request, 'posts/search_post.html')


# 좋아요 기능
def like(request, post_id):
    post = get_object_or_404(Post, pk = post_id)

    if post.likes.filter(username=request.user.username).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    post.save()
    return redirect('posts:read_post', post_id)


# # 좋아요 확인
# def like_list(request):
#     posts = Post.objects.all()

#     if request.user.is_authenticated:
#         posts = Post.likes.get(username=request.user.username)
#         context = {'posts' : posts}
#         return render(request, 'posts/like_list.html', context )
        

#     else:
#         context = {'post' : posts}
#         return render(request, 'posts/like_list.html', context )


# 팔로우 기능
def follow():
    
    return()