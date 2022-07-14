from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import  ArticleListView,RegionListView



router = DefaultRouter()
router.register(r'ArticleListView',ArticleListView , basename='abc'),
router.register(r'RegionListView',RegionListView,basename = 'xyz')


urlpatterns =[
    
    # for token 
    # path('auth/', obtain_auth_token),

    # for login purposes
    path('auth/',include('rest_framework.urls')),   
]

urlpatterns += router.urls