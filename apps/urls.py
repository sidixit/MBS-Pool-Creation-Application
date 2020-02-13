from django.conf.urls import include, url
from django.contrib import admin

import theme.views
import issuer_multi_view.urls

urlpatterns = [
    url(r'^$', theme.views.home, name='home'),
    url(r'^issuer_multi_view/', include(issuer_multi_view.urls, namespace='issuer_multi_view')),
    url(r'^admin/', include(admin.site.urls)),
]
