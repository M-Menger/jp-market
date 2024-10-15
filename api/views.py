from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .src.serializers import (MarketSerializer, UserSerializer) 
from .models import Market
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
        methods=["POST"],
        request_body=UserSerializer,
        tags=["token"],
)

@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"username": serializer.data["username"]}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST0)

@swagger_auto_schema(
    methods=["GET"],  
    tags=['PRODUCTS'],
)
@api_view(['GET'])  
def get_market(request, pk=None): 
    if pk:
        market = Market.objects.get(pk=pk) 
        serializer = MarketSerializer(market) 
    else:
        market = Market.objects.all() 
        serializer = MarketSerializer(market, many=True) 
    return Response(serializer.data, status=status.HTTP_200_OK) 

@swagger_auto_schema(
    methods=["POST"],
    request_body=MarketSerializer,
    tags=['MARKET'],
)
@api_view(['POST'])  
def create_market(request):
    serializer = MarketSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)  
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@swagger_auto_schema(
    methods=["PUT"],
    request_body=MarketSerializer,
    tags=['UPDATEPRODUCT'],
)
@api_view(['PUT']) 
def update_market(request, pk):
    market = Market.objects.get(pk=pk)  
    serializer = MarketSerializer(market, data=request.data) 
    if serializer.is_valid():
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_200_OK) 
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@swagger_auto_schema(
    methods=["DELETE"],
    tags=['DELETEPRODUCT'],
)
@api_view(['DELETE'])  
def delete_market(request, pk):  
    market = Market.objects.get(pk=pk) 
    market.delete() 
    return Response(status=status.HTTP_204_NO_CONTENT)
