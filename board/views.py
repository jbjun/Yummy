from django.shortcuts import render, redirect
from .forms import BoardWriteForm
from .models import Board
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404

class BoardListView(ListView):
    model = Board
    paginate_by = 5
    template_name = 'board/board_list.html'
    context_object_name = 'board_list'

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        board_list = Board.objects.order_by('-id')

        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'all':
                    search_board_list = board_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
                            writer__user_id__icontains=search_keyword))
                elif search_type == 'title_content':
                    search_board_list = board_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword))
                elif search_type == 'title':
                    search_board_list = board_list.filter(title__icontains=search_keyword)
                elif search_type == 'contents':
                    search_board_list = board_list.filter(contents__icontains=search_keyword)
                elif search_type == 'writer':
                    search_board_list = board_list.filter(writer__user_id__icontains=search_keyword)

                return search_board_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')

        return board_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 5
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')

        if len(search_keyword) > 1:
            context['q'] = search_keyword
        context['type'] = search_type

        return context



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

def board_detail_view(request, pk):
    board = get_object_or_404(Board, pk=pk)
    # session_cookie = request.session['writer']
    # cookie_name = F'notice_hits:{session_cookie}'
    context = {
        'board': board
    }
    # response = render(request, 'notice/notice_detail.html', context)
    #
    # if request.COOKIES.get(cookie_name) is not None:
    #     cookies = request.COOKIES.get(cookie_name)
    #     cookies_list = cookies.split('|')
    #     if str(pk) not in cookies_list:
    #         response.set_cookie(cookie_name, cookies + f'|{pk}', expires=None)
    #         board.hits += 1
    #         board.save()
    #         return response
    # else:
    #     response.set_cookie(cookie_name, pk, expires=None)
    #     board.hits += 1
    #     board.save()
    #     return response

    return render(request,'board/board_detail.html', context)