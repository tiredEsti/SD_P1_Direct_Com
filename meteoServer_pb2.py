# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: meteoServer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11meteoServer.proto\x1a\x1bgoogle/protobuf/empty.proto\"H\n\x0cRawMeteoData\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\x12\x10\n\x08humidity\x18\x02 \x01(\x02\x12\x11\n\ttimestamp\x18\x03 \x01(\t\"2\n\x10RawPollutionData\x12\x0b\n\x03\x63o2\x18\x01 \x01(\x02\x12\x11\n\ttimestamp\x18\x02 \x01(\t2~\n\tLBService\x12\x35\n\nAddAirData\x12\r.RawMeteoData\x1a\x16.google.protobuf.Empty\"\x00\x12:\n\x0b\x41\x64\x64PollData\x12\x11.RawPollutionData\x1a\x16.google.protobuf.Empty\"\x00\x32\x8b\x01\n\x0cMeteoService\x12;\n\x10ProcessMeteoData\x12\r.RawMeteoData\x1a\x16.google.protobuf.Empty\"\x00\x12>\n\x0fProcessPollData\x12\x11.RawPollutionData\x1a\x16.google.protobuf.Empty\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'meteoServer_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RAWMETEODATA._serialized_start=50
  _RAWMETEODATA._serialized_end=122
  _RAWPOLLUTIONDATA._serialized_start=124
  _RAWPOLLUTIONDATA._serialized_end=174
  _LBSERVICE._serialized_start=176
  _LBSERVICE._serialized_end=302
  _METEOSERVICE._serialized_start=305
  _METEOSERVICE._serialized_end=444
# @@protoc_insertion_point(module_scope)
