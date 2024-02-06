from rest_framework import serializers

from .models import Teammate


class TeammateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    lastname = serializers.CharField(max_length=255)
    key_id = serializers.IntegerField()

    def create(self, validated_data):
        return Teammate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.lastname = validated_data.get("lastname", instance.lastname)
        instance.key_id = validated_data.get("key_id", instance.key_id)
        instance.save()
        return instance



