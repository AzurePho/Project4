from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Dev
from .serializers.common import DevSerializer


# Create your views here.

class DevListView(APIView):
    
    def get(self, _requesst):
        devs = Dev.objects.all()
        serialized_genres = DevSerializer(devs, many=True)
        return Response(serialized_genres.data, status=status.HTTP_200_OK)
    