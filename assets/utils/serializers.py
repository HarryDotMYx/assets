from django.core.serializers.json import DjangoJSONEncoder
import uuid

class UUIDEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return obj.hex
        return super().default(obj)

def serialize_uuid(uuid_obj):
    """Serialize a UUID object to a string."""
    return uuid_obj.hex if uuid_obj else None