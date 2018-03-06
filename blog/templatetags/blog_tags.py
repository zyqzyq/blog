# coding: utf-8
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

from ..models import Post, Category, Tag
from django.db.models.aggregates import Count
from django import template
import markdown2

register = template.Library()


@register.simple_tag()
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag()
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag()
def get_categories():
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag()
def get_tags():
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.filter(is_safe=True)
@register.simple_tag()
def custom_markdown(value):
    return mark_safe(markdown2.markdown(force_text(value),
                                        extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables",
                                                "spoiler"]))