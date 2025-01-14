from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Response(_message.Message):
    __slots__ = ["name", "age", "d", "m_MyMessage", "m_string"]
    class DEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    M_MYMESSAGE_FIELD_NUMBER: _ClassVar[int]
    M_STRING_FIELD_NUMBER: _ClassVar[int]
    name: str
    age: int
    d: _containers.ScalarMap[str, str]
    m_MyMessage: MyMessage
    m_string: str
    def __init__(self, name: _Optional[str] = ..., age: _Optional[int] = ..., d: _Optional[_Mapping[str, str]] = ..., m_MyMessage: _Optional[_Union[MyMessage, _Mapping]] = ..., m_string: _Optional[str] = ...) -> None: ...

class MyMessage(_message.Message):
    __slots__ = ["name", "age", "o_int32", "o_google_protobuf_Timestamp"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    O_INT32_FIELD_NUMBER: _ClassVar[int]
    O_GOOGLE_PROTOBUF_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    name: str
    age: int
    o_int32: int
    o_google_protobuf_Timestamp: _timestamp_pb2.Timestamp
    def __init__(self, name: _Optional[str] = ..., age: _Optional[int] = ..., o_int32: _Optional[int] = ..., o_google_protobuf_Timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ["name", "age", "d", "m"]
    class DEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGE_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    M_FIELD_NUMBER: _ClassVar[int]
    name: str
    age: int
    d: _containers.ScalarMap[str, str]
    m: MyMessage
    def __init__(self, name: _Optional[str] = ..., age: _Optional[int] = ..., d: _Optional[_Mapping[str, str]] = ..., m: _Optional[_Union[MyMessage, _Mapping]] = ...) -> None: ...
