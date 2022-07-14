from django import views
from .models import Article,Region
from .serializer import ArticleSerializer,RegionSerializer
from rest_framework import viewsets

class ArticleListView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class RegionListView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer