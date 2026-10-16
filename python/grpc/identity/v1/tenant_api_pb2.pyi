from identity.v1 import tenant_pb2 as _tenant_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateTenantRequest(_message.Message):
    __slots__ = ("tenant",)
    TENANT_FIELD_NUMBER: _ClassVar[int]
    tenant: _tenant_pb2.Tenant
    def __init__(self, tenant: _Optional[_Union[_tenant_pb2.Tenant, _Mapping]] = ...) -> None: ...

class CreateTenantResponse(_message.Message):
    __slots__ = ("tenant",)
    TENANT_FIELD_NUMBER: _ClassVar[int]
    tenant: _tenant_pb2.Tenant
    def __init__(self, tenant: _Optional[_Union[_tenant_pb2.Tenant, _Mapping]] = ...) -> None: ...

class GetTenantByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetTenantByIDResponse(_message.Message):
    __slots__ = ("tenant",)
    TENANT_FIELD_NUMBER: _ClassVar[int]
    tenant: _tenant_pb2.Tenant
    def __init__(self, tenant: _Optional[_Union[_tenant_pb2.Tenant, _Mapping]] = ...) -> None: ...

class UpdateTenantByIDRequest(_message.Message):
    __slots__ = ("id", "tenant")
    ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_FIELD_NUMBER: _ClassVar[int]
    id: str
    tenant: _tenant_pb2.Tenant
    def __init__(self, id: _Optional[str] = ..., tenant: _Optional[_Union[_tenant_pb2.Tenant, _Mapping]] = ...) -> None: ...

class UpdateTenantByIDResponse(_message.Message):
    __slots__ = ("tenant",)
    TENANT_FIELD_NUMBER: _ClassVar[int]
    tenant: _tenant_pb2.Tenant
    def __init__(self, tenant: _Optional[_Union[_tenant_pb2.Tenant, _Mapping]] = ...) -> None: ...

class DeleteTenantByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteTenantByIDResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListTenantsRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListTenantsResponse(_message.Message):
    __slots__ = ("tenants", "next_page_token")
    TENANTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tenants: _containers.RepeatedCompositeFieldContainer[_tenant_pb2.Tenant]
    next_page_token: str
    def __init__(self, tenants: _Optional[_Iterable[_Union[_tenant_pb2.Tenant, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
