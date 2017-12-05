from django.shortcuts import render, redirect
from .forms import CoursesForm
from .models import OneSearch
from .search_class.search_class import search
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def get_form(form):
    def wrap_keys(d, *args):
        for k in args:
            d[k] = ['dummy', d[k]]

    new_form = dict(form)
    new_form.pop('email', None)
    if new_form['sel_day'] == []:
        new_form['sel_day'] = ['dummy', '%']
    else:
        new_form['sel_day'] = ['dummy'] + new_form['sel_day']
    wrap_keys(new_form, 'sel_attr', 'sel_camp', 'sel_insm',
              'sel_ptrm', 'sel_schd', 'sel_sess', 'sel_subj', 'sel_instr',)
    # manually add keys and values
    new_form['term_in'] = '201820'
    new_form['sel_levl'] = 'dummy'
    return new_form


@login_required
def search_page(request):
    user = User.objects.get(username=request.user)
    form = CoursesForm()
    return render(request, 'search_course/search_page.html', {'form':form})


@login_required(login_url='')
def userPage(request):
    user = User.objects.get(username=request.user)
    searches = OneSearch.objects.all().order_by('-id')
    searchList=[]
    for i in searches:
        if i.creator == user:
            searchList.append(i)
    return render(request, 'search_course/userPage.html',{'searches':searchList})


def result_page(request):
    if request.method == "POST":
        form = CoursesForm(request.POST)
        if form.is_valid():
            s = search()
            new_form = get_form(form.cleaned_data)
            courses = s.get_courses(new_form)
            new_search = OneSearch(csn=new_form['sel_crse'], subj=new_form['sel_subj'],creator=request.user)
            # new_search.emailAdd=new_form['email']
            new_search.save()
            # for debug print
            # for c in courses:
            #     print(c.course_info)

            return render(request, 'search_course/result_page.html', {'courses': courses})
    else:
        form = CoursesForm()
    return redirect('search_page')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('search_page')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

# def login(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username,password=raw_password)
#             login(request, user)
#             return search_page(request)
#     else:
#         form = UserCreationForm()
#     return render(request, 'search_course/login.html', {'form':form})
