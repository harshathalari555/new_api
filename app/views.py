from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

# Create your views here.
class MovieList(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

@api_view(["POST",])
def register_view(request):

    if request.method =="POST":
        serializer = AccountSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            data['response']= "sussessfully registerd new account"
            data['username']= account.username
            data['password'] = account.password
            data['email'] = account.email
            token = Token.objects.get_or_create(user=account).key
            print(token)
            data['token'] = token

        else:

            serializer.errors

        return Response(data)


