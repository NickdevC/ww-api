from django.db import IntegrityError
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
    
    def create(self, validated_data):
        """Checks for duplicate favourites and raises error"""
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serialziers.ValidationError({
                'detail': 'possible duplicate'
            })


class FavouriteDetailSerializer(FavouriteSerializer):
    """Serializer for the Favourite model used in Detail view.
    Post is a read only field so that we dont have to set it on each update
    """
    favourite = serializers.ReadOnlyField(source='favourite.id')