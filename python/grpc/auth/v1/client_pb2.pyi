import datetime

from common.v1 import meta_pb2 as _meta_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GrantType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRANT_TYPE_UNSPECIFIED: _ClassVar[GrantType]
    GRANT_TYPE_AUTHORIZATION_CODE: _ClassVar[GrantType]
    GRANT_TYPE_PASSWORD: _ClassVar[GrantType]
    GRANT_TYPE_IMPLICIT: _ClassVar[GrantType]
    GRANT_TYPE_CLIENT_CREDENTIALS: _ClassVar[GrantType]
    GRANT_TYPE_REFRESH_TOKEN: _ClassVar[GrantType]
    GRANT_TYPE_DEVICE_CODE: _ClassVar[GrantType]
    GRANT_TYPE_JWT_BEARER: _ClassVar[GrantType]

class ResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESPONSE_TYPE_UNSPECIFIED: _ClassVar[ResponseType]
    RESPONSE_TYPE_CODE: _ClassVar[ResponseType]
    RESPONSE_TYPE_TOKEN: _ClassVar[ResponseType]
    RESPONSE_TYPE_ID_TOKEN: _ClassVar[ResponseType]

class TokenEndpointAuthMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TOKEN_ENDPOINT_AUTH_METHOD_UNSPECIFIED: _ClassVar[TokenEndpointAuthMethod]
    TOKEN_ENDPOINT_AUTH_METHOD_CLIENT_SECRET_BASIC: _ClassVar[TokenEndpointAuthMethod]
    TOKEN_ENDPOINT_AUTH_METHOD_CLIENT_SECRET_POST: _ClassVar[TokenEndpointAuthMethod]
    TOKEN_ENDPOINT_AUTH_METHOD_NONE: _ClassVar[TokenEndpointAuthMethod]
    TOKEN_ENDPOINT_AUTH_METHOD_PRIVATE_KEY_JWT: _ClassVar[TokenEndpointAuthMethod]

class SubjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUBJECT_TYPE_UNSPECIFIED: _ClassVar[SubjectType]
    SUBJECT_TYPE_PUBLIC: _ClassVar[SubjectType]
    SUBJECT_TYPE_PAIRWISE: _ClassVar[SubjectType]
GRANT_TYPE_UNSPECIFIED: GrantType
GRANT_TYPE_AUTHORIZATION_CODE: GrantType
GRANT_TYPE_PASSWORD: GrantType
GRANT_TYPE_IMPLICIT: GrantType
GRANT_TYPE_CLIENT_CREDENTIALS: GrantType
GRANT_TYPE_REFRESH_TOKEN: GrantType
GRANT_TYPE_DEVICE_CODE: GrantType
GRANT_TYPE_JWT_BEARER: GrantType
RESPONSE_TYPE_UNSPECIFIED: ResponseType
RESPONSE_TYPE_CODE: ResponseType
RESPONSE_TYPE_TOKEN: ResponseType
RESPONSE_TYPE_ID_TOKEN: ResponseType
TOKEN_ENDPOINT_AUTH_METHOD_UNSPECIFIED: TokenEndpointAuthMethod
TOKEN_ENDPOINT_AUTH_METHOD_CLIENT_SECRET_BASIC: TokenEndpointAuthMethod
TOKEN_ENDPOINT_AUTH_METHOD_CLIENT_SECRET_POST: TokenEndpointAuthMethod
TOKEN_ENDPOINT_AUTH_METHOD_NONE: TokenEndpointAuthMethod
TOKEN_ENDPOINT_AUTH_METHOD_PRIVATE_KEY_JWT: TokenEndpointAuthMethod
SUBJECT_TYPE_UNSPECIFIED: SubjectType
SUBJECT_TYPE_PUBLIC: SubjectType
SUBJECT_TYPE_PAIRWISE: SubjectType

class Client(_message.Message):
    __slots__ = ("id", "client_secret", "name", "client_uri", "logo_uri", "redirect_uris", "post_logout_redirect_uris", "grant_types", "response_types", "scopes", "audience", "token_endpoint_auth_method", "jwks_uri", "is_public", "subject_type", "access_token_ttl", "refresh_token_ttl", "contacts", "tenant_id", "active", "meta")
    ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_URI_FIELD_NUMBER: _ClassVar[int]
    LOGO_URI_FIELD_NUMBER: _ClassVar[int]
    REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    POST_LOGOUT_REDIRECT_URIS_FIELD_NUMBER: _ClassVar[int]
    GRANT_TYPES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPES_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ENDPOINT_AUTH_METHOD_FIELD_NUMBER: _ClassVar[int]
    JWKS_URI_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_TTL_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_TTL_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    id: str
    client_secret: str
    name: str
    client_uri: str
    logo_uri: str
    redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    post_logout_redirect_uris: _containers.RepeatedScalarFieldContainer[str]
    grant_types: _containers.RepeatedScalarFieldContainer[GrantType]
    response_types: _containers.RepeatedScalarFieldContainer[ResponseType]
    scopes: _containers.RepeatedScalarFieldContainer[str]
    audience: _containers.RepeatedScalarFieldContainer[str]
    token_endpoint_auth_method: TokenEndpointAuthMethod
    jwks_uri: str
    is_public: bool
    subject_type: SubjectType
    access_token_ttl: _duration_pb2.Duration
    refresh_token_ttl: _duration_pb2.Duration
    contacts: _containers.RepeatedScalarFieldContainer[str]
    tenant_id: str
    active: bool
    meta: _meta_pb2.Meta
    def __init__(self, id: _Optional[str] = ..., client_secret: _Optional[str] = ..., name: _Optional[str] = ..., client_uri: _Optional[str] = ..., logo_uri: _Optional[str] = ..., redirect_uris: _Optional[_Iterable[str]] = ..., post_logout_redirect_uris: _Optional[_Iterable[str]] = ..., grant_types: _Optional[_Iterable[_Union[GrantType, str]]] = ..., response_types: _Optional[_Iterable[_Union[ResponseType, str]]] = ..., scopes: _Optional[_Iterable[str]] = ..., audience: _Optional[_Iterable[str]] = ..., token_endpoint_auth_method: _Optional[_Union[TokenEndpointAuthMethod, str]] = ..., jwks_uri: _Optional[str] = ..., is_public: _Optional[bool] = ..., subject_type: _Optional[_Union[SubjectType, str]] = ..., access_token_ttl: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., refresh_token_ttl: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]] = ..., contacts: _Optional[_Iterable[str]] = ..., tenant_id: _Optional[str] = ..., active: _Optional[bool] = ..., meta: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
