from django.db import models

# from src.articles.models import Article
# from src.articles.serializer import ArticleSerializer


# class ArticleManager(models.Manager):
#     def by_regions(self, regions, region_separator=","):
#         """
#         Restricts the returned articles to given regions
#         """
#         if regions:
#             qs = self.prefetch_related("regions")
#             for region in regions.split(region_separator):
#                 qs = qs.filter(regions__code=region)

#             return qs

#         return {'you have to add region for the result'}


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    regions = models.ForeignKey("Region", related_name="articles", blank=True,on_delete=models.CASCADE) 

    def __str__(self):
        return self.title

    # @property
    # def regions_name(self):
    #     return self.regions.name    

class Region(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_token(sender,instance=None,created= False,**kwargs):
    if created:
        Token.objects.create(user = instance)
        

    