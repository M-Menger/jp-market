from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .src.serializers import MarketSerializer 
from rest_framework import status
from .models import Market
from drf_yasg.utils import swagger_auto_schema


class MarketAPIView(APIView):

    @swagger_auto_schema(
            methods=["GET"],
            tags=['Products'],
    )
    def get(self, request, pk=None):
        if pk:
            market = Market.objects.get(pk=pk)
            serializer = MarketSerializer(market)
        else:
            market = Market.objects.all()
            serializer = MarketSerializer(market, many=True)
        return Response(serializer.data, status=status.HTTP_200_ok)
    

    @swagger_auto_schema(
        methods=["POST"],
        request_body = MarketSerializer,
        tags=['Markett'],
    )
    def post(self, request):
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        methods=["PUT"],
        request_body = MarketSerializer,
        tags=['AttProduct'],
    )
    def put(self, request, pk):
        market = Market.objects.get(pk=pk)
        serializer = MarketSerializer(market, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        methods=["DELETE"],
        request_body = MarketSerializer,
        tags=['DelProduct'],
    )
    def delete(self, request, pk):
        market = Market.objects.get(pk=pk)
        market.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # @api_view(['GET'])
    # def home(request):
    #     if request.method == 'GET':
    #         category = request.GET.get('category', None)
    #         if category:
    #             market = Market.objects.filter(category__icontains=category)
    #         else:
    #             market = Market.objects.all()

    #         serializer = MarketSerializer(market, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
        