# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: template.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0etemplate.proto\x12\x05types\x1a\x0c\x63ommon.proto\"\xb7\x01\n\x0f\x41nalyzeTemplate\x12!\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x11.types.FieldTypes\x12\x11\n\tallFields\x18\x02 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x12\n\ncreateTime\x18\x04 \x01(\t\x12\x14\n\x0cmodifiedTime\x18\x05 \x01(\t\x12\x10\n\x08language\x18\x06 \x01(\t\x12\x1d\n\x15resultsScoreThreshold\x18\x07 \x01(\x02\"\xca\x01\n\x11\x41nonymizeTemplate\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\ncreateTime\x18\x02 \x01(\t\x12\x14\n\x0cmodifiedTime\x18\x03 \x01(\t\x12@\n\x18\x66ieldTypeTransformations\x18\x04 \x03(\x0b\x32\x1e.types.FieldTypeTransformation\x12\x34\n\x15\x64\x65\x66\x61ultTransformation\x18\x05 \x01(\x0b\x32\x15.types.Transformation\"g\n\x12JsonSchemaTemplate\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\ncreateTime\x18\x02 \x01(\t\x12\x14\n\x0cmodifiedTime\x18\x03 \x01(\t\x12\x12\n\njsonSchema\x18\x04 \x01(\t\"k\n\x17\x46ieldTypeTransformation\x12!\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x11.types.FieldTypes\x12-\n\x0etransformation\x18\x02 \x01(\x0b\x32\x15.types.Transformation\"\xd1\x01\n\x0eTransformation\x12)\n\x0creplaceValue\x18\x02 \x01(\x0b\x32\x13.types.ReplaceValue\x12\'\n\x0bredactValue\x18\x03 \x01(\x0b\x32\x12.types.RedactValue\x12#\n\thashValue\x18\x04 \x01(\x0b\x32\x10.types.HashValue\x12#\n\tmaskValue\x18\x05 \x01(\x0b\x32\x10.types.MaskValue\x12!\n\x08\x66PEValue\x18\x06 \x01(\x0b\x32\x0f.types.FPEValue\" \n\x0cReplaceValue\x12\x10\n\x08newValue\x18\x01 \x01(\t\"\r\n\x0bRedactValue\"\x0b\n\tHashValue\"K\n\tMaskValue\x12\x18\n\x10maskingCharacter\x18\x01 \x01(\t\x12\x13\n\x0b\x63harsToMask\x18\x02 \x01(\x05\x12\x0f\n\x07\x66romEnd\x18\x03 \x01(\x08\"7\n\x08\x46PEValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05tweak\x18\x02 \x01(\t\x12\x0f\n\x07\x64\x65\x63rypt\x18\x03 \x01(\x08\"E\n\x08\x44\x42\x43onfig\x12\x18\n\x10\x63onnectionString\x18\x01 \x01(\t\x12\x11\n\ttableName\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"\x8f\x01\n\x08\x44\x61tasink\x12!\n\x08\x64\x62\x43onfig\x18\x01 \x01(\x0b\x32\x0f.types.DBConfig\x12\x35\n\x12\x63loudStorageConfig\x18\x02 \x01(\x0b\x32\x19.types.CloudStorageConfig\x12)\n\x0cstreamConfig\x18\x03 \x01(\x0b\x32\x13.types.StreamConfig\"}\n\x10\x44\x61tasinkTemplate\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12(\n\x0f\x61nalyzeDatasink\x18\x02 \x03(\x0b\x32\x0f.types.Datasink\x12*\n\x11\x61nonymizeDatasink\x18\x03 \x03(\x0b\x32\x0f.types.Datasink\"S\n\x11\x42lobStorageConfig\x12\x13\n\x0b\x61\x63\x63ountName\x18\x01 \x01(\t\x12\x12\n\naccountKey\x18\x02 \x01(\t\x12\x15\n\rcontainerName\x18\x03 \x01(\t\"e\n\x08S3Config\x12\x10\n\x08\x61\x63\x63\x65ssId\x18\x01 \x01(\t\x12\x11\n\taccessKey\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x12\n\nbucketName\x18\x04 \x01(\t\x12\x10\n\x08\x65ndpoint\x18\x05 \x01(\t\"Z\n\x13GoogleStorageConfig\x12\x0c\n\x04json\x18\x01 \x01(\t\x12\x11\n\tprojectId\x18\x02 \x01(\t\x12\x0e\n\x06scopes\x18\x03 \x01(\t\x12\x12\n\nbucketName\x18\x04 \x01(\t\"\xa5\x01\n\x12\x43loudStorageConfig\x12\x33\n\x11\x62lobStorageConfig\x18\x01 \x01(\x0b\x32\x18.types.BlobStorageConfig\x12!\n\x08s3Config\x18\x02 \x01(\x0b\x32\x0f.types.S3Config\x12\x37\n\x13GoogleStorageConfig\x18\x03 \x01(\x0b\x32\x1a.types.GoogleStorageConfig\"r\n\x0cStreamConfig\x12\'\n\x0bkafkaConfig\x18\x01 \x01(\x0b\x32\x12.types.KafkaConfig\x12!\n\x08\x65hConfig\x18\x02 \x01(\x0b\x32\x0f.types.EHConfig\x12\x16\n\x0epartitionCount\x18\x03 \x01(\x05\"Y\n\x0bKafkaConfig\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\r\n\x05topic\x18\x02 \x01(\t\x12\x14\n\x0csaslUsername\x18\x03 \x01(\t\x12\x14\n\x0csaslPassword\x18\x04 \x01(\t\"\xcb\x01\n\x08\x45HConfig\x12\x13\n\x0b\x65hNamespace\x18\x01 \x01(\t\x12\x0e\n\x06\x65hName\x18\x02 \x01(\t\x12\x1a\n\x12\x65hConnectionString\x18\x03 \x01(\t\x12\x11\n\tehKeyName\x18\x04 \x01(\t\x12\x12\n\nehKeyValue\x18\x05 \x01(\t\x12\x1f\n\x17storageAccountNameValue\x18\x06 \x01(\t\x12\x1e\n\x16storageAccountKeyValue\x18\x07 \x01(\t\x12\x16\n\x0e\x63ontainerValue\x18\x08 \x01(\t\"\xb2\x01\n\x0eStreamTemplate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12)\n\x0cstreamConfig\x18\x03 \x01(\x0b\x32\x13.types.StreamConfig\x12\x19\n\x11\x61nalyzeTemplateId\x18\x04 \x01(\t\x12\x1b\n\x13\x61nonymizeTemplateId\x18\x05 \x01(\t\x12\x1a\n\x12\x64\x61tasinkTemplateId\x18\x06 \x01(\t\"Z\n\x0cScanTemplate\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x35\n\x12\x63loudStorageConfig\x18\x02 \x01(\x0b\x32\x19.types.CloudStorageConfig\"\xc8\x01\n\x16ScannerCronJobTemplate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1f\n\x07trigger\x18\x03 \x01(\x0b\x32\x0e.types.Trigger\x12\x16\n\x0escanTemplateId\x18\x04 \x01(\t\x12\x19\n\x11\x61nalyzeTemplateId\x18\x05 \x01(\t\x12\x1b\n\x13\x61nonymizeTemplateId\x18\x06 \x01(\t\x12\x1a\n\x12\x64\x61tasinkTemplateId\x18\x07 \x01(\t\"\xa6\x01\n\x12StreamsJobTemplate\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x19\n\x11streamsTemplateId\x18\x03 \x01(\t\x12\x19\n\x11\x61nalyzeTemplateId\x18\x04 \x01(\t\x12\x1b\n\x13\x61nonymizeTemplateId\x18\x05 \x01(\t\x12\x1a\n\x12\x64\x61tasinkTemplateId\x18\x06 \x01(\t\",\n\x07Trigger\x12!\n\x08schedule\x18\x01 \x01(\x0b\x32\x0f.types.Schedule\"$\n\x08Schedule\x12\x18\n\x10recurrencePeriod\x18\x01 \x01(\t\"\x8b\x01\n\x16\x41nonymizeImageTemplate\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x12\n\ncreateTime\x18\x02 \x01(\t\x12\x14\n\x0cmodifiedTime\x18\x03 \x01(\t\x12\x32\n\x11\x66ieldTypeGraphics\x18\x04 \x03(\x0b\x32\x17.types.FieldTypeGraphic\"V\n\x10\x46ieldTypeGraphic\x12!\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x11.types.FieldTypes\x12\x1f\n\x07graphic\x18\x02 \x01(\x0b\x32\x0e.types.Graphic\"8\n\x07Graphic\x12-\n\x0e\x66illColorValue\x18\x01 \x01(\x0b\x32\x15.types.FillColorValue\":\n\x0e\x46illColorValue\x12\x0b\n\x03red\x18\x01 \x01(\x01\x12\r\n\x05green\x18\x02 \x01(\x01\x12\x0c\n\x04\x62lue\x18\x03 \x01(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'template_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ANALYZETEMPLATE']._serialized_start=40
  _globals['_ANALYZETEMPLATE']._serialized_end=223
  _globals['_ANONYMIZETEMPLATE']._serialized_start=226
  _globals['_ANONYMIZETEMPLATE']._serialized_end=428
  _globals['_JSONSCHEMATEMPLATE']._serialized_start=430
  _globals['_JSONSCHEMATEMPLATE']._serialized_end=533
  _globals['_FIELDTYPETRANSFORMATION']._serialized_start=535
  _globals['_FIELDTYPETRANSFORMATION']._serialized_end=642
  _globals['_TRANSFORMATION']._serialized_start=645
  _globals['_TRANSFORMATION']._serialized_end=854
  _globals['_REPLACEVALUE']._serialized_start=856
  _globals['_REPLACEVALUE']._serialized_end=888
  _globals['_REDACTVALUE']._serialized_start=890
  _globals['_REDACTVALUE']._serialized_end=903
  _globals['_HASHVALUE']._serialized_start=905
  _globals['_HASHVALUE']._serialized_end=916
  _globals['_MASKVALUE']._serialized_start=918
  _globals['_MASKVALUE']._serialized_end=993
  _globals['_FPEVALUE']._serialized_start=995
  _globals['_FPEVALUE']._serialized_end=1050
  _globals['_DBCONFIG']._serialized_start=1052
  _globals['_DBCONFIG']._serialized_end=1121
  _globals['_DATASINK']._serialized_start=1124
  _globals['_DATASINK']._serialized_end=1267
  _globals['_DATASINKTEMPLATE']._serialized_start=1269
  _globals['_DATASINKTEMPLATE']._serialized_end=1394
  _globals['_BLOBSTORAGECONFIG']._serialized_start=1396
  _globals['_BLOBSTORAGECONFIG']._serialized_end=1479
  _globals['_S3CONFIG']._serialized_start=1481
  _globals['_S3CONFIG']._serialized_end=1582
  _globals['_GOOGLESTORAGECONFIG']._serialized_start=1584
  _globals['_GOOGLESTORAGECONFIG']._serialized_end=1674
  _globals['_CLOUDSTORAGECONFIG']._serialized_start=1677
  _globals['_CLOUDSTORAGECONFIG']._serialized_end=1842
  _globals['_STREAMCONFIG']._serialized_start=1844
  _globals['_STREAMCONFIG']._serialized_end=1958
  _globals['_KAFKACONFIG']._serialized_start=1960
  _globals['_KAFKACONFIG']._serialized_end=2049
  _globals['_EHCONFIG']._serialized_start=2052
  _globals['_EHCONFIG']._serialized_end=2255
  _globals['_STREAMTEMPLATE']._serialized_start=2258
  _globals['_STREAMTEMPLATE']._serialized_end=2436
  _globals['_SCANTEMPLATE']._serialized_start=2438
  _globals['_SCANTEMPLATE']._serialized_end=2528
  _globals['_SCANNERCRONJOBTEMPLATE']._serialized_start=2531
  _globals['_SCANNERCRONJOBTEMPLATE']._serialized_end=2731
  _globals['_STREAMSJOBTEMPLATE']._serialized_start=2734
  _globals['_STREAMSJOBTEMPLATE']._serialized_end=2900
  _globals['_TRIGGER']._serialized_start=2902
  _globals['_TRIGGER']._serialized_end=2946
  _globals['_SCHEDULE']._serialized_start=2948
  _globals['_SCHEDULE']._serialized_end=2984
  _globals['_ANONYMIZEIMAGETEMPLATE']._serialized_start=2987
  _globals['_ANONYMIZEIMAGETEMPLATE']._serialized_end=3126
  _globals['_FIELDTYPEGRAPHIC']._serialized_start=3128
  _globals['_FIELDTYPEGRAPHIC']._serialized_end=3214
  _globals['_GRAPHIC']._serialized_start=3216
  _globals['_GRAPHIC']._serialized_end=3272
  _globals['_FILLCOLORVALUE']._serialized_start=3274
  _globals['_FILLCOLORVALUE']._serialized_end=3332
# @@protoc_insertion_point(module_scope)
