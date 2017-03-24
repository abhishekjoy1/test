from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import routers, serializers, viewsets
from notes.models import Note
from notes.serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class NoteViewSet(viewsets.ViewSet):
                
	queryset = Note.objects.all() 
	def list(self, request):
                if 'subject' in request.GET:
                	subject = request.GET['subject']
        		queryset = Note.objects.filter(subject=subject)
			serializer = NoteSerializer(queryset, many=True)
			return Response(serializer.data)

                queryset = Note.objects.all() 
		serializer = NoteSerializer(queryset, many=True)
		return Response(serializer.data) 

	def retrieve(self, request, pk=None):
		queryset = Note.objects.all() 
        	note = get_object_or_404(queryset, pk=pk)
        	serializer = NoteSerializer(note)
		return Response(serializer.data)

	@api_view(['POST',])
	def create(self, request):
	        pass

	@api_view(['PUT',])
	def update(self, request, pk=None):
        	pass


	@api_view(['DELETE',])
    	def destroy(self, request, pk=None):
		try:
    			user = Note.objects.get(pk=pk)
			note.delete()
  		except User.DoesNotExist:
    			return Response(status=status.HTTP_404_NOT_FOUND)

