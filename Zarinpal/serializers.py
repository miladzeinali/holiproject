from rest_framework import serializers

class ResultSerializer(serializers.Serializer):
    Status = serializers.IntegerField()
    Authority = serializers.CharField(max_length=200)

class ResSerializer(serializers.Serializer):
    Status = serializers.IntegerField()
    RefID = serializers.IntegerField()