"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include, handler400, handler403, handler404, handler500
from django.contrib import admin
from users.views import register_view,login_view, logout_view
from Articles.views import error

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('Articles.urls', namespace="articles")),
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^comment/', include("Comments.urls"), name='comment'),
    url(r'^api/users/', include('users.API.urls',namespace="users-api")),
    url(r'^api/articles/', include('Articles.api.urls',namespace="articles-api")),
    url(r'^api/comments/', include('Comments.api.urls',namespace="comments-api")),
]

handler400 = error
handler403 = error
handler404 = error
handler500 = error