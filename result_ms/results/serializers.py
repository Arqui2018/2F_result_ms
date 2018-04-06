from rest_framework import serializers
from django.utils import timezone
from .models import Result

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('id','user_id','amount','date','g_local','g_visit','winner','match_id','wallet_id')
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    amount = serializers.IntegerField()
    date = serializers.DateTimeField(default=timezone.now)
    g_local = serializers.IntegerField()
    g_visit = serializers.IntegerField()
    winner = serializers.BooleanField(default=False)
    match_id = serializers.IntegerField()
    wallet_id = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Result` instance, given the validated data.
        """
        return Result.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Result` instance, given the validated data.
        """
        instance.id = validated_data.get('id', instance.id)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.date = validated_data.get('date', instance.date)
        instance.g_local = validated_data.get('g_local', instance.g_local)
        instance.g_visit = validated_data.get('g_visit', instance.g_visit)
        instance.winner = validated_data.get('winner', instance.winner)
        instance.match_id = validated_data.get('match_id', instance.match_id)
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
rs = Result(user_id=1, amount=50000, g_local=0, g_visit=3, match_id=123, wallet_id=1010)
rs.save()

rs = Result(user_id=2, amount=3400, g_local=2, g_visit=1, match_id=13, wallet_id=2020)
rs.save()

rs = Result(user_id=1, amount=15000, g_local=1, g_visit=1, match_id=34, wallet_id=1010)
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
