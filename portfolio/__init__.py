@api_view(['GET', 'POST', 'DELETE'])
# GET list of app, POST a new app, DELETE all app
def app_list(request,pk):
    # find tutorial by pk (id)
    try:
        app = Message.objects.get(pk=pk)
    except app.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

        # GET / PUT / DELETE app

    @api_view(['GET'])
    def app_list_published(request):
# GET all published app


# Create and Save a new Message
@api_view(['GET', 'POST', 'DELETE'])
def app_list(request):
    ...

    elif request.method == 'POST':
        app_data = JSONParser().parse(request)
        app_serializer = MessageSerializer(data=app_data)
        if app_serializer.is_valid():
            app_serializer.save()
            return JsonResponse(app_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        app = Message.objects.all()

        Name = request.GET.get('Mane', None)
        if Name is not None:
            app = app.filter(title__icontains=Name)

        app_serializer = appSerializer, many=True)
        return JsonResponse(app_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    @api_view(['GET', 'PUT', 'DELETE'])
    def app_detail(request, pk):
        # ... tutorial = Tutorial.objects.get(pk=pk)

        if request.method == 'GET':
            tutorial_serializer = MessageSerializer(app)
            return JsonResponse(app_serializer.data)


#Update object
        @api_view(['GET', 'PUT', 'DELETE'])
        def app_Name(request, pk):
            # ... app = Message.objects.get(pk=pk)
            # ...

            elif request.method == 'PUT':
            tutorial_data = JSONParser().parse(request)
            app_serializer = MessageSerializer(app, data=app_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(tutorial_serializer.data)
            return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       # Delete object
    @api_view(['GET', 'PUT', 'DELETE'])
    def app_list(request, pk):
        # ... app = Message.objects.get(pk=pk)
        # ...

        elif request.method == 'DELETE':
        app.delete()
        return JsonResponse({'message': 'Message was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    # Delete all object


@api_view(['GET', 'POST', 'DELETE'])
def app_list(request):
    # ...

    elif request.method == 'DELETE':
    count = Message.objects.all().delete()
    return JsonResponse({'message': '{} Message were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)

    #Find all objects by condition


@api_view(['GET'])
def app_list_published(request):
    tutorials = Message.objects.filter(published=True)

    if request.method == 'GET':
        tutorials_serializer = MessageSerializer(tutorials, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)


    ##############
    path(r'^api/app$', views.app_Nane),
    path(r'^api/app$', views.app_Nane),
    path(r'^api/app/(?P<pk>[0-9]+)$', views.app_Nachricht),
    path(r'^api/app/published$', views.app_list_published)

    #######

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',




