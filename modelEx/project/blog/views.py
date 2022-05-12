from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .form import BlogForm
from django.core.paginator import Paginator

def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    pagnum = request.GET.get('page')
    blogs = paginator.get_page(pagnum)
    return render(request, "home.html", {'blogs': blogs})


def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.view_cnt += 1
    blog.save()
    return render(request, 'detail.html', {'blog': blog})


def new(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home.html')
    else:
        form = BlogForm()
        return render(request, "new.html", {'form':form})

def create(request):
    new_blog = Blog()  # 빈 Blog 객체 생성
    new_blog.title =  request.POST['title']
    # POST요청으로 받은 'title'의 데이터를 위에서 만든 객체의 title 컬럼에 할당
    new_blog.content = request.POST['content']
    # POST요청으로 받은 'contents'의 데이터를 위에서 만든 객체의 contents 컬럼에 할당
    new_blog.image = request.FILES['image']
    new_blog.save() #실제 데이터베이스에 저장을 시키게 한다.
    return redirect('detail',new_blog.id) #새로 만들어준 상세페이지로 redirect한다

def edit(request,id):
    edit_blog = get_object_or_404(Blog, pk = id) # 파라미터 id를 받아서 디비에 해당 객체를 가져온다.

    # if request.method == 'POST':
    #     form = BlogForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home.html')
    # else:
    #     form = BlogForm()
    #     return render(request, "edit.html", {'form':edit_blog})
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request,id):
    update_blog = get_object_or_404(Blog, pk=id) # 파라미터로 받은 id의 Blog 객체 가져옴
    update_blog.title = request.POST['title']
    update_blog.content = request.POST['content']
    if request.FILES['image']:
        update_blog.image = request.FILES['image']
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request,id):
    delete_blog  = get_object_or_404(Blog, pk = id) #파라미터로 받은 id에 해당하는 Blog객체 가져옴
    delete_blog.delete() #삭제
    return redirect('home')

def scrap(request,id):
    blog = get_object_or_404(Blog, pk = id) #파라미터로 받은 id에 해당하는 Blog객체 가져옴
    if blog.scrap == False:
        blog.scrap = True
    else:
        blog.scrap = False
    blog.save()
    return render(request, 'detail.html', {'blog': blog})