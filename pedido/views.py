from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views import View

class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse("Pagar")

class SalvarPedido(View):
    pass

class Detalhe(View):
    pass


