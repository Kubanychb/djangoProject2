from django.shortcuts import render
from rest_framework.response import Response
from movie_app.models import Director, Movie, Review
from rest_framework.decorators import api_view
from movie_app.serializers import DiroctorListSerializer, DiroctorDetailSerializer, MovieListSerializer, MovieDetailSerializer, ReviewListSerializer, ReviewDetailSerializer
from rest_framework import status


@api_view(['GET'])
def directirs_list(request):
    directors = Director.objects.all()
    serializer = DiroctorListSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail(request, id):
    try:
       director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'},
                        status=status.HTTP_404_NOT_FOUND
                        )
    data = DiroctorDetailSerializer(director).data
    return Response(data=data)


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detail(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = MovieDetailSerializer(movie).data
    return Response(data=data)



@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer  = ReviewListSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    data = ReviewDetailSerializer(review).data
    return Response(data=data)