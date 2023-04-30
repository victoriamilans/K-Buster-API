from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import MovieSerializer, MovieOrderSerializer
from .models import Movie
from users.permissions import IsEmployeeOrReadOnly
from django.shortcuts import get_object_or_404
from .permissions import IsAuthenticatedPermission
from users.models import User
from rest_framework.pagination import PageNumberPagination


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def get(self, request: Request):
        movies = Movie.objects.get_queryset().order_by("id")
        result_page = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieDatailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]

    def delete(self, request: Request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        serializer = MovieSerializer(movie)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request: Request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)

        serializer = MovieSerializer(movie)

        return Response(serializer.data)


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedPermission]

    def post(self, request: Request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        self.check_object_permissions(request, movie)

        user = User.objects.get(username=request.user)

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(movie=movie, user=user)

        return Response(serializer.data, status.HTTP_201_CREATED)