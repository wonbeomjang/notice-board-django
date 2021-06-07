from django.urls import path    

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.PostViewset.as_view({'get': 'list', 'post': 'create',})),
    path('<int:id>', views.PostElementViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
