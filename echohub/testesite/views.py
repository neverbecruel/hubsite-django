from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question



def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "testesite/index.html", context) # request, template path e context


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # model e ORM
    return render(request, "testesite/detail.html",{"question": question})


def results(request, question_id):
    return HttpResponse(f"Você está olhando para o resultado da questão {question_id}")

def vote(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Questão não encontrada.")
    return render(request, "testesite/vote.html", {"question": question}) # request, template path
                                                                                              # e contexto
