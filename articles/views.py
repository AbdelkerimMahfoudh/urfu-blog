from django.shortcuts import render,redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url='/')
def articles(request):
    articles=Article.objects.all().order_by('date')
    return render(request,'articles/articles.html',{'articles':articles})

@login_required(login_url='/')
def articles_details(request,slug):
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article.html', { 'article': article })
    # return HttpResponse(slug)


@login_required(login_url='/account/login')
def create_article(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request,'articles/create_article.html',{'form':form})

