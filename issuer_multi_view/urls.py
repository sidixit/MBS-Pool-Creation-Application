from django.conf.urls import url

from issuer_multi_view import views

urlpatterns = [
  url(r'^$', views.home, name='home'),
  url(r'^issuer_view/(?P<pk>\d+)$', views.issuer_view, name='issuer_view'),
  url(r'^issuer_new$', views.issuer_create, name='issuer_new'),
  url(r'^issuer_edit/(?P<pk>\d+)$', views.issuer_update, name='issuer_edit'),
  url(r'^issuer_delete/(?P<pk>\d+)$', views.issuer_delete, name='issuer_delete'),
  url(r'^issuer_login/$', views.issuer_login, name='issuer_login'),

  url(r'^pool_home$', views.pool_home, name='pool_home'),
  url(r'^pool_view/(?P<pk>\d+)$', views.pool_view, name='pool_view'),
  url(r'^pool_new$', views.pool_create, name='pool_new'),
  url(r'^pool_edit/(?P<pk>\d+)$', views.pool_update, name='pool_edit'),
  url(r'^pool_delete/(?P<pk>\d+)$', views.pool_delete, name='pool_delete'),

  url(r'^loan_new$', views.loan_create, name='loan_new'),
  url(r'^loan_home$', views.loan_home, name='loan_home'),
  url(r'^loan_edit/(?P<pk>\d+)$', views.loan_update, name='loan_edit'),
  url(r'^loan_delete/(?P<pk>\d+)$', views.loan_delete, name='loan_delete'),
  url(r'^loan_view/(?P<pk>\d+)$', views.loan_view, name='loan_view'),

  url(r'^admin_login/$', views.admin_login, name='admin_login'),
  url(r'^admin_home/$', views.admin_home, name='admin_home'),

]