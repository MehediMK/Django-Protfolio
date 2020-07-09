
from django.shortcuts import render

from .models import Myskill,Contactinfo


def homepage(request):
    item = Myskill.objects.all()

    title = 'Welcome to TheMMHKbd'

    desc = 'I am Md. Mehedi Hasan Khan, I am full stack web developer'

    context = {
            'title':title,
            'description':desc,
            'data':item
        }

    return render(request,'index.html',context)

def aboutpage(request):
    title = 'About page for skill app'
    desc = """
        Abstract. Grinold provides a general framework for the description of various aspects of a portfolio using a set of factors. ... Grinold first provides a theoretical structure with a model that describes various aspects of a portfolio as either the allocation of a portfolio's variance or as the covariance of two portfolios ...
    """

    context ={
        'title':title,
        'aboutdesc':desc,
    }

    return render(request,'about.html',context)


def contactpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('comments')

        # mydata = Contactinfo(cname = name, cemail = email, cquery = query)
        mydata = Contactinfo()
        mydata.cname = name
        mydata.cemail = email
        mydata.cquery = query
        
        mydata.save()

    return render(request,'contact.html')