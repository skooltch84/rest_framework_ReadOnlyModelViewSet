# rest_framework_ReadOnlyModelViewSet
How to build a Rest API using a ReadOnlyModelViewSet

The ReadOnlyModelViewSet inherits from GenericAPIView but it only provides the 'read-only'
actions - .list() and .retrieve()

You need to provide at least the queryset and serializer_class attributes