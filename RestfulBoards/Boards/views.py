from django.shortcuts import render, get_object_or_404
from .models import Board
from .forms import BoardForm

# Create your views here.

#Boards 는 게시글들의 목록을 볼 수 있는 게시판
def Boards(request):

    board = Board.objects.all()

    context = {'board' : board }
    return render(request, 'index/Boards.html', context)




#Board 는 게시글 한 개 쓰기
def Create_post(request):\

    if request.method == "POST": 
        form = BoardForm(request.POST)

        if form.is_valid():
            form.save()   
            return render(request, 'index/success.html')
        
    else:
        board = BoardForm()
       
    context = {'board' : board }
    return render(request, 'index/Board.html', context)


def update_post(request, pk):

    board = get_object_or_404(Board, pk=pk)
    
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)

        if form.is_valid():
            form.save()
            return render(request, 'index/success.html')

    else:
        board = BoardForm(instance=board)

    context = { 'board': board }
    return render(request, 'index/update.html', context)



def delete_post(request, pk):

    board = Board.objects.get(pk=pk)

    board.delete()
    return render(request, 'index/success.html')

def page(request, pk):
    
    board = Board.objects.get(pk=pk)
   
    context = { 'board' : board }
    return render(request, 'index/page.html', context)
