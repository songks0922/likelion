from django.shortcuts import render, redirect
from .models import Post
# Create your views here.


def mypage(request):

    return render(request, 'mypage.html')


def writing(request):
    if request.method == "GET":
        return render(request, 'writing.html')

    elif request.method == "POST":
        post = Post()
        post.user = request.user
        post.content = request.POST["content"]
        post.save()
        return redirect('/')
    return render(request, 'writing.html')


def main(request):

    return render(request, 'main.html')
