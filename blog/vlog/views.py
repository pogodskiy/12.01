from django.shortcuts import render

posts = [
    {
        'author':'admin',
        'title':'Это мой первый пост',
        'content':'содержимое первого поста',
        'date_posted':'12.01.2023'
     },
    {
        'author':'user',
        'title':'Это мой второй пост',
        'content':'содержимое второго поста',
        'date_posted':'12.01.2023'
    }
]

def index(request):
    context = {
        'posts':posts
    }
    return render(request,'home.html',context)

def about(request):

    return render(request,'about.html',{'title':'О клубе'})

