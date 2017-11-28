from django.shortcuts import render

# Create your views here.
def search_page(request):
    return render(request, 'search_course/search_page.html', {})
