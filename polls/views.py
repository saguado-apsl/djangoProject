from django.shortcuts import render, get_object_or_404
from polls.models import Question, Choice


def index(request):

    latest_questions_list = Question.objects.order_by('-pub_date')[0:5]

    return render(request, 'index.html', {'question_list': latest_questions_list})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def result(request, question_id):

    question = get_object_or_404(pk=question_id)
    return render(request, 'result.html', {'question': question})


def vote(request, question_id):

    question = get_object_or_404(pk=question_id)
    return render(request, 'vote.html', {'question': question})
