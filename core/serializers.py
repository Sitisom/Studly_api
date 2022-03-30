from rest_framework import serializers

from core.models import User, Rating


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Rating
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    subscription = serializers.SerializerMethodField()

    @staticmethod
    def get_subscription(obj):
        from course.serializers import SubscriptionSerializer
        subscription = obj.subscriptions.filter(is_valid=True).first()

        if subscription:
            return SubscriptionSerializer(subscription).data
        else:
            return None

    class Meta:
        model = User
        fields = ('role', 'subscription', 'full_name', 'avatar')
