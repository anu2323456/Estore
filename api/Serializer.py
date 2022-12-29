from rest_framework import serializers

from api.models import Reviews


class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    author=serializers.CharField()
    price=serializers.IntegerField()
    publisher=serializers.CharField()
    qty=serializers.IntegerField()

class ReviewModelSerializer(serializers.ModelSerializer):
    created_date=serializers.DateTimeField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"

