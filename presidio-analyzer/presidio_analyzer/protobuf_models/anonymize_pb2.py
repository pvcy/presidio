# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anonymize.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import template_pb2 as template__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61nonymize.proto\x12\x05types\x1a\x0c\x63ommon.proto\x1a\x0etemplate.proto\"\xc1\x01\n\x13\x41nonymizeApiRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x19\n\x11\x61nalyzeTemplateId\x18\x02 \x01(\t\x12\x1b\n\x13\x61nonymizeTemplateId\x18\x03 \x01(\t\x12/\n\x0f\x61nalyzeTemplate\x18\x04 \x01(\x0b\x32\x16.types.AnalyzeTemplate\x12\x33\n\x11\x61nonymizeTemplate\x18\x05 \x01(\x0b\x32\x18.types.AnonymizeTemplate\"z\n\x10\x41nonymizeRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\x12*\n\x08template\x18\x02 \x01(\x0b\x32\x18.types.AnonymizeTemplate\x12,\n\x0e\x61nalyzeResults\x18\x03 \x03(\x0b\x32\x14.types.AnalyzeResult\"!\n\x11\x41nonymizeResponse\x12\x0c\n\x04text\x18\x01 \x01(\t2P\n\x10\x41nonymizeService\x12<\n\x05\x41pply\x12\x17.types.AnonymizeRequest\x1a\x18.types.AnonymizeResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'anonymize_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ANONYMIZEAPIREQUEST']._serialized_start=57
  _globals['_ANONYMIZEAPIREQUEST']._serialized_end=250
  _globals['_ANONYMIZEREQUEST']._serialized_start=252
  _globals['_ANONYMIZEREQUEST']._serialized_end=374
  _globals['_ANONYMIZERESPONSE']._serialized_start=376
  _globals['_ANONYMIZERESPONSE']._serialized_end=409
  _globals['_ANONYMIZESERVICE']._serialized_start=411
  _globals['_ANONYMIZESERVICE']._serialized_end=491
# @@protoc_insertion_point(module_scope)
