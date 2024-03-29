# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scheduler.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import stream_pb2 as stream__pb2
import scan_pb2 as scan__pb2
import template_pb2 as template__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fscheduler.proto\x12\x05types\x1a\x0cstream.proto\x1a\nscan.proto\x1a\x0etemplate.proto\"y\n\x18ScannerCronJobApiRequest\x12 \n\x18ScannerCronJobTemplateId\x18\x01 \x01(\t\x12;\n\x15scannerCronJobRequest\x18\x02 \x01(\x0b\x32\x1c.types.ScannerCronJobRequest\"o\n\x15ScannerCronJobRequest\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\x1f\n\x07trigger\x18\x02 \x01(\x0b\x32\x0e.types.Trigger\x12\'\n\x0bscanRequest\x18\x03 \x01(\x0b\x32\x12.types.ScanRequest\"\x18\n\x16ScannerCronJobResponse\"i\n\x14StreamsJobApiRequest\x12\x1c\n\x14StreamsJobTemplateId\x18\x01 \x01(\t\x12\x33\n\x11streamsJobRequest\x18\x02 \x01(\x0b\x32\x18.types.StreamsJobRequest\"O\n\x11StreamsJobRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x0estreamsRequest\x18\x02 \x01(\x0b\x32\x14.types.StreamRequest\"\x14\n\x12StreamsJobResponse2\xa4\x01\n\x10SchedulerService\x12\x44\n\x0b\x41pplyStream\x12\x18.types.StreamsJobRequest\x1a\x19.types.StreamsJobResponse\"\x00\x12J\n\tApplyScan\x12\x1c.types.ScannerCronJobRequest\x1a\x1d.types.ScannerCronJobResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'scheduler_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SCANNERCRONJOBAPIREQUEST']._serialized_start=68
  _globals['_SCANNERCRONJOBAPIREQUEST']._serialized_end=189
  _globals['_SCANNERCRONJOBREQUEST']._serialized_start=191
  _globals['_SCANNERCRONJOBREQUEST']._serialized_end=302
  _globals['_SCANNERCRONJOBRESPONSE']._serialized_start=304
  _globals['_SCANNERCRONJOBRESPONSE']._serialized_end=328
  _globals['_STREAMSJOBAPIREQUEST']._serialized_start=330
  _globals['_STREAMSJOBAPIREQUEST']._serialized_end=435
  _globals['_STREAMSJOBREQUEST']._serialized_start=437
  _globals['_STREAMSJOBREQUEST']._serialized_end=516
  _globals['_STREAMSJOBRESPONSE']._serialized_start=518
  _globals['_STREAMSJOBRESPONSE']._serialized_end=538
  _globals['_SCHEDULERSERVICE']._serialized_start=541
  _globals['_SCHEDULERSERVICE']._serialized_end=705
# @@protoc_insertion_point(module_scope)
