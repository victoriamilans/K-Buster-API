from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .serializers import UserSerializer
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAuthenticatedandEmployeePermission
from movies.permissions import IsAuthenticatedPermission


class UsersView(APIView):

    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedPermission, IsAuthenticatedandEmployeePermission]

    def patch(self, request: Request, user_id):
        user = get_object_or_404(User, id=user_id)

        self.check_object_permissions(request, user)

        serializer = UserSerializer(user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

    def get(self, request: Request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)

        return Response(serializer.data)
