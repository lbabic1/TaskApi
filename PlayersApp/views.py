from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PlayersApp.models import Player
from PlayersApp.serializers import PlayerSerializer
# Create your views here.

@csrf_exempt
def PlayerApi(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            player = Player.objects.all()
            player_serializer = PlayerSerializer(player, many = True)
        else:
            player = Player.objects.get(PlayerId = id)
            player_serializer = PlayerSerializer(player)
        return JsonResponse(player_serializer.data, safe = False)
    elif request.method == 'POST':
        player_data = JSONParser().parse(request)
        player_serializer = PlayerSerializer(data = player_data)
        if player_serializer.is_valid(raise_exception=True):
            player_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)
    elif request.method == 'PUT':
        player_data = JSONParser().parse(request)
        player = Player.objects.get(PlayerId = player_data['PlayerId'])
        player_serializer = PlayerSerializer(player, data = player_data)
        if player_serializer.is_valid():
            player_serializer.save()
            return JsonResponse("Update Successfully", safe = False)
        return JsonResponse("Failed to Update", safe = False)
    elif request.method == 'DELETE':
        player = Player.objects.get(PlayerId = id)
        player.delete()
        return JsonResponse("Deleted Successfully", safe = False)
