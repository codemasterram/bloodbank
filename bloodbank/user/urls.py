from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bloodstock$', views.bloodstock, name='bloodstock'),
    url(r'^bloodbank$', views.bloodbank, name='bloodbank'),
    url(r'^faq$', views.faq, name='faq'),
    url(r'^login$', views.login, name='login'),
    url(r'^entry$', views.entry, name='entry'),
    url(r'^donors$', views.donors, name='donors'),
    url(r'^register$', views.register, name='register'),
    url(r'^events$', views.events, name='events'),
    # url(r'^donorlist$', views.donorlist, name='donorlist'),

    
]