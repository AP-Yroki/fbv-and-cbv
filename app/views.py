from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .forms import NewsForm, CategoryForm, AuthorForm, PublisherForm, \
    ConfirmForm
from django.http import HttpResponseNotFound
from django.views import View


class NewsListView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'news_list.html', {
            'news': News.objects.all(),
        })


class AddNewsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_news.html', {
            'form': NewsForm(),
        })

    def post(self, request, *args, **kwargs):
        form = NewsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')

        return self.get(request)


class NewsUpdateView(View):

    def get(self, request, id, *args, **kwargs):
        news = get_object_or_404(News, id=id)
        return render(request, 'edit.html', {
            'form': NewsForm(instance=news)
        })

    def post(self, request, id, *args, **kwargs):
        news = get_object_or_404(News, id=id)
        form = NewsForm(instance=news, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list', id=news.id)
        return self.get(request, id)


class NewsDeleteView(View):
    def get(self, request, id, *args, **kwargs):
        news = get_object_or_404(News, id=id)

        return render(request, 'confirm_delete.html', {
            'news': news,
            'form': ConfirmForm(),
        })

    def post(self, request, id, *args, **kwargs):
        news = get_object_or_404(News, id=id)
        form = ConfirmForm(data=request.POST)
        if form.is_valid():
            news.delete()
            return redirect('news_list')

        return self.get(request, id)

class NewsMainPageView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {
            'news': News.objects.all(),
        })


class AddCategoryView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_category.html', {
            'form': CategoryForm(),
        })

    def post(self, request, *args, **kwargs):
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        return self.get(request)


class AddAuthorView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_author.html', {
            'form': AuthorForm(),
        })

    def post(self, request, *args, **kwargs):
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        return self.get(request)


class AddPublisherView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_publisher.html', {
            'form': PublisherForm(),
        })

    def post(self, request, *args, **kwargs):
        form = PublisherForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        return self.get(request)
