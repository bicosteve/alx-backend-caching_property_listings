from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache


from .models import Property
from .serializers import PropertySerializer
from .utils import get_all_properties


# Create your views here.
@api_view(["GET", "POST"])
@cache_page(60 * 5)
def property_list(request):
    if request.method == "GET":
        cached_res = get_all_properties()
        if cached_res:
            return Response({"data": cached_res}, safe=True)
        properties = Property.objects.all().values()
        serializer = PropertySerializer(properties, many=True)
        cache.set("all_properties")
        return Response({"data": list(serializer.data)}, safe=False)

    elif request.method == "POST":
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            qs = Property.objects.all()
            updated_serializer = PropertySerializer(qs, many=True)
            cache.set("all_properties", updated_serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
