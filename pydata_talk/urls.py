
from django.conf.urls import url
from django.contrib import admin

from talk_app.views import IndexView, PrepareView, StateView, FederalView, ResourceView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^prepare/$', PrepareView.as_view(), name='prepare_view'),
    url(r'^state/$', StateView.as_view(), name='state_view'),
    url(r'^federal/$', FederalView.as_view(), name='federal_view'),
    url(r'^resources/$', ResourceView.as_view(), name='resource_view'),

]
