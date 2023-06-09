from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

'''@api_view()
def hello_world(request):
    print('home page run')
    return Response({'this is ' :'hello world'})
'''

'''@api_view(['GET])
def hello_world(request):
    print('home page run')
    return Response({'this is ' :'hello world'})
'''

'''@api_view(['POST'])
def hello_world(request):
    if request.method == 'POST':
        print(request.data)
        return Response({'this is ' :'hello world'})
'''

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg' :'this is get method'})

    if request.method == 'POST':
        print(request.data)
        return Response({'msg' :'this is post method','data':request.data})
