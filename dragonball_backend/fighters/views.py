import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FighterListView(APIView):
    def get(self, request):
        response = requests.get('https://dragonball-api.com/api/characters')
        if response.status_code == 200:
            data = response.json()[:10]  # Tomamos solo los primeros 10 peleadores
            fighters = [
                {
                    'name': fighter['name'],
                    'description': fighter.get('description', 'No description available'),
                    'image': fighter.get('image', 'No image available')
                }
                for fighter in data
            ]
            return Response(fighters, status=status.HTTP_200_OK)
        return Response({"error": "Failed to fetch data"}, status=status.HTTP_400_BAD_REQUEST)
