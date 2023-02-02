from django.urls import path

from . import views


urlpatterns = [
    path('user/add', views.BotUserCreateView.as_view(), name='user-create'),
    path('user/fromid/<int:from_id>',
         views.BotUserRetrieveByFromId.as_view(), name='user-retrieve-by-from-id'),
    path('user/passport/<str:passport_number>',
         views.BotUserRetrieveByPassportView.as_view(), name='user-retrieve-by-passport-number'),
    path('user/<int:pk>', views.BotUserUpdateView.as_view(), name='user-update'),
    path('user/phone/<str:phone_number>',
         views.BotUserRetrieveByPhoneNumber.as_view(), name='user-retrieve-by-phone-number'),

    path('admin/add', views.BotAdminCreateView.as_view(), name='admin-create'),
    path('admin/<int:from_id>', views.BotAdminRetrieveView.as_view(), name='admin-retrieve-by-from-id'),
    path('admin/list', views.BotAdminListView.as_view())
]

