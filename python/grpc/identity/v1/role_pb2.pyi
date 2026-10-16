from common.v1 import meta_pb2 as _meta_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Permission(_message.Message):
    __slots__ = ("id", "name", "resource", "action", "description", "tenant_id", "meta")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    resource: str
    action: str
    description: str
    tenant_id: str
    meta: _meta_pb2.Meta
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., resource: _Optional[str] = ..., action: _Optional[str] = ..., description: _Optional[str] = ..., tenant_id: _Optional[str] = ..., meta: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...

class Role(_message.Message):
    __slots__ = ("id", "name", "description", "permission_ids", "permissions", "tenant_id", "meta")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    description: str
    permission_ids: _containers.RepeatedScalarFieldContainer[str]
    permissions: _containers.RepeatedCompositeFieldContainer[Permission]
    tenant_id: str
    meta: _meta_pb2.Meta
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., permission_ids: _Optional[_Iterable[str]] = ..., permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]] = ..., tenant_id: _Optional[str] = ..., meta: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...

class RoleBinding(_message.Message):
    __slots__ = ("id", "role_id", "user_id", "resource_scope", "tenant_id", "meta")
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    id: str
    role_id: str
    user_id: str
    resource_scope: str
    tenant_id: str
    meta: _meta_pb2.Meta
    def __init__(self, id: _Optional[str] = ..., role_id: _Optional[str] = ..., user_id: _Optional[str] = ..., resource_scope: _Optional[str] = ..., tenant_id: _Optional[str] = ..., meta: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
