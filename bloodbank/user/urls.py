from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bloodstock$', views.bloodstock, name='bloodstock'),
    url(r'^bloodbank$', views.bloodbank, name='bloodbank'),
    url(r'^faq$', views.faq, name='faq'),
]