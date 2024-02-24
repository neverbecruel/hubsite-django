from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question



def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "testesite/index.html", context) # request, template path e context


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # model e ORM
    perguntas = question.choice_set.all()
    if perguntas:
        for choice in question.choice_set.all():
            print(choice.choice_text)
    else:
        print("ERRO")

    return render(request, "testesite/detail.html",{"question": question})


def results(request, question_id):
    return HttpResponse(f"Você está olhando para o resultado da questão {question_id}")


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,"testesite/detail.html",{
                "question": question,
                "error_message": "Você não selecionou uma questão.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("results", args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "testesite/results.html", {"question": question})