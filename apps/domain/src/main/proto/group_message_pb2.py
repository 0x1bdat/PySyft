# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/group_message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from syft.proto.syft_assets import (
    common_object_pb2 as proto_dot_syft__assets_dot_common__object__pb2,
)
from syft.proto.syft_assets.io import (
    address_pb2 as proto_dot_syft__assets_dot_io_dot_address__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="proto/group_message.proto",
    package="syft.core.node.common.service",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x19proto/group_message.proto\x12\x1dsyft.core.node.common.service\x1a%proto/syft_assets/common_object.proto\x1a"proto/syft_assets/io/address.proto"\x8c\x01\n\x12\x43reateGroupMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"u\n\x13\x43reateGroupResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08"\x89\x01\n\x0fGetGroupMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"r\n\x10GetGroupResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08"\x8c\x01\n\x12GetAllGroupMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"u\n\x13GetAllGroupResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08"\x8c\x01\n\x12SearchGroupMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"u\n\x13SearchGroupResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08"\x8c\x01\n\x12UpdateGroupMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address"u\n\x13UpdateGroupResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07success\x18\x03 \x01(\x08\x62\x06proto3',
    dependencies=[
        proto_dot_syft__assets_dot_common__object__pb2.DESCRIPTOR,
        proto_dot_syft__assets_dot_io_dot_address__pb2.DESCRIPTOR,
    ],
)


_CREATEGROUPMESSAGE = _descriptor.Descriptor(
    name="CreateGroupMessage",
    full_name="syft.core.node.common.service.CreateGroupMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.CreateGroupMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.CreateGroupMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.core.node.common.service.CreateGroupMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=136,
    serialized_end=276,
)


_CREATEGROUPRESPONSE = _descriptor.Descriptor(
    name="CreateGroupResponse",
    full_name="syft.core.node.common.service.CreateGroupResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.CreateGroupResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.CreateGroupResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="syft.core.node.common.service.CreateGroupResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=278,
    serialized_end=395,
)


_GETGROUPMESSAGE = _descriptor.Descriptor(
    name="GetGroupMessage",
    full_name="syft.core.node.common.service.GetGroupMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.GetGroupMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.GetGroupMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.core.node.common.service.GetGroupMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=398,
    serialized_end=535,
)


_GETGROUPRESPONSE = _descriptor.Descriptor(
    name="GetGroupResponse",
    full_name="syft.core.node.common.service.GetGroupResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.GetGroupResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.GetGroupResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="syft.core.node.common.service.GetGroupResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=537,
    serialized_end=651,
)


_GETALLGROUPMESSAGE = _descriptor.Descriptor(
    name="GetAllGroupMessage",
    full_name="syft.core.node.common.service.GetAllGroupMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.GetAllGroupMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.GetAllGroupMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.core.node.common.service.GetAllGroupMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=654,
    serialized_end=794,
)


_GETALLGROUPRESPONSE = _descriptor.Descriptor(
    name="GetAllGroupResponse",
    full_name="syft.core.node.common.service.GetAllGroupResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.GetAllGroupResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.GetAllGroupResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="syft.core.node.common.service.GetAllGroupResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=796,
    serialized_end=913,
)


_SEARCHGROUPMESSAGE = _descriptor.Descriptor(
    name="SearchGroupMessage",
    full_name="syft.core.node.common.service.SearchGroupMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.SearchGroupMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.SearchGroupMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.core.node.common.service.SearchGroupMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=916,
    serialized_end=1056,
)


_SEARCHGROUPRESPONSE = _descriptor.Descriptor(
    name="SearchGroupResponse",
    full_name="syft.core.node.common.service.SearchGroupResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.SearchGroupResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.SearchGroupResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="syft.core.node.common.service.SearchGroupResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1058,
    serialized_end=1175,
)


_UPDATEGROUPMESSAGE = _descriptor.Descriptor(
    name="UpdateGroupMessage",
    full_name="syft.core.node.common.service.UpdateGroupMessage",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.UpdateGroupMessage.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.UpdateGroupMessage.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="reply_to",
            full_name="syft.core.node.common.service.UpdateGroupMessage.reply_to",
            index=2,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1178,
    serialized_end=1318,
)


_UPDATEGROUPRESPONSE = _descriptor.Descriptor(
    name="UpdateGroupResponse",
    full_name="syft.core.node.common.service.UpdateGroupResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="msg_id",
            full_name="syft.core.node.common.service.UpdateGroupResponse.msg_id",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="syft.core.node.common.service.UpdateGroupResponse.address",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="success",
            full_name="syft.core.node.common.service.UpdateGroupResponse.success",
            index=2,
            number=3,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1320,
    serialized_end=1437,
)

_CREATEGROUPMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_syft__assets_dot_common__object__pb2._UID
_CREATEGROUPMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_CREATEGROUPMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_CREATEGROUPRESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_syft__assets_dot_common__object__pb2._UID
_CREATEGROUPRESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_GETGROUPMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_syft__assets_dot_common__object__pb2._UID
_GETGROUPMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_GETGROUPMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_GETGROUPRESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_syft__assets_dot_common__object__pb2._UID
_GETGROUPRESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_GETALLGROUPMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_syft__assets_dot_common__object__pb2._UID
_GETALLGROUPMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_GETALLGROUPMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_GETALLGROUPRESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_syft__assets_dot_common__object__pb2._UID
_GETALLGROUPRESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_SEARCHGROUPMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_syft__assets_dot_common__object__pb2._UID
_SEARCHGROUPMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_SEARCHGROUPMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_SEARCHGROUPRESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_syft__assets_dot_common__object__pb2._UID
_SEARCHGROUPRESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_UPDATEGROUPMESSAGE.fields_by_name[
    "msg_id"
].message_type = proto_dot_syft__assets_dot_common__object__pb2._UID
_UPDATEGROUPMESSAGE.fields_by_name[
    "address"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_UPDATEGROUPMESSAGE.fields_by_name[
    "reply_to"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
_UPDATEGROUPRESPONSE.fields_by_name[
    "msg_id"
].message_type = proto_dot_syft__assets_dot_common__object__pb2._UID
_UPDATEGROUPRESPONSE.fields_by_name[
    "address"
].message_type = proto_dot_syft__assets_dot_io_dot_address__pb2._ADDRESS
DESCRIPTOR.message_types_by_name["CreateGroupMessage"] = _CREATEGROUPMESSAGE
DESCRIPTOR.message_types_by_name["CreateGroupResponse"] = _CREATEGROUPRESPONSE
DESCRIPTOR.message_types_by_name["GetGroupMessage"] = _GETGROUPMESSAGE
DESCRIPTOR.message_types_by_name["GetGroupResponse"] = _GETGROUPRESPONSE
DESCRIPTOR.message_types_by_name["GetAllGroupMessage"] = _GETALLGROUPMESSAGE
DESCRIPTOR.message_types_by_name["GetAllGroupResponse"] = _GETALLGROUPRESPONSE
DESCRIPTOR.message_types_by_name["SearchGroupMessage"] = _SEARCHGROUPMESSAGE
DESCRIPTOR.message_types_by_name["SearchGroupResponse"] = _SEARCHGROUPRESPONSE
DESCRIPTOR.message_types_by_name["UpdateGroupMessage"] = _UPDATEGROUPMESSAGE
DESCRIPTOR.message_types_by_name["UpdateGroupResponse"] = _UPDATEGROUPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateGroupMessage = _reflection.GeneratedProtocolMessageType(
    "CreateGroupMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEGROUPMESSAGE,
        "__module__": "proto.group_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.CreateGroupMessage)
    },
)
_sym_db.RegisterMessage(CreateGroupMessage)

CreateGroupResponse = _reflection.GeneratedProtocolMessageType(
    "CreateGroupResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEGROUPRESPONSE,
        "__module__": "proto.group_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.CreateGroupResponse)
    },
)
_sym_db.RegisterMessage(CreateGroupResponse)

GetGroupMessage = _reflection.GeneratedProtocolMessageType(
    "GetGroupMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETGROUPMESSAGE,
        "__module__": "proto.group_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.GetGroupMessage)
    },
)
_sym_db.RegisterMessage(GetGroupMessage)

GetGroupResponse = _reflection.GeneratedProtocolMessageType(
    "GetGroupResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETGROUPRESPONSE,
        "__module__": "proto.group_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.GetGroupResponse)
    },
)
_sym_db.RegisterMessage(GetGroupResponse)

GetAllGroupMessage = _reflection.GeneratedProtocolMessageType(
    "GetAllGroupMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETALLGROUPMESSAGE,
        "__module__": "proto.group_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.GetAllGroupMessage)
    },
)
_sym_db.RegisterMessage(GetAllGroupMessage)

GetAllGroupResponse = _reflection.GeneratedProtocolMessageType(
    "GetAllGroupResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETALLGROUPRESPONSE,
        "__module__": "proto.group_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.GetAllGroupResponse)
    },
)
_sym_db.RegisterMessage(GetAllGroupResponse)

SearchGroupMessage = _reflection.GeneratedProtocolMessageType(
    "SearchGroupMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHGROUPMESSAGE,
        "__module__": "proto.group_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.SearchGroupMessage)
    },
)
_sym_db.RegisterMessage(SearchGroupMessage)

SearchGroupResponse = _reflection.GeneratedProtocolMessageType(
    "SearchGroupResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHGROUPRESPONSE,
        "__module__": "proto.group_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.SearchGroupResponse)
    },
)
_sym_db.RegisterMessage(SearchGroupResponse)

UpdateGroupMessage = _reflection.GeneratedProtocolMessageType(
    "UpdateGroupMessage",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEGROUPMESSAGE,
        "__module__": "proto.group_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.UpdateGroupMessage)
    },
)
_sym_db.RegisterMessage(UpdateGroupMessage)

UpdateGroupResponse = _reflection.GeneratedProtocolMessageType(
    "UpdateGroupResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _UPDATEGROUPRESPONSE,
        "__module__": "proto.group_message_pb2"
        # @@protoc_insertion_point(class_scope:syft.core.node.common.service.UpdateGroupResponse)
    },
)
_sym_db.RegisterMessage(UpdateGroupResponse)


# @@protoc_insertion_point(module_scope)
