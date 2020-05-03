from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from apiDatabase.models import City, Languages
from django.http import JsonResponse

# Create your views here.

def index(request):
	# my_dict = {'insert_me': 'Hello Dynamic, from apiDatabase views.py'}
	# return render(request, 'apiDatabase/index.html', context=my_dict)
	qs = list(Languages.objects.select_related('city').values('city__city_name', 'c', 'c_plus', 'c_sharp', 'dart', 'go', 'haskell', 'html_css', 'java','javaScript', 'kotlin', 'matLab', 'obj_c', 'perl', 'php', 'python', 'r', 'ruby', 'rust','scala', 'swift', 'typeScript', 'visual_basic', 'asp_net', 'angular', 'bootstrap', 'django','ember','flask','laravel', 'node_js', 'rails', 'react','spring','vue_js','ms_sql', 'mongoDB','my_sql','postGreSql', 'redis', 'sqlite'))
	return JsonResponse(qs, safe=False)