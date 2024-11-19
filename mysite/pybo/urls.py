from django.urls import path

from . import views # 현재 디렉토리에 존재하는 모듈중 views.py모듈을 가져와라.

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'), # detail 함수가 실행됨.
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/craete/', views.question_create, name='question_create'),
]