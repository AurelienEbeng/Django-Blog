from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


posts = [
    
    {
        'author': 'Marry',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'July 12 2023'
    },
    
    {
        'author': 'James',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted':'Sep 22 2023'
    }
    
    
 ]






# Create your views here.
def home(request):
    ###return HttpResponse("<h1>Home Page</h1>")
    return render(request, "blog/home.html", {'posts': Post.objects.all(), 'title': 'Welcome Page'})



def about(request):
    ##return HttpResponse("<h1>About Us Page</h1>")
    return render(request, "blog/about.html",{'title':'About Us'})
    

    
