from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^detail/(?P<id>\d+)', views.detail, name='detail'),
    # url(r'^update/(?P<id>\d+)/(?P<title>\w+)', views.update, name='update'),
    # url(r'^delete/(?P<id>\d+)', views.delete, name='delete'),
    url(r'^$', views.home, name='home'),
    url(r'^update/newspaper', views.storeNewsPaper, name='storeNewsPaper'),
    url(r'^category/(?P<category_id>[\d]+)', views.listNewPaperByCategory, name='listNewPaperByCategory'),
    url(r'^detail/(?P<slug>[\w-]+)', views.detailNewPaper, name='detailNewPaper'),
]