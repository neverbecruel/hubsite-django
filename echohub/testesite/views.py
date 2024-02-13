from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Ola, mundo")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    return HttpResponse(f"Você está olhando para o resultado da questão {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Você está votando para a questão {question_id}")