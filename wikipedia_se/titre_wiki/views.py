
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.exceptions import MethodNotAllowed
from .serializers import TitreSerializer
from .Titre_ES_Script import search



@csrf_exempt
def search(request):
    """

    """
    if request.method == 'GET':
        print(request.GET.get('q','no'))
        query = request.GET.get('q', '')
        Es_Results = search(query)
        serializer = TitreSerializer(Es_Results, many=True)

        return JsonResponse(serializer.data, safe=False)

    raise MethodNotAllowed()

