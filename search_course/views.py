from django.shortcuts import render, redirect
from .forms import UserForm
from .search_class.search_class import search
# Create your views here.

def get_form(form):
    def wrap_keys(d, *args):
        for k in args:
            d[k] = ['dummy', d[k]]
    
    new_form = dict(form)
    new_form.pop('email', None)
    wrap_keys(new_form, 'sel_attr', 'sel_camp', 'sel_insm',
              'sel_ptrm', 'sel_schd', 'sel_sess', 'sel_subj')
    # manually add keys and values
    new_form['sel_instr'] = ['dummy', '%']
    new_form['sel_day'] = ['dummy']
    new_form['term_in'] = '201820'
    new_form['sel_levl'] = 'dummy'
    return new_form


def search_page(request):
    form = UserForm()
    return render(request, 'search_course/search_page.html', {'form':form})


def result_page(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            s = search()            
            courses = s.get_courses(get_form(form.cleaned_data))
            # for debug print
            # for c in courses:
            #     print(c.course_info)
            
            return render(request, 'search_course/result_page.html', {'courses': courses})
    else:
        form = UserForm()
    return redirect('search_page')
