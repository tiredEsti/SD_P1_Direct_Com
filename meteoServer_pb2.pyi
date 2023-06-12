from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessedData(_message.Message):
    __slots__ = ["poll", "timestampPoll", "timestampWell", "well"]
    POLL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPPOLL_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMPWELL_FIELD_NUMBER: _ClassVar[int]
    WELL_FIELD_NUMBER: _ClassVar[int]
    poll: float
    timestampPoll: str
    timestampWell: str
    well: float
    def __init__(self, well: _Optional[float] = ..., poll: _Optional[float] = ..., timestampWell: _Optional[str] = ..., timestampPoll: _Optional[str] = ...) -> None: ...

class RawMeteoData(_message.Message):
    __slots__ = ["humidity", "temperature", "timestamp"]
    HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    humidity: float
    temperature: float
    timestamp: str
    def __init__(self, temperature: _Optional[float] = ..., humidity: _Optional[float] = ..., timestamp: _Optional[str] = ...) -> None: ...

class RawPollutionData(_message.Message):
    __slots__ = ["co2", "timestamp"]
    CO2_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    co2: float
    timestamp: str
    def __init__(self, co2: _Optional[float] = ..., timestamp: _Optional[str] = ...) -> None: ...
