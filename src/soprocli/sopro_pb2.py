# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sopro.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bsopro.proto\x12\x05sopro\"\x0f\n\rHealthRequest\"!\n\x0eHealthResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2I\n\x0cSoproService\x12\x39\n\x08PingPong\x12\x14.sopro.HealthRequest\x1a\x15.sopro.HealthResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sopro_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HEALTHREQUEST._serialized_start=22
  _HEALTHREQUEST._serialized_end=37
  _HEALTHRESPONSE._serialized_start=39
  _HEALTHRESPONSE._serialized_end=72
  _SOPROSERVICE._serialized_start=74
  _SOPROSERVICE._serialized_end=147
# @@protoc_insertion_point(module_scope)