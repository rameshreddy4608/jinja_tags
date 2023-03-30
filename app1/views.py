from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'NAME':'RAMESH'}
    return render(request,'jinja.html',context=d)