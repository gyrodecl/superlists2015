from django.conf.urls import include, url
from lists import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^(?P<list_id>\d+)$', views.view_list, name="view_list"),
    #url(r'^(?P<list_id>\d+)/add_item$', views.add_item_to_list, name="add_item_to_list"),
    url(r'^new$', views.new_list, name='new_list')
]
