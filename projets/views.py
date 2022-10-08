from django.shortcuts import render
from .models import Projet


def index(request):
    projet=Projet.objects.all()
    return render(request,'index.html',{'projet':projet})


@api_view(['GET', 'POST', 'DELETE'])
def kandidaten_list(request):
    # GET Liste der Kandidaten, POST ein neuer Kandidat, DELETE alle Kandidaten
    if request.method == 'GET':
        kandidat = Kandidat.objects.all()

        Vorname = request.query_params.get('Vorname', None)
        if Vorname is not None:
            kandidat = kandidat.filter(title__icontains=Vorname)

        kandidat_serializer = KandidatSerializer(kandidat, many=True)
        return JsonResponse(kandidat_serializer.data, safe=False)
        # 'safe=False' für die Serialisierung von Objekten

    elif request.method == 'POST':
        kandidat_data = JSONParser().parse(request)
        kandidat_serializer = KandidatSerializer(data=kandidat_data)
        if kandidat_serializer.is_valid():
            kandidat_serializer.save()
            return JsonResponse(kandidat_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(kandidat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Kandidat.objects.all().delete()
        return JsonResponse({'Nachricht': '{} Kandidaten wurden erfolgreich gelöscht!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def kandidaten_detail(request, pk):
    # Kandidaten finden durch pk (id)
    try:
        kandidat = Kandidat.objects.get(pk=pk)
    except Kandidat.DoesNotExist:
        return JsonResponse({'Nachricht': 'Der Kandidat existiert nicht'}, status=status.HTTP_404_NOT_FOUND)

        # GET / PUT / DELETE Kandidat
    if request.method == 'GET':
        kandidat_serializer = KandidatSerializer(kandidat)
        return JsonResponse(kandidat_serializer.data)

    elif request.method == 'PUT':
        kandidat_data = JSONParser().parse(request)
        kandidat_serializer = KandidatSerializer(kandidat, data=kandidat_data)
        if kandidat_serializer.is_valid():
            kandidat_serializer.save()
            return JsonResponse(kandidat_serializer.data)
        return JsonResponse(kandidat_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        kandidat.delete()
        return JsonResponse({'Nachricht': 'Kandidat wurde erfolgreich gelöscht!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def kandidaten_list_erwachsene(request):

    # GET alle erwachsenen Kandidaten
    kandidat = Kandidat.objects.filter(ist_erwachsene=True)
    if request.method == 'GET':
        kandidat_serializer = KandidatSerializer(kandidat, many=True)
        return JsonResponse(kandidat_serializer.data, safe=False)