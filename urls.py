from django.conf.urls import include, url
from .views import jarrbo_planner, jarrbo_planner_two, jarrbo_planner_three

urlpatterns = [
    url(r'^$', jarrbo_planner, name='jarrbo_planner'),
    url(r'^two/$', jarrbo_planner_two, name='jarrbo_planner_two'),
    url(r'^three/$', jarrbo_planner_three, name='jarrbo_planner_three'),
]
