from rest_framework import serializers
from app.models import *


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class AccountSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

