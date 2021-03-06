# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from results.models import Result
from results.serializers import ResultSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def result_list(request):
    """
    List all code results, or create a new result.
    """
    if request.method == 'GET':
        results = Result.objects.all()
        serializer = ResultSerializer(results, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ResultSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def result_detail(request, id):
    """
    Retrieve, update or delete a result.
    """
    try:
        result = Result.objects.get(id=id)
    except Result.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ResultSerializer(result)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ResultSerializer(result, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        serializer = ResultSerializer(result)
        result.delete()
        return JSONResponse(serializer.data, status=204)

@csrf_exempt
def result_user(request, user_id):
    """
    List all code results by user_id
    """
    try:
        result = Result.objects.filter(user_id=user_id)
    except Result.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ResultSerializer(result, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def result_match(request, match_id):
    """
    List all code results by match_id
    """
    try:
        result = Result.objects.filter(match_id=match_id)
    except Result.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ResultSerializer(result, many=True)
        return JSONResponse(serializer.data)
