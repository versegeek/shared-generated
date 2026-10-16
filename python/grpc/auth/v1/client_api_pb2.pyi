from auth.v1 import client_pb2 as _client_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateClientRequest(_message.Message):
    __slots__ = ("client",)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: _client_pb2.Client
    def __init__(self, client: _Optional[_Union[_client_pb2.Client, _Mapping]] = ...) -> None: ...

class CreateClientResponse(_message.Message):
    __slots__ = ("client",)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: _client_pb2.Client
    def __init__(self, client: _Optional[_Union[_client_pb2.Client, _Mapping]] = ...) -> None: ...

class GetClientByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetClientByIDResponse(_message.Message):
    __slots__ = ("client",)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: _client_pb2.Client
    def __init__(self, client: _Optional[_Union[_client_pb2.Client, _Mapping]] = ...) -> None: ...

class UpdateClientByIDRequest(_message.Message):
    __slots__ = ("id", "client")
    ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    client: _client_pb2.Client
    def __init__(self, id: _Optional[str] = ..., client: _Optional[_Union[_client_pb2.Client, _Mapping]] = ...) -> None: ...

class UpdateClientByIDResponse(_message.Message):
    __slots__ = ("client",)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: _client_pb2.Client
    def __init__(self, client: _Optional[_Union[_client_pb2.Client, _Mapping]] = ...) -> None: ...

class DeleteClientByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteClientByIDResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListClientsRequest(_message.Message):
    __slots__ = ("tenant_id", "page_size", "page_token")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    page_size: int
    page_token: str
    def __init__(self, tenant_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListClientsResponse(_message.Message):
    __slots__ = ("clients", "next_page_token")
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    clients: _containers.RepeatedCompositeFieldContainer[_client_pb2.Client]
    next_page_token: str
    def __init__(self, clients: _Optional[_Iterable[_Union[_client_pb2.Client, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class RotateClientSecretRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RotateClientSecretResponse(_message.Message):
    __slots__ = ("client",)
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: _client_pb2.Client
    def __init__(self, client: _Optional[_Union[_client_pb2.Client, _Mapping]] = ...) -> None: ...
