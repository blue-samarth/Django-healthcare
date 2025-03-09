# healthcare_project/accounts/views.py

from rest_framework import status, generics, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import UserSerializer
# Create your views here.

user = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
            }, status=status.HTTP_201_CREATED
        )
