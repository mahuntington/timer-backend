from rest_framework import generics
from .serializers import SessionSerializer 
from .models import Session

class SessionList(generics.ListCreateAPIView):
    queryset = Session.objects.all() # tell django how to retrieve all objects from the DB
    serializer_class = SessionSerializer # tell django what serializer to use

class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
