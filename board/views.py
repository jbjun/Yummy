from django.shortcuts import render, redirect
from .forms import BoardWriteForm
from .models import Board

def list(request):
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}

    return render(request,'list.html',context)

def write(request):
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}

    if request.method == 'GET':
        write_from = BoardWriteForm()
        context['forms'] = write_from
        return render(request, 'write.html', context)

    elif request.method == 'POST':
        write_form = BoardWriteForm(request.POST)

        if write_form.is_valid():
            # writer = User.objects.get(user_id=login_session)
            board = Board(
                title=write_form.title,
                contents=write_form.contents,
                # writer=writer,
                board_name=write_form.board_name
            )
            board.save()
            return redirect('/board/list')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
                return render(request, 'board/write.html', context)

def detail(request):
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}

    return render(request,'detail.html', context)