from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question

def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date') # 기본은 오름차순, -가 붙면 내림차순
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list' : page_obj}
    for question in page_obj:
        if question.ip_address:
            question.ip_address = question.ip_address.split('.')
            question.ip_address = f"{question.ip_address[0]}.{question.ip_address[1]}"
    # question_list = dao. 데이터를 가져오는 역할.
    # context = dto. 데이터를 담는 그릇이다.
    return render(request, 'pybo/question_list.html',context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id) # 정직하게 오브젝트만 가져옴
    context = {'question' : question}
    if question.ip_address:
        ip_address = question.ip_address.split('.')
        context['ip_address'] = f"{ip_address[0]}.{ip_address[1]}"
    return render(request, 'pybo/question_detail.html', context)