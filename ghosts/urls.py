"""ghosts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers

from ghosts import models, views

admin.site.register(models.BoastsAndRoasts)

router = routers.DefaultRouter()
router.register(r'boastsandroasts', views.BoastsAndRoastsView)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls))
    # path('', views.index, name='homepage'),
    # path('boastandroastform/', views.BoastsAndRoastsFormView,
    #      name='boastandroastform'),
    # path('upvote/<int:id>', views.UpvoteAddView, name='upvote'),
    # path('downvote/<int:id>', views.DownvoteAddView, name='downvote'),
    # path('netvotes/', views.NetVotes, name='netvote'),
    # path('allboasts/', views.Boasts, name='allboasts'),
    # path('allroasts/', views.Roasts, name='allroasts'),
    # path('delete/<int:id>', views.DeletePost, name='delete')
]
