"""
This module does the serialization to (sqlite) DB operations.
"""
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Harvester

__author__ = "Jan Frömberg"
__copyright__ = "Copyright 2018, GeRDI Project"
__credits__ = ["Jan Frömberg"]
__license__ = "Apache 2.0"
__maintainer__ = "Jan Frömberg"
__email__ = "jan.froemberg@tu-dresden.de"


class HarvesterSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Harvester
        fields = ('id', 'name', 'owner', 'metadataPrefix', 'notes', 'enabled',
                  'url', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    harvester = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Harvester.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'harvester')
