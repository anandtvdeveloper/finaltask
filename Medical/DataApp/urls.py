from django.urls import path
from . import views
app_name='DataApp'
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('<slug:c_slug>/',views.homepage,name='department_by_category'),
    path('demo',views.demo,name='demo'),
    path('display',views.display,name='display'),

]