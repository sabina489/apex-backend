from common.api.serializers import CreatorSerializer
from notes.models import Content, Note


class NoteSerializer(CreatorSerializer):
    class Meta:
        model = Note
        fields = CreatorSerializer.Meta.fields + ("title",)
        read_only_fields = CreatorSerializer.Meta.read_only_fields


class ContentSerializer(CreatorSerializer):
    note = NoteSerializer()

    class Meta:
        model = Content
        fields = CreatorSerializer.Meta.fields + (
            "name",
            "description",
            "type",
            "file",
            "note",
        )
        read_only_fields = CreatorSerializer.Meta.read_only_fields