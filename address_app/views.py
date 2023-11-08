from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Address
from .serializers.address import AddressSerializer


def address(x):
    content = "juste text"
    return HttpResponse(content)


@api_view(['GET'])
def getAddress(request: HttpRequest):

    # to get the list of fields from address.py
    inpList = AddressSerializer.Meta.fields
    address = Address.objects.all()
    serializer = AddressSerializer(address, many=True)
    # print(serializer.data)
    # return Response(serializer.data)
    return render(
        request,
        'address_app/html/insAddress.html',
        {
            "data": (serializer.data),
            "inpList": inpList[1:],  # from index 1 to end
            "FonctionName": "getAddress()"
        }
    )


@api_view(['POST'])
def insAddress(request: HttpRequest):
    inpList = AddressSerializer.Meta.fields

    serializer = AddressSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)

    # return Response(serializer.data)
    return render(
        request,
        'address_app/html/insAddress.html',
        {
            "data": serializer.data,
            "inpList": inpList[1:],  # from index 1 to end
            "FonctionName": "insAddress()"
        }
    )
