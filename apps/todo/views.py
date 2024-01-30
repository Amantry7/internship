from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import TaskSerializer
from .models import Task
# Create your views here.
class TaskAPIViws(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer