from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status 
from rest_framework.views import APIView
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
import pandas as pd
from rest_framework.decorators import action
from rest_framework import viewsets
# Create your views here.
fs = FileSystemStorage(location='tmp/')

class DataViewSet(viewsets.ModelViewSet):
    queryset = FileHandling.objects.all()
    serializer_class = FileHandlingSerializers

    @action(detail=False, methods=['POST'])
    def uploadfile(self, request):

        file = request.FILES['files']
        if file is not None:
            df = pd.read_csv(file)
            data_list = []

            for index,row in df.iterrows():
                (index,user_id,first_name,last_name,gender,email,phone,d_o_b,job_title) = row
                data_list.append(FileHandling(index=index,user_id=user_id,first_name=first_name,last_name=last_name,gender=gender,email=email,phone=phone,d_o_b=d_o_b,job_title=job_title))

            FileHandling.objects.bulk_create(data_list)

            return Response({'success':'True',
                    'failure':'False',
                    'msg': 'Record save successfully'},
                    status= status.HTTP_201_CREATED)               
        else:
             return Response({'success':'False',
                        'failure':'True',
                        'msg': 'File must be provided or please attach file'},
                        status= status.HTTP_400_BAD_REQUEST)
