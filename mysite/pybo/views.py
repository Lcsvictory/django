from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseNotAllowed
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

'''
views에서 모든 귀찮은 작업을 모두 거쳐서 정제된 데이터들만 html로 보내는구나. DAO 역할을 수행하는것이 views구나.

제네릭 뷰는 데이터 조회, 수정, 삭제, 추가 같은 정형화된 작업들을 미리 클래스로 만들어놓은 뷰를 말한다. 일반 뷰를 사용하다가 반복됨을 체감할때 사용해보자.
'''


def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date') # 기본은 오름차순, -가 붙으면 내림차순
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    # question_list = dao. 데이터를 가져오는 역할.
    context = {'question_list' : page_obj}
    # context = dto. 데이터를 담는 그릇이다.
    return render(request, 'pybo/question_list.html',context)

def detail(request, question_id):
    # question = Question.objects.get(id=question_id) # 정직하게 오브젝트만 가져옴
    question = get_object_or_404(Question, pk=question_id) # 오브젝트가 없으면 404에러를 가져옴 
    ip_address = request.META.get('REMOTE_ADDR', 'ip주소가 없습니다.')
    context = {'question' : question, 'ip_address' : ip_address}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # return redirect('pybo:detail', question_id=question_id)
    # 동일한 결과.
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid(): # invalid, 유효하지 않다면
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible')
    context = {'question' :question, 'form' :form} # 유효하지 않은 데이터를 html로 보낸다.
    return render(request, 'pybo/question_detail.html', context)


def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)