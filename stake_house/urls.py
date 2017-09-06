import main_app.views as main_app
"""stake_house URL Configuration

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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main_app.main_page),
    url(r'^user/login/$', main_app.login),
    url(r'^user/logout/$', main_app.logout),

    url(r'^stakes/$', main_app.stakes),
    url(r'^contacts/$', main_app.contacts),
    url(r'^galary/$', main_app.galary),
    url(r'^menu/$', main_app.menu),
    url(r'^news/$', main_app.news),
    url(r'^reviews/$', main_app.reviews),
]
