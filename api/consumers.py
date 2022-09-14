from djangochannelsrestframework.observer.generics import ObserverModelInstanceMixin

from .models import Product
from .serializers import ProductSerializer
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer


class ProductConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
