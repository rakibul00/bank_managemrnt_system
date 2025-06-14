
from django.urls import path
from .import views
from .views import UserRegistrationView, UserLoginView, user_logout,UserBankAccountUpdateView
 
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' )
]