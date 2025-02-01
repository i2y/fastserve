from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CityLocation(_message.Message):
    __slots__ = ("city", "country")
    CITY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    city: str
    country: str
    def __init__(
        self, city: _Optional[str] = ..., country: _Optional[str] = ...
    ) -> None: ...

class Olympics(_message.Message):
    __slots__ = ("year",)
    YEAR_FIELD_NUMBER: _ClassVar[int]
    year: int
    def __init__(self, year: _Optional[int] = ...) -> None: ...
