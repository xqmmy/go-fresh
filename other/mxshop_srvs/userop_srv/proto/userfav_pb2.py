# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: userfav.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='userfav.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z\007.;proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ruserfav.proto\x1a\x1bgoogle/protobuf/empty.proto\"1\n\x0eUserFavRequest\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x0f\n\x07goodsId\x18\x02 \x01(\x05\"2\n\x0fUserFavResponse\x12\x0e\n\x06userId\x18\x01 \x01(\x05\x12\x0f\n\x07goodsId\x18\x02 \x01(\x05\"D\n\x13UserFavListResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x1e\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x10.UserFavResponse2\xec\x01\n\x07UserFav\x12\x33\n\nGetFavList\x12\x0f.UserFavRequest\x1a\x14.UserFavListResponse\x12\x35\n\nAddUserFav\x12\x0f.UserFavRequest\x1a\x16.google.protobuf.Empty\x12\x38\n\rDeleteUserFav\x12\x0f.UserFavRequest\x1a\x16.google.protobuf.Empty\x12;\n\x10GetUserFavDetail\x12\x0f.UserFavRequest\x1a\x16.google.protobuf.EmptyB\tZ\x07.;protob\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,])




_USERFAVREQUEST = _descriptor.Descriptor(
  name='UserFavRequest',
  full_name='UserFavRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='UserFavRequest.userId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='goodsId', full_name='UserFavRequest.goodsId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=95,
)


_USERFAVRESPONSE = _descriptor.Descriptor(
  name='UserFavResponse',
  full_name='UserFavResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userId', full_name='UserFavResponse.userId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='goodsId', full_name='UserFavResponse.goodsId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=147,
)


_USERFAVLISTRESPONSE = _descriptor.Descriptor(
  name='UserFavListResponse',
  full_name='UserFavListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='UserFavListResponse.total', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='UserFavListResponse.data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=217,
)

_USERFAVLISTRESPONSE.fields_by_name['data'].message_type = _USERFAVRESPONSE
DESCRIPTOR.message_types_by_name['UserFavRequest'] = _USERFAVREQUEST
DESCRIPTOR.message_types_by_name['UserFavResponse'] = _USERFAVRESPONSE
DESCRIPTOR.message_types_by_name['UserFavListResponse'] = _USERFAVLISTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserFavRequest = _reflection.GeneratedProtocolMessageType('UserFavRequest', (_message.Message,), {
  'DESCRIPTOR' : _USERFAVREQUEST,
  '__module__' : 'userfav_pb2'
  # @@protoc_insertion_point(class_scope:UserFavRequest)
  })
_sym_db.RegisterMessage(UserFavRequest)

UserFavResponse = _reflection.GeneratedProtocolMessageType('UserFavResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERFAVRESPONSE,
  '__module__' : 'userfav_pb2'
  # @@protoc_insertion_point(class_scope:UserFavResponse)
  })
_sym_db.RegisterMessage(UserFavResponse)

UserFavListResponse = _reflection.GeneratedProtocolMessageType('UserFavListResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERFAVLISTRESPONSE,
  '__module__' : 'userfav_pb2'
  # @@protoc_insertion_point(class_scope:UserFavListResponse)
  })
_sym_db.RegisterMessage(UserFavListResponse)


DESCRIPTOR._options = None

_USERFAV = _descriptor.ServiceDescriptor(
  name='UserFav',
  full_name='UserFav',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=220,
  serialized_end=456,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFavList',
    full_name='UserFav.GetFavList',
    index=0,
    containing_service=None,
    input_type=_USERFAVREQUEST,
    output_type=_USERFAVLISTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddUserFav',
    full_name='UserFav.AddUserFav',
    index=1,
    containing_service=None,
    input_type=_USERFAVREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteUserFav',
    full_name='UserFav.DeleteUserFav',
    index=2,
    containing_service=None,
    input_type=_USERFAVREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserFavDetail',
    full_name='UserFav.GetUserFavDetail',
    index=3,
    containing_service=None,
    input_type=_USERFAVREQUEST,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERFAV)

DESCRIPTOR.services_by_name['UserFav'] = _USERFAV

# @@protoc_insertion_point(module_scope)
