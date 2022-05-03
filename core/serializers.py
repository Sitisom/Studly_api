from rest_framework import serializers

from core.models import User, Rating


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.full_name

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'full_name')


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    subscription = serializers.SerializerMethodField()

    def get_subscription(self, obj):
        from course.serializers import SubscriptionSerializer

        return SubscriptionSerializer(
            obj.subscriptions.order_by('rate_plan__order').last()
        ).data

    class Meta:
        model = User
        fields = ('role', 'subscription', 'full_name', 'avatar')
