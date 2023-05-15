from rest_framework import serializers
from save.models import Favourite


class FavouriteSerializer(serializers.ModelSerializer):
    """Serializer for the Favourite model"""
    owner = serialziers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favourite
        fields = [
            'id', 'owner', 'created_on', 'adventure_post',
        ]