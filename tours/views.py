from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tour, Category
from .serializers import TourSerializer, CategorySerializer


class TourListAPIView(APIView):
    def get(self, request):
        tours = Tour.objects.filter(is_active=True)
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)