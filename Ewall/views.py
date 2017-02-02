from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework import generics

from Ewall.models import UserText
from Ewall.serializers import UserTextSerializer

from django.contrib.auth.models import User
from Ewall.serializers import UserSerializer

from Ewall.permissions import IsOwnerOrReadOnly

from rest_framework import permissions

from django.contrib.auth.decorators import login_required




def wallView(request):
    posts_list = UserText.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    context = {'posts_list': posts_list}
    return render(request, 'Wall.html', context)


class UserTextList(generics.ListCreateAPIView):
    queryset = UserText.objects.all()
    serializer_class = UserTextSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserTextDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserText.objects.all()
    serializer_class = UserTextSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
