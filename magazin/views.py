from django.shortcuts import render
from magazin.models import Product, Category,Order
from rest_framework import status
from .serializers import ProductSerializer,ProductCreateUpdateSerializer,CategorySerializer,OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .filters import ProductFilter, CategoryFilter
from rest_framework.generics import ListAPIView,ListCreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

class ProductListCreateAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class ProductDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        serializer = ProductCreateUpdateSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListCreateAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter


class CategoryDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=404)

        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=404)

        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=404)

        category.delete()
        return Response(status=204)

class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        order.delete()
        return Response(status=204)