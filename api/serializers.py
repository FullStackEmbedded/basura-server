from rest_framework import serializers

from .models import TrashCan, TrashState


class TrashCanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrashCan
        fields = ('id',)

class TrashStateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrashState
        fields = ('trash_can', 'timestamp', 'fill_state')