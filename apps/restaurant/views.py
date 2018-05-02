from rest_framework import generics, status
from rest_framework.views import APIView #esto es para hacerlo a mano
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import (
    Restaurant, Category, Product, Details,
)
from .serializer import (
    RestaurantSerializer, CategorySerializer, ProductSerializer, DetailSerializer,
)

#POST = Create, GET = list o retrieve (traen todos o un registro), Update = PUT y PATCH (para modificar cosas), Destroy = DELETE

class RestaurantCreateListView(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

"""
Esta es la forma de escribir la clase anterior a pie:
class RestaurantCreateListView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        restaurant = request.data
        serializer = RestaurantSerializer(data=restaurant)
        if serializer.is_valid(): #el is_valid checa si los datos del serializer son igual que los modelos
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201HTTP_201_CREATED) """
"""
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """


class RestaurantUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()

"""
Esta es la forma de hacerlo a pie:
class RestaurantUpdateView(APIView):
    def get(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Restponse(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk): #el metodo pt es igual sólo no ponemos partial=True
        restaurant = get_object_or_404(Restaurant, pk=pk)
        new_data = request.data
        serializer = RestaurantSerializer(resataurant, data=new_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        restaurant = get_object_or_404(Restaurant, pk=pk)
        restaurant.delete()
        return Restponse(status=status.HTTP_204_NO_CONTENT)  """

class CategorytCreateListView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class ProductCreateListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class DetailsCreateListView(generics.ListCreateAPIView):
    serializer_class = DetailSerializer
    queryset = Details.objects.all()

class DetailsUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DetailSerializer
    queryset = Details.objects.all()
