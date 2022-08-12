from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import PpAgent

from .serializers import PpAgentSerializer, PpAgentModelSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework import generics, mixins

@csrf_exempt 
def list_pp_agents(request):
    if request.method == 'GET':
        list = PpAgent.objects.all()
        serializer = PpAgentModelSerializer(list, many=True)
        return JsonResponse(serializer.data, safe =False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PpAgentModelSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400) 

@csrf_exempt
def pp_Agent(request, id):
    try:
        pp_agent = PpAgent.objects.get(id=id)
    except PpAgent.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PpAgentModelSerializer(pp_agent)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PpAgentModelSerializer(pp_agent, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400) 

    elif request.method == 'DELETE':
        pp_agent.delete()
        return HttpResponse(status=204)

# api_view decorators in function based Api view 

@api_view(['GET', 'POST'])
def pp_agentapi_view(request):
    if request.method == 'GET':
        list = PpAgent.objects.all()
        serializer = PpAgentModelSerializer(list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PpAgentModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET', 'POST', 'DELETE'])
def api_view_pp_Agent(request, id):
    try:
        pp_agent = PpAgent.objects.get(id=id)
    except PpAgent.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PpAgentModelSerializer(pp_agent)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PpAgentModelSerializer(pp_agent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        pp_agent.delete()
        return Response(status=status.HTTP_205_RESET_CONTENT)

# class based API views

class ClassViewPpAgent(APIView):
    def get(self, request):
        agents = PpAgent.objects.all()
        serializer = PpAgentModelSerializer(agents, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PpAgentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ClassViewAgentDetails(APIView):
    def get_agent(self, id):
        try:
            return PpAgent.objects.get(id=id)
        except PpAgent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        agent = self.get_agent(id)
        serializer = PpAgentModelSerializer(agent)
        return Response(serializer.data)
    
    def put(self, request, id):
        agent = self.get_agent(id)
        serializer = PpAgentModelSerializer(agent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        agent = self.get_agent(id)
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# genericApiviews with mixins 

class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = PpAgentModelSerializer
    queryset = PpAgent.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)

    def post(self, request):
        return self.create(request)
    
    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)