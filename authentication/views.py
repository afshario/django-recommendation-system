from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import SignUpSerializer
from rest_framework_simplejwt import tokens
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()

class SignUpView(APIView):
      serializer_class = SignUpSerializer
      permission_classes = [AllowAny]
      def post(self, request):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                  serializer.save()
                  user = User.objects.get(email=serializer.validated_data['email'])
                  token = tokens.RefreshToken.for_user(user)
                  send_mail(
                        'Welcome to our system',
                        f'Please activate your account by clicking the following link: '
                        f'{settings.SITE_DOMAIN}/api/v1/auth/activate/{str(token.access_token)}',
                        settings.DEFAULT_FROM_EMAIL,
                        [str(user.email)],
                        fail_silently=False,
                  )

                  return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    