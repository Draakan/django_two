# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def journal_list(request):
	journals = (
		{'id': 1,
		  'name': u'Віталій',
		  'last_name': u'Подоба'},
		{'id': 2,
		  'name': u'Андрій',
		  'last_name': u'Корост'},
		{'id': 3,
		  'name': u'Тарас',
		  'last_name': u'Притула'},
)
	return render(request, 'students/journal_list.html', 
    		{'journals' : journals})
