from common.v1 import meta_pb2 as _meta_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TenantStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TENANT_STATUS_UNSPECIFIED: _ClassVar[TenantStatus]
    TENANT_STATUS_ACTIVE: _ClassVar[TenantStatus]
    TENANT_STATUS_SUSPENDED: _ClassVar[TenantStatus]
TENANT_STATUS_UNSPECIFIED: TenantStatus
TENANT_STATUS_ACTIVE: TenantStatus
TENANT_STATUS_SUSPENDED: TenantStatus

class Tenant(_message.Message):
    __slots__ = ("id", "name", "status", "self_signup_enabled", "meta")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SELF_SIGNUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    status: TenantStatus
    self_signup_enabled: bool
    meta: _meta_pb2.Meta
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[TenantStatus, str]] = ..., self_signup_enabled: _Optional[bool] = ..., meta: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
