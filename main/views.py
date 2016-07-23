from django.shortcuts import render, HttpResponse
from django.views.generic import View

# Create your views here.
class Sabado(View):
	def get(self,request):
#		return HttpResponse(' Quiubo!!! ')
		return render(request,'hola.html')
