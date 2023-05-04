from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Game
from .serializers.common import GameSerializer
from .serializers.populated import PopulatedGameSerializer

class GameListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )


    def get(self, _request):
        games = Game.objects.all()
        serialized_products = GameSerializer(games, many=True)
        return Response(serialized_products.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        request.data["owner"] = request.user.id
        game_to_add = GameSerializer(data=request.data)
        try:
            game_to_add.is_valid()
            game_to_add.save()
            return Response(game_to_add.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            res = {
                "detail": str(e)
            } 
            return Response(res, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except AssertionError as e:
            return Response({"detail":str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"detail": "Unprocessible Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class GameDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def get_game(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise NotFound(detail="Game not found")
    def get(self, request, pk):
            request.data["owner"] = request.user.id
            game = self.get_game(pk=pk)
            serialized_game = PopulatedGameSerializer(game)
            return Response(serialized_game.data, status=status.HTTP_200_OK)
    def post(self, request, pk):
        game_to_edit = self.get_album(pk=pk)
        updated_game = GameSerializer(game_to_edit, data=request.data)
        try:
            updated_game.is_valid()
            updated_game.save()
            return Response(updated_game.data, status=status.HTTP_202_ACCEPTED)
        except AssertionError as e:
            return Response({"detail": str(e)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"details": "Unprocessable Entity"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def delete(self, _request, pk):
        game_to_delete = self.get_game(pk=pk)
        game_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)