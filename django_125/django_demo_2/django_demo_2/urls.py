"""django_demo_2 URL Configuration

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
from charts import views as charts_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',charts_views.index,name='index'),
    url(r'^demo_1/$',charts_views.demo_1,name='demo_1'),
    url(r'^charts_data/$',charts_views.charts_data,name='charts_data'),
    url(r'^charts_data_2/$',charts_views.charts_data_2,name='charts_data_2'),

]
