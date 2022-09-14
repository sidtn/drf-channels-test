
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from api.views import index, ProductViewSet, change_product1_name

router = routers.SimpleRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", index),
    path("pr1", change_product1_name)
]

urlpatterns += router.urls
