# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    universities = University.objects.all()
    professors = Professor.objects.all()
    context = {
        'universities': universities,
        'professors': professors
    }
    return render(request, 'app/note.html', context)


def search_form(request):
    universities = University.objects.all()
    professors = Professor.objects.all()
    context = {
        'universities': universities,
        'professors': professors
    }
    return render(request, 'app/search.html', context)


def search(request):
    queryset = []
    n_ids = {}
    universities = University.objects.all()
    professors = Professor.objects.all()

    if 'q' in request.GET:
        queries = request.GET['q'].replace("-", " ")
        queries = queries.split()
        u_ids = request.GET.getlist('uni')
        p_ids = request.GET.getlist('pro')
        for query in queries:
            tag_ids = Tag.objects.filter(t_name__contains=query).values('t_id')
            note_ids = NoteTag.objects.filter(t_id__in=tag_ids).values('n_id')
            notes = Note.objects.filter(n_id__in=note_ids, u_id__in=u_ids, p_id__in=p_ids)
            for n in notes:
                if n.n_id not in n_ids:
                    queryset.append(n)
                    n_ids[n.n_id] = 1
                else:
                    n_ids[n.n_id] += 1

        queryset.sort(key=lambda x: n_ids[x.n_id], reverse=True)

        uni = {}
        pro = {}

        for note in queryset:
            uid = Note.objects.filter(n_id=note.n_id).values('u_id')
            uni[note.n_id] = University.objects.get(u_id__in=uid)
            pid = Note.objects.filter(n_id=note.n_id).values('p_id')
            pro[note.n_id] = Professor.objects.get(p_id__in=pid)

        context = {
            'notes': queryset,
            'uni': uni,
            'prof': pro,
            'universities': universities,
            'professors': professors
        }

        return render(request, 'app/search-result.html', context)
    else:
        return HttpResponse("<html>Please enter valid search query!</html>")


def register(request):
    return render(request, 'app/registration.html')


def login(request):
    return render(request, 'app/login.html')


def add_user(request):
    user_name = request.POST.get('fname', 'not')
    print(user_name)
    return HttpResponse("<html>User " + user_name + " added!</html>")
