from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView

from .models import BotUser, BotAdmin
from .serializers import BotUserSerializer, BotAdminSerializer


class BotUserCreateView(CreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer


class BotUserRetrieveByFromId(RetrieveAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    lookup_field = 'from_id'


class BotUserRetrieveByPassportView(RetrieveAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    lookup_field = 'passport_number'


class BotUserRetrieveByPhoneNumber(RetrieveAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    lookup_field = 'phone_number'


class BotUserUpdateView(UpdateAPIView, RetrieveAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer


class BotAdminCreateView(CreateAPIView):
    queryset = BotAdmin.objects.all()
    serializer_class = BotAdminSerializer


class BotAdminRetrieveView(RetrieveAPIView):
    queryset = BotAdmin.objects.all()
    serializer_class = BotAdminSerializer
    lookup_field = 'from_id'


class BotAdminListView(ListAPIView):
    queryset = BotAdmin.objects.all()
    serializer_class = BotAdminSerializer
