from auth.v1 import idp_provider_pb2 as _idp_provider_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateIdpProviderRequest(_message.Message):
    __slots__ = ("idp_provider",)
    IDP_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    idp_provider: _idp_provider_pb2.IdpProvider
    def __init__(self, idp_provider: _Optional[_Union[_idp_provider_pb2.IdpProvider, _Mapping]] = ...) -> None: ...

class CreateIdpProviderResponse(_message.Message):
    __slots__ = ("idp_provider",)
    IDP_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    idp_provider: _idp_provider_pb2.IdpProvider
    def __init__(self, idp_provider: _Optional[_Union[_idp_provider_pb2.IdpProvider, _Mapping]] = ...) -> None: ...

class GetIdpProviderByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetIdpProviderByIDResponse(_message.Message):
    __slots__ = ("idp_provider",)
    IDP_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    idp_provider: _idp_provider_pb2.IdpProvider
    def __init__(self, idp_provider: _Optional[_Union[_idp_provider_pb2.IdpProvider, _Mapping]] = ...) -> None: ...

class UpdateIdpProviderByIDRequest(_message.Message):
    __slots__ = ("id", "idp_provider")
    ID_FIELD_NUMBER: _ClassVar[int]
    IDP_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    id: str
    idp_provider: _idp_provider_pb2.IdpProvider
    def __init__(self, id: _Optional[str] = ..., idp_provider: _Optional[_Union[_idp_provider_pb2.IdpProvider, _Mapping]] = ...) -> None: ...

class UpdateIdpProviderByIDResponse(_message.Message):
    __slots__ = ("idp_provider",)
    IDP_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    idp_provider: _idp_provider_pb2.IdpProvider
    def __init__(self, idp_provider: _Optional[_Union[_idp_provider_pb2.IdpProvider, _Mapping]] = ...) -> None: ...

class DeleteIdpProviderByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteIdpProviderByIDResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListIdpProvidersRequest(_message.Message):
    __slots__ = ("tenant_id", "page_size", "page_token")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    page_size: int
    page_token: str
    def __init__(self, tenant_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListIdpProvidersResponse(_message.Message):
    __slots__ = ("idp_providers", "next_page_token")
    IDP_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    idp_providers: _containers.RepeatedCompositeFieldContainer[_idp_provider_pb2.IdpProvider]
    next_page_token: str
    def __init__(self, idp_providers: _Optional[_Iterable[_Union[_idp_provider_pb2.IdpProvider, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
