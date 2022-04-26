from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import get_user_model

# Create your views here.

# 인덱스 페이지
def index(request):
    user = request.user

    if user.is_authenticated:        
        return redirect('posts:posts')
    else:
        return redirect('accounts:login')


# 전체 게시글(내 게시글, 팔로우 게시글) list 페이지 (Read)
def posts(request):
    posts = Post.objects.all()
    
    context = { 'posts' : posts }
    return render(request, 'posts/list.html', context)

    # followings = request.user.followings.values_list("-id", flat=True)
    # followings.append(request.user.id)
    
    # posts = Post.objects.filter(user__in=followings).order_by("-id")
    # context = {'posts', posts}

    # return render(request, 'posts/list.html', context)


# 게시글 작성 (Create)
def create_post(request, user_id):

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
def read_post(request, pk, user_id):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.all()
    people = get_object_or_404(get_user_model(), id=user_id)

    context = { 'post' : post, 'comments' : comments, 'people' : people }
    return render(request, 'posts/post.html', context)

# 게시글 수정 (Update)
def update_post(request, pk, user_id):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:read_post', pk=pk, id=user_id)
    
    form = PostForm(instance=post)
    context = {'form' : form}
    return render(request, 'posts/update_post.html', context)

# 게시글 삭제 (Delete)
def delete_post(request, pk, user_id):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:read_post', pk=pk, id=user_id)

# 댓글 작성 (Create)
def create_comment(request, pk, user_id):
    
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        message = request.POST.get('message')

        if not message:
            return HttpResponse('댓글 내용을 입력하세요', status=400)
        
        Comment.objects.create( post=post, author=request.user, message=message)
        return redirect('posts:read_post', id=user_id, pk=pk)
    
    form = CommentForm()
    context = { 'form' : form }
    return render(request, 'posts/create_comment.html', context)

# 댓글 읽기 (Read)
def read_comments(request, pk, user_id):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.all()
    
    context = { 'post' : post, 'comments' : comments }
    return render(request, 'posts/read_comments.html', context)

# 댓글 수정 (Update)
def update_comment(request, post_id, comment_id, user_id):

    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            comment.save()
            return redirect('posts:read_post', pk=post_id, id=user_id)
    
    form = CommentForm(instance=comment)
    context = { 'form' : form }
    return render(request, 'posts/update_comment.html', context)

# 댓글 삭제 (Delete)
def delete_comment(request, post_id, comment_id, user_id):

    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    
    return redirect('posts:read_post', pk=post_id, id=user_id)

# 검색 기능(검색이 이뤄지지 않았을 때는, 모든 게시물을 보여준다.)
def search_post(request):

    posts = Post.objects.all()
    keyword = ""

    if request.method == "POST":
        keyword = request.POST.get('keyword',"")  
        
        if keyword:
            posts = Post.objects.filter(Q(title__icontains=keyword) | Q(content__icontains=keyword) | Q(author__username__icontains=keyword)).order_by("-id")
        
    context = {'posts':posts, 'keyword':keyword}
    return render(request, 'posts/search_post.html', context)

# 좋아요 기능(좋아요 수 나타내기 용도)
def like(request, post_id, user_id):
    post = get_object_or_404(Post, pk = post_id)

    if post.likes.filter(username=request.user.username).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    post.save()
    return redirect('posts:read_post', post_id, user_id)

# 좋아요 리스트(좋아요 누른 개시물 보기)
# def like_list(request, user_id):
#     posts = Post.objects.all()

#     if request.user.is_authenticated:
#         posts = Post.likes.all(username=request.user.username)
#         context = {'posts' : posts}
#         return render(request, 'posts/like_list.html', context )
#     else:
#         context = {'post' : posts}
#         return render(request, 'posts/like_list.html', context )


# 나의 게시물만 모아둔 페이지
def my_page(request):
    user = request.user
    posts = Post.objects.filter(author__username=user).order_by("-id")
    
    context = {'posts': posts}
    return render(request, 'posts/my_page.html', context)