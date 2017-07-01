"""newface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from auth import views as auth
from item import views as item

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', item.home, name='home'),
    url(r'^signin/$', auth.login), 
    url(r'^logout/$', auth.logout), 
    url(r'^signup/$', auth.join), 
    url(r'^items/$', item.Items.as_view()), 
    url(r'^items/(?P<item_id>\d*)/$', item.ItemDetail.as_view()), 
    url(r'^questions/$', item.Questions.as_view()), 
    url(r'^questions/(?P<question_id>\d*)/$', item.QuestionDetail.as_view()), 
]
