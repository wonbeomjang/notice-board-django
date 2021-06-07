from django.urls import path    

from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.AccountList.as_view({'get': 'list'})),
    path('<int:id>', views.AccountList.as_view({'get': 'retrieve'})),
    path('login', views.Login.as_view({'post': 'retrieve'})),
    path('register', views.Register.as_view({'post': 'create'})),
]
