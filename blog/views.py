from django.shortcuts import render, get_object_or_404, HttpResponse
from blog.models import Article, Category
from django.contrib.auth.models import User
from account.models import UserInFo
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ArticleCategoryForm, ArticlePostForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


# Create your views here.


def blog_homepage(request):
    return render(request, "blog/homepage.html", locals())


def blog_article(request, article_id):
    # article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)
    # 这个方法能帮我们简化对请求网页不存在时的异常请求
    pub = article.pub_date
    return render(request, "blog/content.html", {"article": article, "pub_date": pub})


def home(request):
    return render(request, 'home.html')


def articles(request):
    return render(request, 'list.html')


def leave_message(request):
    return render(request, 'blog/leave_message.html')


def home_leave_message(request):
    return render(request, 'leave_message.html')


def about(request):
    user_obj = UserInFo.objects.all()
    return render(request, 'blog/about.html', {'user_obj': user_obj})


def words(request):
    return render(request, 'blog/words.html')


def album(request):
    return render(request, 'blog/album.html')


@csrf_exempt
def article_category(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "GET":
        name = Category.objects.filter(user=user)
        column_form = ArticleCategoryForm()
        return render(request, 'blog/article_category.html', locals())
    if request.method == "POST":
        column_name = request.POST['column']
        columns = Category.objects.filter(name=column_name)
        if columns:
            return HttpResponse("2")
        else:
            Category.objects.create(user=user, name=column_name)
            return HttpResponse("1")


@require_POST
@csrf_exempt
def rename_article_column(request):
    column_id = request.POST["column_id"]
    column_name = request.POST["column_name"]

    line = Category.objects.get(id=column_id)
    line.name = column_name
    line.save()
    return HttpResponse("1")


@require_POST
@csrf_exempt
def del_article_column(request):
    column_id = request.POST["column_id"]
    line = Category.objects.get(id=column_id)
    line.delete()
    return HttpResponse("1")


@csrf_exempt
def article_post(request):
    if request.method == "POST":
        column_id = request.POST["column_id"]
        title = request.POST["title"]
        user = User.objects.get(username=request.user.username)
        line = Article.objects.get(category=column_id)
        line.title = title
        line.author = user
        line.save()
        return HttpResponse("1")

    else:
        article_post_form = ArticlePostForm()
        article_columns = Category.objects.all()
        return render(request, 'blog/article_post.html', locals())
