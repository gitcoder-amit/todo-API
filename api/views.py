from django.shortcuts import render
from rest_framework.views import APIView
from api.models import Todo
from api.serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class TodoView(APIView):
    def get(self, request):
        todo_objs = Todo.objects.all()
        serializer = TodoSerializer(todo_objs, many=True)
        return Response({
            'data': serializer.data
        })

    def post(self, request):
        try:
            data = request.data
            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':status.HTTP_201_CREATED,
                    'message':'success data',
                    'data': serializer.data
                })
            return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message':'invalid data',
            'data': serializer.errors
            })
        except Exception as e:
            print(e)

        return Response({
            'status':False,
            'message':'Something went wrong'
        })


class TodoDetailView(APIView):
    def get_object(self, pk):
        try: 
            return Todo.objects.get(pk=pk)
        except:
            raise Http404
    
    def get(self, request, pk):
        instance = self.get_object(pk)
        breakpoint()
        serailizer = TodoSerializer(instance)
        return Response(data=serailizer.data)

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = TodoSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        
