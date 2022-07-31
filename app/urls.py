from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token 
from rest_framework.routers import DefaultRouter
from .views import  ArticleListView,RegionListView



router = DefaultRouter()
router.register(r'ArticleListView',ArticleListView , basename='abc'),
router.register(r'RegionListView',RegionListView,basename = 'xyz')


urlpatterns =[
    
    # for token 
    path('authtoken/', obtain_auth_token),

    # for login button that show on browser window 
    path('auth/',include('rest_framework.urls')),   
]

urlpatterns += router.urls