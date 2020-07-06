from django.shortcuts import render
from django.urls import reverse

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Article
from .forms import ArticleModelForm
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    ListView,
    DetailView,
)


# Create your views here.


def article_list_view(request):
    queryset = Article.objects.all()

    context = {
        "object_list": queryset
    }

    return render(request,'articles/article_list.html', context)

def article_detail_view(request, id):
    obj = Article.objects.get(id=id)

    context = {
        "object_detail": obj
    }

    return render(request,'articles/article_detail.html', context)

def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        "form": form
    }

    return render(request, 'article/article_create.html', context)

def article_update_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()

        context = {
            "form": form
        }

    return render(request,'articles/article_update.html', context)


def article_delete_view(request, id):
    obj = get_object_or_404(Article, id=id)

    if request.method == "POST":
        obj.delete()

        return redirect('../../')

    context = {
        "object": obj
    }

    return render(request,"articles/article_delete.html", context)

def dynamic_lookup_view(request, id):
    try:
        obj = Article.objects.get(id=id)

    except Article.DoesNotExist.get(id=id):
        raise Http404

        context = {
        "object": obj
        }

    return render(request,'articles/article_detail.html', context)


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name ='articles/article_create.html'
    form = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #     return '/'

class ArticleUpdateView(UpdateView):
    template_name ='articles/article_create.html'
    form = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article_list')
