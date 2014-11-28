# -*- coding: utf8 -*-
#从django.conf.urls.defaults导入所有对象，其中包括了一个叫做patterns的函数
from django.conf.urls import patterns,url 
from polls import views

#URLConf:url就像一座桥梁，通过这个桥梁我们才找到视图中对应的代码，渲染的模板
urlpatterns = patterns('',
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(),name='detail'),
    url(r'^(?P<pk>\d+)/result/$',views.ResultsView.as_view(),name='results'),
    url(r'^(?P<question_id>\d+)/vote/$',views.vote,name='vote'),
    #url( r'^grappelli/', include( 'grappelli.urls' ) ),
)
'''
patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^specifics/(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),'''
