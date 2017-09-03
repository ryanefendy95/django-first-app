from django.conf.urls import url
from first_app import views

app_name = 'first_appaa'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
