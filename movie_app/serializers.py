from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DiroctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class DiroctorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'



class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title'.split()



class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie'.split()
