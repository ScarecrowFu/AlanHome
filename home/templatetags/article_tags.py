import re
from django import template
from bs4 import BeautifulSoup
from markdown import markdown


register = template.Library()


@register.simple_tag
def get_menu_articles(menu, num=6):
    return menu.get_articles().all()[:num]


@register.filter
def format_time(t):
    return t.strftime('%Y-%m-%d %H:%M:%S')


@register.filter
def page_range(number):
    return range(number)


@register.filter
def markdown_to_text(markdown_string, sub=None):
    """ Converts a markdown string to plaintext """
    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown(markdown_string)
    # remove code snippets
    html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
    html = re.sub(r'<code>(.*?)</code >', ' ', html)
    # extract text
    soup = BeautifulSoup(html, "html.parser")
    text = ''.join(soup.findAll(text=True))
    if sub:
        return text[:sub]
    return text
