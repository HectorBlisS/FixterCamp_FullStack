from django.shortcuts import render, HttpResponse
from django.views.generic import View


class Sabado(View):
	def get(self,request):
		# return HttpResponse('Tengo hambre hijo!')
		return render(request,'hola.html')


