# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: large_message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b"\n\x13large_message.proto\x1a\x19google/protobuf/any.proto\"\xc5\x05\n\x0bSomeMessage\x12\x1f\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x11.SomeMessage.Data\x12\x1f\n\x04meta\x18\x02 \x01(\x0b\x32\x11.SomeMessage.Meta\x1a\x17\n\x08Previews\x12\x0b\n\x03url\x18\x01 \x01(\t\x1a\x96\x01\n\x07\x41rtwork\x12\r\n\x05width\x18\x01 \x01(\r\x12\x0e\n\x06height\x18\x02 \x01(\r\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0f\n\x07\x62gColor\x18\x04 \x01(\t\x12\x12\n\ntextColor1\x18\x05 \x01(\t\x12\x12\n\ntextColor2\x18\x06 \x01(\t\x12\x12\n\ntextColor3\x18\x07 \x01(\t\x12\x12\n\ntextColor4\x18\x08 \x01(\t\x1a\x8e\x02\n\nAttributes\x12'\n\x08previews\x18\x01 \x03(\x0b\x32\x15.SomeMessage.Previews\x12%\n\x07\x61rtwork\x18\x02 \x01(\x0b\x32\x14.SomeMessage.Artwork\x12\x12\n\nartistName\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x11\n\talbumName\x18\x05 \x01(\t\x12\x13\n\x0btrackNumber\x18\x06 \x01(\r\x12\x12\n\ngenreNames\x18\x07 \x03(\t\x12\x18\n\x10\x64urationInMillis\x18\x08 \x01(\r\x12\x13\n\x0breleaseDate\x18\t \x01(\t\x12\x0c\n\x04isrc\x18\n \x01(\t\x12\x15\n\rcontentRating\x18\x0b \x01(\t\x1a[\n\x04\x44\x61ta\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04href\x18\x03 \x01(\t\x12+\n\nattributes\x18\x04 \x01(\x0b\x32\x17.SomeMessage.Attributes\x1a'\n\x06Paging\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\r\x1a+\n\x04Meta\x12#\n\x06paging\x18\x01 \x01(\x0b\x32\x13.SomeMessage.Pagingb\x06proto3"
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "large_message_pb2", globals())
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _SOMEMESSAGE._serialized_start = 51
    _SOMEMESSAGE._serialized_end = 760
    _SOMEMESSAGE_PREVIEWS._serialized_start = 132
    _SOMEMESSAGE_PREVIEWS._serialized_end = 155
    _SOMEMESSAGE_ARTWORK._serialized_start = 158
    _SOMEMESSAGE_ARTWORK._serialized_end = 308
    _SOMEMESSAGE_ATTRIBUTES._serialized_start = 311
    _SOMEMESSAGE_ATTRIBUTES._serialized_end = 581
    _SOMEMESSAGE_DATA._serialized_start = 583
    _SOMEMESSAGE_DATA._serialized_end = 674
    _SOMEMESSAGE_PAGING._serialized_start = 676
    _SOMEMESSAGE_PAGING._serialized_end = 715
    _SOMEMESSAGE_META._serialized_start = 717
    _SOMEMESSAGE_META._serialized_end = 760
# @@protoc_insertion_point(module_scope)