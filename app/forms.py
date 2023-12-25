from django import forms
from .models import News, Category, Author, Publisher



class ConfirmForm(forms.Form):
    confirm = forms.BooleanField(label='Вы точно хотите удалить этот пост?', required=True)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'image', 'category', 'author', 'publishers']

    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select())
    author = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.Select())
    publishers = forms.ModelMultipleChoiceField(queryset=Publisher.objects.all(), widget=forms.SelectMultiple())