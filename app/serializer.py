from dataclasses import fields
from rest_framework import serializers
from .models import Article,Region


class ArticleSerializer(serializers.ModelSerializer):
    # regions_name = serializers.CharField(source='regions.name', read_only=True)

    class Meta:
        model = Article
        # depth = 1
        # fields = ['title','content','regions_name'] 
        fields = '__all__'
        

class RegionSerializer(serializers.ModelSerializer):

    articles = ArticleSerializer(many=True,read_only = True)   
    class Meta:
        model = Region
        fields = ['id','name','articles']       