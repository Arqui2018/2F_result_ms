from django.conf.urls import url
from results import views
#from rest_framework_swagger.views import get_swagger_view

#schema_view = get_swagger_view(title='Result')

urlpatterns = [
    #url(r'^$', schema_view),
    url(r'^results/$', views.result_list),
    url(r'^results/(?P<id>[0-9]+)/$', views.result_detail),
]
