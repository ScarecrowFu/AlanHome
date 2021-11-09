from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url, include
from home.views import index, list_articles, article_detail, search_articles
from home.apis import markdown_uploader, like_article

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('martor/', include('martor.urls')),
                  path('grappelli/', include('grappelli.urls')),  # grappelli URLS
                  url(r'^index/$', index, name='index'),  # 首页
                  url(r'^$', index, name='index'),  # 首页
                  url(r'^articles/(?P<instance_id>\d+)/$', list_articles, name='articles'),
                  url(r'^search/$', search_articles, name='search_articles'),
                  url(r'^article/(?P<instance_id>\d+)/$', article_detail, name='article'),


                  path(
                      'api/md_uploader/', markdown_uploader, name='markdown_uploader_page'
                  ),
                  url(r'^api/md_uploader/$', markdown_uploader, name='markdown_uploader_page'),
                  url(r'^api/like_article/(?P<instance_id>\d+)/$', like_article, name='like_article'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
