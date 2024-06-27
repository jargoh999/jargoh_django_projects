from django.urls import path
from . import views

urlpatterns = [
    path('accounts', views.ListAccount.as_view()),
    path('accounts/<str:pk>', views.account_detail),
    path('deposit', views.deposit),
    path('withdraw', views.withdraw),
]
