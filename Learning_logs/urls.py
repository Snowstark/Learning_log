"""定义Learning_logs的url模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Main page
    url(r'^$', views.index, name='index'),

    # Show all topics
    url(r'^topics/$', views.topics, name='topics'),

    # Special topic to show
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]