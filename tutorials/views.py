
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from tutorials.models import Product
from tutorials.models import Shopcart
from tutorials.serializers import TutorialSerializer
from tutorials.serializers import ShopcartSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Product.objects.all()                 
        name = request.GET.get('name', None)       
        if name is not None:
            tutorials = tutorials.filter(name__icontains=name)
                  
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    tutorial = Product.objects.get(pk=pk)
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(tutorial) 
        return JsonResponse(tutorial_serializer.data) 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    # GET / PUT / DELETE tutorial
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    # GET all published tutorials
    tutorials = Product.objects.filter(name="True")
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)

# Create your views here.
@api_view(['GET'])
def tutorial_add_shopcart(request,pk):
    # GET all published tutorials
    
    if request.method == 'GET': 
        tutorial = Product.objects.get(pk=pk)
        tutorial.amount=tutorial.amount-1
        if tutorial.amount<0:
            return JsonResponse({'message': 'This product is out of stock !'}, status=status.HTTP_404_NOT_FOUND) 
            
        tutorial.save()     
        try:
                shopcart = Shopcart.objects.get(productId=pk)
        except Shopcart.DoesNotExist:
                shopcart = None
        if shopcart !=None:
           shopcart.quantity=shopcart.quantity+1
           shopcart.save()
           tutorials_serializer = ShopcartSerializer(shopcart)
           return JsonResponse(tutorials_serializer.data, safe=False)
        elif shopcart ==None:
           newshopcart=Shopcart(quantity=1,productId=pk)          
           newshopcart.save()
           tutorials_serializer = ShopcartSerializer(newshopcart)
           return JsonResponse(tutorials_serializer.data, safe=False)
