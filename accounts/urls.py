from django.urls import path    
from rest_framework_jwt.views import verify_jwt_token
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.AccountList.as_view({'get': 'list'})),
    path('<int:id>', views.AccountList.as_view({'get': 'retrieve'})),
    path('login', views.Login.as_view({'post': 'create'})),
    path('register', views.Register.as_view({'post': 'create'})),
    path('withdrawal', views.Withdrawal.as_view({'post': 'destroy'})),
]
