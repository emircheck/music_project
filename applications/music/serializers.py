from rest_framework import serializers

from applications.music.models import Category, Music


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title', 'year')


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(Category.objects.get(music=instance.id)).data
        representation.pop('id')
        return representation
