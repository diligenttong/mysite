from django import forms
from blog.models import Article, Category
from DjangoUeditor.forms import UEditorField


# class ArticleForm(forms.ModelForm):
#     class Meta:
#         model = Article
#         exclude = ['author', 'views', 'slug', 'pub_date']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'class': 'form-control'}),
#             'category': forms.Select(attrs={'class': 'form-control'}),
#             'tags': forms.CheckboxSelectMultiple(attrs={'class': 'multi-checkbox'}),
#         }

class ArticleCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ("title", "body")
