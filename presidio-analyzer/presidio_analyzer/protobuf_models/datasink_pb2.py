# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: datasink.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import template_pb2 as template__pb2
import anonymize_pb2 as anonymize__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x64\x61tasink.proto\x12\x05types\x1a\x0c\x63ommon.proto\x1a\x0etemplate.proto\x1a\x0f\x61nonymize.proto\"\x80\x01\n\x0f\x44\x61tasinkRequest\x12,\n\x0e\x61nalyzeResults\x18\x01 \x03(\x0b\x32\x14.types.AnalyzeResult\x12\x31\n\x0f\x61nonymizeResult\x18\x02 \x01(\x0b\x32\x18.types.AnonymizeResponse\x12\x0c\n\x04path\x18\x03 \x01(\t\"\x12\n\x10\x44\x61tasinkResponse\"\x13\n\x11\x43ompletionMessage*\x93\x01\n\x11\x44\x61tasinkTypesEnum\x12\t\n\x05mysql\x10\x00\x12\t\n\x05mssql\x10\x01\x12\x0c\n\x08postgres\x10\x02\x12\x0b\n\x07sqlite3\x10\x03\x12\n\n\x06oracle\x10\x04\x12\t\n\x05kafka\x10\x05\x12\x0c\n\x08\x65venthub\x10\x06\x12\x06\n\x02s3\x10\x07\x12\r\n\tazureblob\x10\x08\x12\x11\n\rgooglestorage\x10\t2\xcc\x01\n\x0f\x44\x61tasinkService\x12:\n\x05\x41pply\x12\x16.types.DatasinkRequest\x1a\x17.types.DatasinkResponse\"\x00\x12:\n\x04Init\x12\x17.types.DatasinkTemplate\x1a\x17.types.DatasinkResponse\"\x00\x12\x41\n\nCompletion\x12\x18.types.CompletionMessage\x1a\x17.types.DatasinkResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'datasink_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DATASINKTYPESENUM']._serialized_start=245
  _globals['_DATASINKTYPESENUM']._serialized_end=392
  _globals['_DATASINKREQUEST']._serialized_start=73
  _globals['_DATASINKREQUEST']._serialized_end=201
  _globals['_DATASINKRESPONSE']._serialized_start=203
  _globals['_DATASINKRESPONSE']._serialized_end=221
  _globals['_COMPLETIONMESSAGE']._serialized_start=223
  _globals['_COMPLETIONMESSAGE']._serialized_end=242
  _globals['_DATASINKSERVICE']._serialized_start=395
  _globals['_DATASINKSERVICE']._serialized_end=599
# @@protoc_insertion_point(module_scope)
