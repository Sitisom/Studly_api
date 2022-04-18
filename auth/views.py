
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from auth.serializers import RegisterSerializer
from core.models import User


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(True)
        user = self.perform_create(serializer)

        refresh = RefreshToken.for_user(user)

        attr = dict()
        attr['access'] = str(refresh.access_token)
        attr['refresh'] = str(refresh)

        headers = self.get_success_headers(serializer.data)
        return Response(attr, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
