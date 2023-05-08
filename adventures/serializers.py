from rest_framework import serializers
from .models import Adventure


class AdventureSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Adventure
        fields = [
            'id', 'owner', 'created_at', 'updated_at',
            'title', 'subheading', 'location', 'post_image',
            'family_friendly', 'all_weather', 'terrain_challenge',
            'cost', 'duration', 'description',
        ]