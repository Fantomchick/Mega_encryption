from django.urls import path

from . import views
#добавил привязку к идексу
urlpatterns= [
    path('',views.index,name='index'),
    path('reg/',views.reg,name='reg'),
    path('logout/',views.logout_view,name='logout'),
    path('/cryptographer',views.cryptographer,name='cryptographer'), 
    path('/codebreaker',views.codebreaker,name='codebreaker'),       
]