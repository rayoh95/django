from django.shortcuts import render, get_object_or_404
from .models import Boards
from .forms import BoardForm

# Create your views here.
def list(request):

    myboard = Boards.objects.all()

    context = {'board' : myboard }
    return render(request, 'index/list.html', context)


def create(request):

    if request.method == "POST": 
        form = BoardForm(request.POST)

        if form.is_valid():
            form.save()   
            return render(request, 'index/success.html')
        
    else:
        myboard = BoardForm()
       
    context = {'board' : myboard }
    return render(request, 'index/create.html', context)


def update(request, pk):
    board = get_object_or_404(Boards, pk=pk)
    board_test = Boards.objects.get(pk=pk)
    print('board_test', board_test, type(board_test), dir(board_test))

    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)

        if form.is_valid():
            form.save()
            return render(request, 'index/success.html')

    else:
        myboard = BoardForm(instance=board)

    context = { 'board': myboard }
    return render(request, 'index/update.html', context)

def delete(request, pk):
    
    board = Boards.objects.get(pk=pk)

    board.delete()
    return render(request, 'index/success.html')

def page(request, pk):
    
    board_test = Boards.objects.get(pk=pk)
    print('board_test', board_test, type(board_test), dir(board_test))
    
    
    context = { 'board' : board_test}
    return render(request, 'index/page.html', context)

    