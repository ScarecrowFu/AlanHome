from django.db import models
import time
from martor.models import MartorField


class Menu(models.Model):
    name = models.CharField(max_length=255, verbose_name='菜单名称')
    sort = models.IntegerField(default=0, verbose_name='排序值权重', help_text='权重越大越靠前')
    creator = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='创建者',
                                related_name='user_menus')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')

    class Meta:
        db_table = 'menu'
        verbose_name = '菜单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_articles(self):
        return Article.objects.filter(category__menu=self).order_by('-created_time').all()


class Category(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE, verbose_name='所属菜单', related_name='menu_categories')
    sort = models.IntegerField(default=0, verbose_name='排序值权重', help_text='权重越大越靠前')
    name = models.CharField(max_length=255, verbose_name='类型名称')
    creator = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='创建者',
                                related_name='user_categories')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')

    class Meta:
        db_table = 'category'
        verbose_name = '类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='标签名称')
    sort = models.IntegerField(default=0, verbose_name='排序值权重', help_text='权重越大越靠前')
    creator = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='创建者',
                                related_name='user_tags')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')

    class Meta:
        db_table = 'tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 上传文件目录
def upload_cover_path(instance, filename):
    file_path = f'cover/{instance.title}/{int(time.time())}/{filename}'
    return file_path


class ArticleManager(models.Manager):
    def get_publish(self):
        return self.filter(status=20, is_deleted=False)


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='文档标题')
    # 记录修改时上一次的文档内容
    # pre_content = MartorField(blank=True, verbose_name='文档内容')
    description = MartorField(blank=True, verbose_name='簡介')
    content = MartorField(blank=True, verbose_name='文档内容')
    cover = models.ImageField(upload_to=upload_cover_path, blank=True, null=True, verbose_name='封面')
    sort = models.IntegerField(default=0, verbose_name='排序值权重', help_text='权重越大越靠前')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签', related_name='tag_articles')
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL,
                                 verbose_name='所属类型', related_name='category_articles')
    creator = models.ForeignKey('User', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='创建者',
                                related_name='created_articles')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建日期')
    # 10表示草稿状态，20表示发布状态
    status = models.IntegerField(default=10,  choices=((10, '草稿'), (20, '发布')), verbose_name='文档状态')
    is_deleted = models.BooleanField(default=False, verbose_name='已删除')
    is_recommend = models.BooleanField(default=False, verbose_name='是否推荐')
    view_count = models.IntegerField(default=0, verbose_name='观看次数')
    like_count = models.IntegerField(default=0, verbose_name='点赞次数')

    class Meta:
        db_table = 'article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    objects = ArticleManager()