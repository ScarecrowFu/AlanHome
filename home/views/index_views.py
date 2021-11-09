from django.shortcuts import render, HttpResponse
from home.models import Menu, Category, Tag, Article
from django.core.paginator import Paginator
from django.db.models import Sum
from home.utils.base_helpers import get_website_configure


def base_data():
    menus = Menu.objects.all().order_by('-sort')
    random_articles = Article.objects.get_publish().order_by('?').all()[:5]
    tags = Tag.objects.all()
    articles_count = Article.objects.get_publish().count()
    all_view_count = Article.objects.get_publish().aggregate(Sum('view_count'))['view_count__sum']
    if not all_view_count: all_view_count = 0
    website_configure = get_website_configure()
    return {'menus': menus, 'random_articles': random_articles, 'tags': tags,
            'articles_count': articles_count, 'all_view_count': all_view_count, 'website_configure': website_configure}


def index(req):
    # 首页初始化
    data = base_data()
    important_articles = Article.objects.get_publish().filter(sort__gte=100).all()
    if not important_articles:
        important_articles = Article.objects.order_by('?').all()[:5]
    hot_articles = Article.objects.get_publish().order_by('-like_count', '-view_count').all()[:6]
    recommend_articles = Article.objects.get_publish().filter(is_recommend=True).order_by(
        '-like_count', '-view_count').all()[:4]
    latest_articles = Article.objects.get_publish().order_by('-created_time', '-view_count').all()[:6]
    if not recommend_articles:
        recommend_articles = hot_articles[:4]

    return render(req, 'index.html',
                  {
                      **data,
                      'important_articles': important_articles,
                      'hot_articles': hot_articles,
                      'recommend_articles': recommend_articles,
                      'latest_articles': latest_articles,
                  }
                  )


def list_articles(req, instance_id):
    list_type = req.GET.get('type', 'menu')
    is_about = False
    if list_type == 'menu':
        instance = Menu.objects.get(pk=int(instance_id))
        all_articles = Article.objects.get_publish().filter(category__menu=instance).all().order_by(
            '-created_time').distinct()
        if instance.sort < 0:
            is_about = True
    elif list_type == 'category':
        instance = Category.objects.get(pk=int(instance_id))
        all_articles = Article.objects.get_publish().filter(category=instance).all().order_by(
            '-created_time').distinct()
        if instance.menu.sort < 0:
            is_about = True
    elif list_type == 'tag':
        instance = Tag.objects.get(pk=int(instance_id))
        all_articles = Article.objects.get_publish().filter(tags=instance).all().order_by(
            '-created_time').distinct()
    else:
        instance = None
        all_articles = []
    page = int(req.GET.get('page', 1))
    page_size = int(req.GET.get('page_size', 10))
    p_articles = Paginator(all_articles, page_size)
    articles = p_articles.page(page)
    data = base_data()
    render_html = 'articles.html'
    if is_about: render_html = 'about.html'
    return render(req, render_html,
                  {
                      **data,
                      'articles': articles,
                      'page': page,
                      'page_size': page_size,
                      'page_count': len(all_articles),
                      'page_total': p_articles.num_pages,
                      'type': list_type,
                      'instance': instance,
                  }
                  )


def search_articles(req):
    keyword = req.GET.get('keyword', None)
    all_articles = Article.objects.get_publish().filter(title__icontains=keyword).distinct()
    page = int(req.GET.get('page', 1))
    page_size = int(req.GET.get('page_size', 10))
    p_articles = Paginator(all_articles, page_size)
    articles = p_articles.page(page)
    data = base_data()
    render_html = 'articles.html'
    return render(req, render_html,
                  {
                      **data,
                      'articles': articles,
                      'page': page,
                      'page_size': page_size,
                      'page_count': len(all_articles),
                      'page_total': p_articles.num_pages,
                      'keyword': keyword,
                  }
                  )


def article_detail(req, instance_id):
    article = Article.objects.get(pk=int(instance_id))
    next_article = Article.objects.get_publish().filter(created_time__gt=article.created_time).order_by('created_time').first()
    prev_article = Article.objects.get_publish().filter(created_time__lt=article.created_time).order_by('-created_time').first()
    related_articles = Article.objects.get_publish().filter(tags__in=article.tags.all()).exclude(id=article.id).order_by('-created_time').all()[:6]
    data = base_data()
    article.view_count = article.view_count+1
    article.save()
    return render(req, 'detail.html',
                  {
                      **data,
                      'article': article,
                      'prev_article': prev_article,
                      'next_article': next_article,
                      'related_articles': related_articles,
                  }
                  )