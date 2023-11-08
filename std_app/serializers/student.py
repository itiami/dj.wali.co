from rest_framework import serializers
from ..models import StudentModel


class StudentSerilizer(serializers.ModelSerializer):

    class Meta:
        model = StudentModel
        # fields = ('id','nom','prenom','phone','email','tarifRepas')
        # or
        fields = '__all__'
