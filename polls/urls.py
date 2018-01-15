from django.conf.urls import url
from . import views

# The tutorial project has just one app, polls.
# In real Django projects, there might be five, ten, twenty apps or more.
# For example, the polls app has a detail view,
# and so might an app on the same project that is for a blog.
# How does Django knows which app view to create for a url when using the {% url %} template tag?
#
# The answer is to add namespaces to your URLconf.
app_name = 'polls'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # the 'name' value as called by the {% url %} template tag
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]