from django.shortcuts import render

from rest_framework import routers, serializers, viewsets
from notes.models import Note
from notes.serializers import NoteSerializer
from rest_framework.response import Response

class NoteViewSet(viewsets.ViewSet):
                
	queryset = Note.objects.all() 
	def list(self, request):
                queryset = Note.objects.all() 
		serializer = NoteSerializer(queryset, many=True)
		return Response(serializer.data) 


	def retrieve(self, request, pk=None):
                subject = request.GET['subject']
        	queryset = User.objects.filter(subject=subject)

        	user = get_object_or_404(queryset, pk=pk)
        	serializer = UserSerializer(user)
        	return Response(serializer.data)

	def update(self, request, pk=None):
        	pass


    	def destroy(self, request, pk=None):
        	pass
	
