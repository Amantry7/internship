from rest_framework.routers import DefaultRouter

from .views import TaskAPIViws

urlpatterns = [
    
]
router = DefaultRouter()

router.register('todo', TaskAPIViws, basename='api_task')
urlpatterns +=router.urls
