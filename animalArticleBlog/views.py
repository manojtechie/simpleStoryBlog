from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.  

def blogPost(request):
	# return HttpResponse("This is a Animal Article Blog")
	posts = Post.objects.all() # This line fetch the data from the database
	context= {"posts": posts}
	return render(request,"blogHome.html",context)