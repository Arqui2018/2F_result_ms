from django.conf.urls import url
from results import views

urlpatterns = [
    #url(r'^$', schema_view),
    url(r'^results/$', views.result_list),
    url(r'^results/(?P<id>[0-9]+)/$', views.result_detail),
    url(r'^results/users/(?P<user_id>[0-9]+)/$', views.result_user),
    url(r'^results/matches/(?P<match_id>[0-9]+)/$', views.result_match),
]
