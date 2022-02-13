from django.shortcuts import render, get_object_or_404
from IDCO.models import Board
from .forms import BoardForm

# Create your views here.
def list(request):
    # print('Board.objects', Board.objects, type(Board.objects))/채ㅜ'o
    # print('Board.objects.all', Board.objects.all, type(Board.objects.all))
    shurdang = Board.objects.all()
    # for i in shurdang:
    #     if '제목' in i.title:
    #         print(i.title)        
        
    # print('shurdang', shurdang, type(shurdang))
    context = { 'youtube': shurdang } 
    return render(request, 'index/list.html', context)

def create(request):
    
    if request.method == "POST":
        # print('request.POST', request.POST, type(request.POST))
        # board_t = request.POST.get('title')
        # board_c = request.POST.get('content')
        # print('board_t', board_t, type(board_t))
        # print('board_c', board_c, type(board_c))
        # form = Board.objects.create(title=board_t, content=board_c)
        # print('form', form, type(form))
        # return render(request, 'index/success.html')
        # print('if request.method == "POST"', request.method, type(request.method))    # HTML 메서드가 Post 일 경우, 각 매서드와 그 타입을 출력하여 확인한다,
        print('request.POST', request.POST, type(request.POST))
        form = BoardForm(request.POST)
        print('form', form, type(form))
        # print(form, 'form', type(form))       #   form 은 BoardForm(request.POST) 이다.
        if form.is_valid():
            print(form, type(form))
            form.save()
            print(form, type(form))                         #   
            return render(request, 'index/success.html')
        

    else:
    # print('else:', request.method, type(request.method))  # HTML 메서드가 Get 일 경우, 각 매서드와 타입을 출력하여 확인한다.
        youtube = BoardForm()
        # print('youtube', dir(youtube))

    context = { 'shurdang': youtube }
    return render(request, 'index/create.html', context)

def update(request, pk):
    board = get_object_or_404(Board, pk=pk)
    # print('board', board, type(board))
    # print('board.title', board.title, type(board.title))
    # print('board.content', board.content, type(board.content))
    board_test = Board.objects.get(pk=pk)
    print('board_test', board_test, type(board_test), dir(board_test))

    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        # print('form', form, type(form))
        if form.is_valid():
            form.save()
            return render(request, 'index/success.html')

    else:
        form = BoardForm(instance=board)
        # print('form', form, type(form))

    context = { 'form': form }
    return render(request, 'index/update.html', context)