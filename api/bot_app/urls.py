from django.urls import path

from . import views


urlpatterns = [
    path('user/add', views.BotUserCreateView.as_view(), name='user-create'),
    path('user/passport/<str:passport_number>',
         views.BotUserRetrieveByPassportView.as_view(), name='user-retrieve-by-passport-number'),
]
