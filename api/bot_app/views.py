from rest_framework.generics import CreateAPIView, RetrieveAPIView

from .models import BotUser
from .serializers import BotUserSerializer


class BotUserCreateView(CreateAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer


class BotUserRetrieveByPassportView(RetrieveAPIView):
    queryset = BotUser.objects.all()
    serializer_class = BotUserSerializer
    lookup_field = 'passport_number'
