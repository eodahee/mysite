from django.http import HttpResponse
from django.shortcuts import render
from polls.models import Question, Choice
from django.utils import timezone

def result(request, id) :  # 투표의 결과를 보여줌
    question = Question.objects.get(pk=id)
    return render(request, 'polls/result.html', {'question' : question})

def add_question(request) :  # 질문을 추가하고난 다음 페이지
    text = request.POST['text']
    q = Question(question_text=text, pub_date=timezone.now())
    q.save()
    return render(request, 'polls/add_question.html', {})

def input(request) :  # 질문을 추가 할 페이지
    return render(request, 'polls/input.html', {})

def data(request, email, number) :  # data를 확인 할 페이지
    # http://localhost:8000/polls/data?user_name=kim
    value = request.GET['user_name']
    return HttpResponse(value + email + str(number))

def vote(request) :  # 투표 할 페이지
    choice = request.POST['choice']
    print('@^_^@', choice) # 서버에 client의 결과를 보여주게끔
    c = Choice.objects.get(pk=choice)
    c.votes += 1
    c.save()

    return render(request, 'polls/vote.html', {})

def detail(request, id) :  # DB에 입력되어 있는 질문과 답변의 보기를 보여주는 페이지
    question = Question.objects.get(id=id)
    return render(request, 'polls/detail.html', {'item' : question})

def index(request) :  # 질문 리스트들을 출력해줄 페이지(a태그 이용 링크걸기)
    # return HttpResponse('index!!!') 단순히 화면출력을 위한 것
    list = Question.objects.all()
    return render(request, 'polls/index.html', {'question' : list})