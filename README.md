# rest_framework_ReadOnlyModelViewSet
How to build a Rest API using a ReadOnlyModelViewSet

The ReadOnlyModelViewSet inherits from GenericAPIView but it only provides the 'read-only'
actions - .list() and .retrieve()

You need to provide at least the queryset and serializer_class attributes

Serializers will take the data such as querysets and model instances and convert it
to a native python data type and then render as JSON or XML

The reverse process is known as deserialization

The model serializer class provides a useful shortcut for creating serializers
that deal with model instances and querysets.

**ModelSerializers**:
1. Automatically generate a set of fields that correspond to the fields of your model.
2. Automatically generate validators for the serializer
3. Includes simple implementations of .create() and .update().
4. We need to specify the model and the fields to include in a meta class
5. Alternatively you can use an exclude field to indicate fields in the model that you don’t want to be serialized.