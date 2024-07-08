from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from user_app.api.serializers import RegisterSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken



# @api_view(['POST'])
# def logout_view(request):
#     if request.method == 'POST':
#         request.user.auth_token.delete()
#         return Response({"success":True},status=status.HTTP_200_OK)


class Logout_view(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            token = Token.objects.get(user = request.user)
            token.delete()
            return Response({"success":True, "message":"Logout successfuly"},status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"success":False, "message":"Invalid token or user not logged in."},status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegisterSerializer(data=request.data)
#         data={}
#         if serializer.is_valid():
#             account = serializer.save()
#             data['username'] = account.username
#             data['email'] = account.email

#             token = Token.objects.get(user = account)

#             data['token'] = token
#         else:
#             data = serializer.errors
#         return Response(data)

class RegistrationView(APIView):
    def post(self,request):
        data={}
        serializer = RegisterSerializer(data=request.data)
        refresh = RefreshToken.for_user(request.user)
        if serializer.is_valid():
            account = serializer.save()
            data['username'] = account.username
            data['email'] = account.email
            data['token'] = {'refresh':str(refresh),"access":str(refresh.access_token)}
            return Response(data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

