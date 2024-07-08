from django.shortcuts import render
from django.http import JsonResponse
from .models import CarList, ShowroomList, Review
from .api_file.serializers import CarSerializer, ShowroomSerializer, ReviewSerializer
from rest_framework .response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from .api_file.permissions import AdminOrReadOnlyPermission, ReviewUserOrReadOnlyPermission
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.authentication import JWTAuthentication


# from django.http import HttpResponse
# import json

#************************************BASIC FUNCTIONS TO RETURN JSON/JSON LIST RESPONSE*********************************
# def car_list_view(request):
#     cars = CarList.objects.all()
#     data = {
#         "cars":list(cars.values())
#     }
#     data_json = json.dumps(data)
#     # return JsonResponse(data)
#     return HttpResponse(data_json, content_type="application/json")

# def car_detail(request,car_id):
#     car = CarList.objects.get(pk= car_id)
#     data = {
#         "name":car.name,
#         "description":car.description,
#         "active":car.active,
#     }
#     return JsonResponse(data)


class Review_create(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        car = CarList.objects.get(pk=pk)
        useredit= self.request.user
        Review_queryset = Review.objects.filter(car=car, apiuser = useredit)
        if Review_queryset.exists():
            raise ValidationError('You have already reviewed this car')
        serializer.save(car=car) 

class Review_detail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReviewUserOrReadOnlyPermission]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

#**************************************MIXIN + GENERIC_APIVIEW***************************************
# class Review_detail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self,request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


class Reviewlist(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    #****************************************AUTH & PERMISSIONS*****************************************
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # permission_classes = [DjangoModelPermissions]

    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(car=pk)

   

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

#*****************************************MODEL VIEWSET********************************************
class Car_viewset(viewsets.ModelViewSet):
    queryset = CarList.objects.all()
    serializer_class = CarSerializer

#***************************************FUNCTION BASE VIEWS (USEING DECORATORS)***********************************
# @api_view(['GET','POST'])
# def car_list_view(request):
#     if request.method == 'GET':
#         cars = CarList.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = CarSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def car_detail(request,pk):
#     # get particular data
#     if request.method == 'GET':
#         try:
#             car = CarList.objects.get(pk=pk)
#         except:
#             return Response({"error":"car not found"},status=status.HTTP_404_NOT_FOUND)
#         serializer = CarSerializer(car)
#         return Response(serializer.data)
        
#     # update existing data
#     if request.method == 'PUT':
#         car = CarList.objects.get(pk= pk)
#         serializer = CarSerializer(car, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     # delete particular data
#     if request.method == 'DELETE':
#         car = CarList.objects.get(pk = pk)
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET'])
# def showroom_list_view(request):
#     if request.method == 'GET':
#         showrooms = ShowroomList.objects.all()
#         serializer = ShowroomSerializer(showrooms, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)


#****************************VIEW_SET*************************************
class Showroom_viewset(viewsets.ViewSet):
    def list(self, request):
        queryset = ShowroomList.objects.all()
        serializer = ShowroomSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ShowroomList.objects.all()
        showroom = get_object_or_404(queryset, pk=pk)
        serializer = ShowroomSerializer(showroom, context={'request': request})
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

    def update(self, request, pk=None):
        # showroom = ShowroomList.objects.get(pk= pk)
        queryset = ShowroomList.objects.all()
        showroom = get_object_or_404(queryset, pk=pk)
        serializer = ShowroomSerializer(showroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        # showroom = ShowroomList.objects.get(pk = pk)
        queryset = ShowroomList.objects.all()
        showroom = get_object_or_404(queryset, pk=pk)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







class Showroom_list_view(APIView):
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes= [IsAdminUser]

    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAdminUser]

    def get(self, request):
        showrooms = ShowroomList.objects.all()
        serializer = ShowroomSerializer(showrooms, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ShowroomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)

class Showroom_detail(APIView):
    def get(self, request,showroom_id):
        try:
            showroom = ShowroomList.objects.get(pk= showroom_id)
        except ShowroomList.DoesNotExist:
            return Response({"error":"Showroom not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ShowroomSerializer(showroom,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,showroom_id):
        showroom = ShowroomList.objects.get(pk= showroom_id)
        serializer = ShowroomSerializer(showroom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, showroom_id):
        showroom = ShowroomList.objects.get(pk = showroom_id)
        showroom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)