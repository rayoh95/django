from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Comment
from .forms import BoardForm, CommentForm
from django.db.models import Q

# Create your views here.

#Boards 는 게시글들의 목록을 볼 수 있는 게시판
def boards(request):

    boards = Board.objects.all()
    keyWord = ""
    if request.method == "POST":
        keyWord = request.POST.get('keyWord',"")
        
        if keyWord:
            boards = Board.objects.filter(Q(title__icontains=keyWord) | Q(content__icontains=keyWord)).order_by("-id")
       

    context = {'boards':boards, 'keyWord':keyWord}
    return render(request, 'index/Boards.html', context)


#Create_post 는 게시글 한 개 쓰기
def create_board(request):

    if request.method == "POST":
        form = BoardForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'index/success.html')
   
    board = BoardForm()
    context = { 'board' : board } 
    return render(request, 'index/Board.html', context)


def update_board(request, pk):

    board = get_object_or_404(Board, pk=pk)

    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)

        if form.is_valid():
            form.save()
            return render(request, 'index/success.html')
        
    board = BoardForm(instance=board)
    context = {'board':board}
    return render(request, 'index/update.html', context)

def delete_board(request, pk):

    board = Board.objects.get(pk=pk)

    board.delete()
    return render(request, 'index/success.html')

def page(request, pk):

    board = get_object_or_404(Board, pk=pk)
    comments = board.comment_set.all()

    context = {'board' : board, 'comments' : comments }
    return render(request, 'index/page.html', context)

def create_comment(request, pk):

    board = get_object_or_404(Board, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = board     
            comment.save()
            return redirect('Boards:page', pk=board.pk)
    else:
        form = CommentForm()
    context = { 'form' : form }
    return render(request, 'index/comment.html', context)        


def delete_comment(request, board_id, comment_id):

    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    
    return redirect('Boards:page', board_id)

def update_comment(request, board_id, comment_id):

    board = board_id
    pk = comment_id
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            comment.save()
            return redirect('Boards:page', pk=board)
    else:
        form = CommentForm(instance=comment)
    context = { 'form' : form }
    return render(request, 'index/update_comment.html', context)
