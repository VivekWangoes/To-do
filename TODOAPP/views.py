from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .Serializers import *


# Design the ToDo Board function which helps to open the ToDo page.
def todoBoard(request):
    # Fetch the Model data from database
    addTaskData = AddTaskModel.objects.all()
    context = {'addTaskData': addTaskData}
    return render(request, 'ToDoBoard.html', context)


# Design the API for ToDo App using ModelViewSet in DRF.
class AddtaskViewSet(ModelViewSet):
    # Fetch the Serializer and Model.
    serializer_class = AddTaskSerializer
    queryset = AddTaskModel.objects.all()

