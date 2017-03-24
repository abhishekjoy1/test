from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from notes.views import NoteViewSet

#router = DefaultRouter()
#router.register(r'notes/', NoteViewSet)

#urlpatterns = router.urls

urlpatterns = [url(r'^api/', include('notes.urls')),]


