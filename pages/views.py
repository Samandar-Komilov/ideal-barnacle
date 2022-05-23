from django.shortcuts import render
from .models import Page

def index(request):
  pg = Page.objects.get(permalink="/")
  context = {
    'title':pg.title,
    'welcome':pg.home_welcome,
    'header':pg.home_header,
  }
  return render(request, "pages/page.html",context)
