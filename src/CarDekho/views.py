from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def test_api(request):
    if request.method== 'GET':
        return Response({"success":True,"message":"Api working"}, status=status.HTTP_200_OK)