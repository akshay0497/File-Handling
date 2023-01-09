from rest_framework import serializers
from file.models import *

class FileHandlingSerializers(serializers.ModelSerializer):

    class Meta:
        model = FileHandling
        fields = ['index','user_id','first_name','last_name','gender','email','phone','d_o_b','job_title']
