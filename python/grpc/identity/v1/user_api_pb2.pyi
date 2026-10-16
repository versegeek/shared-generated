from identity.v1 import user_pb2 as _user_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateUserRequest(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class GetUserByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetUserByIDResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class GetUserByEmailRequest(_message.Message):
    __slots__ = ("email", "tenant_id")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    tenant_id: str
    def __init__(self, email: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class GetUserByEmailResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class GetUserByIdpIdentityRequest(_message.Message):
    __slots__ = ("idp_provider_id", "subject", "tenant_id")
    IDP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    idp_provider_id: str
    subject: str
    tenant_id: str
    def __init__(self, idp_provider_id: _Optional[str] = ..., subject: _Optional[str] = ..., tenant_id: _Optional[str] = ...) -> None: ...

class GetUserByIdpIdentityResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class UpdateUserByIDRequest(_message.Message):
    __slots__ = ("id", "user")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    id: str
    user: _user_pb2.User
    def __init__(self, id: _Optional[str] = ..., user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class UpdateUserByIDResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class DeleteUserByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteUserByIDResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListUsersRequest(_message.Message):
    __slots__ = ("tenant_id", "page_size", "page_token")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    page_size: int
    page_token: str
    def __init__(self, tenant_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListUsersResponse(_message.Message):
    __slots__ = ("users", "next_page_token")
    USERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    next_page_token: str
    def __init__(self, users: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class LinkIdpIdentityRequest(_message.Message):
    __slots__ = ("user_id", "idp_identity")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IDP_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    idp_identity: _user_pb2.UserIdpIdentity
    def __init__(self, user_id: _Optional[str] = ..., idp_identity: _Optional[_Union[_user_pb2.UserIdpIdentity, _Mapping]] = ...) -> None: ...

class LinkIdpIdentityResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class UnlinkIdpIdentityRequest(_message.Message):
    __slots__ = ("user_id", "idp_provider_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    IDP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    idp_provider_id: str
    def __init__(self, user_id: _Optional[str] = ..., idp_provider_id: _Optional[str] = ...) -> None: ...

class UnlinkIdpIdentityResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...
