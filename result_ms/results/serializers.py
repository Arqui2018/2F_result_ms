from rest_framework import serializers
from .models import Result

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id','user_id','monto','fecha','gol_1','gol_2','winner','partido_id','wallet_id')
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    monto = serializers.IntegerField()
    fecha = serializers.DateTimeField()
    gol_1 = serializers.IntegerField()
    gol_2 = serializers.IntegerField()
    winner = serializers.BooleanField()
    partido_id = serializers.IntegerField()
    wallet_id = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Result` instance, given the validated data.
        """
        return Result.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.monto = validated_data.get('monto', instance.monto)
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.gol_1 = validated_data.get('gol_1', instance.gol_1)
        instance.gol_2 = validated_data.get('gol_2', instance.gol_2)
        instance.winner = validated_data.get('winner', instance.winner)
        instance.partido_id = validated_data.get('partido_id', instance.partido_id)
        instance.wallet_id = validated_data.get('wallet_id', instance.wallet_id)
        instance.save()
        return instance

'''

from results.models import Result
from results.serializers import ResultSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from datetime import datetime
rel_time = datetime.strptime('18-03-2018', '%d-%m-%Y').date()
rs = Result(user_id=1, monto=50000, gol_1=0, gol_2=3, partido_id=123, wallet_id=1010)
rs.save()

rs = Result(user_id=2, monto=3400, gol_1=2, gol_2=1, partido_id=13, wallet_id=2020)
rs.save()

rs = Result(user_id=1, monto=15000, gol_1=1, gol_2=1, partido_id=34, wallet_id=1010)
rs.save()

serializer = ResultSerializer(rs)
serializer.data

content = JSONRenderer().render(serializer.data)
content

from django.utils.six import BytesIO
stream = BytesIO(content)
data = JSONParser().parse(stream)
data

serializer = ResultSerializer(data=data)
serializer.is_valid()

serializer.validated_data

serializer = ResultSerializer(Result.objects.all(), many=True)
serializer.data

from results.serializers import ResultSerializer
serializer = ResultSerializer()
print(repr(serializer))

'''
