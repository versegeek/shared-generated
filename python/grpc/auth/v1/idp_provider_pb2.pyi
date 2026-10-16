from common.v1 import meta_pb2 as _meta_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IdpProviderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IDP_PROVIDER_TYPE_UNSPECIFIED: _ClassVar[IdpProviderType]
    IDP_PROVIDER_TYPE_GOOGLE: _ClassVar[IdpProviderType]
    IDP_PROVIDER_TYPE_GITHUB: _ClassVar[IdpProviderType]
    IDP_PROVIDER_TYPE_WECHAT: _ClassVar[IdpProviderType]
    IDP_PROVIDER_TYPE_FACEBOOK: _ClassVar[IdpProviderType]
    IDP_PROVIDER_TYPE_APPLE: _ClassVar[IdpProviderType]
    IDP_PROVIDER_TYPE_MICROSOFT: _ClassVar[IdpProviderType]
    IDP_PROVIDER_TYPE_SAML: _ClassVar[IdpProviderType]
    IDP_PROVIDER_TYPE_OIDC: _ClassVar[IdpProviderType]
    IDP_PROVIDER_TYPE_LDAP: _ClassVar[IdpProviderType]
IDP_PROVIDER_TYPE_UNSPECIFIED: IdpProviderType
IDP_PROVIDER_TYPE_GOOGLE: IdpProviderType
IDP_PROVIDER_TYPE_GITHUB: IdpProviderType
IDP_PROVIDER_TYPE_WECHAT: IdpProviderType
IDP_PROVIDER_TYPE_FACEBOOK: IdpProviderType
IDP_PROVIDER_TYPE_APPLE: IdpProviderType
IDP_PROVIDER_TYPE_MICROSOFT: IdpProviderType
IDP_PROVIDER_TYPE_SAML: IdpProviderType
IDP_PROVIDER_TYPE_OIDC: IdpProviderType
IDP_PROVIDER_TYPE_LDAP: IdpProviderType

class IdpProvider(_message.Message):
    __slots__ = ("id", "name", "type", "client_id", "client_secret", "scopes", "authorization_endpoint", "token_endpoint", "userinfo_endpoint", "jwks_uri", "issuer", "tenant_id", "enabled", "extra_config", "meta")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZATION_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    USERINFO_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    JWKS_URI_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    EXTRA_CONFIG_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: IdpProviderType
    client_id: str
    client_secret: str
    scopes: _containers.RepeatedScalarFieldContainer[str]
    authorization_endpoint: str
    token_endpoint: str
    userinfo_endpoint: str
    jwks_uri: str
    issuer: str
    tenant_id: str
    enabled: bool
    extra_config: str
    meta: _meta_pb2.Meta
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[_Union[IdpProviderType, str]] = ..., client_id: _Optional[str] = ..., client_secret: _Optional[str] = ..., scopes: _Optional[_Iterable[str]] = ..., authorization_endpoint: _Optional[str] = ..., token_endpoint: _Optional[str] = ..., userinfo_endpoint: _Optional[str] = ..., jwks_uri: _Optional[str] = ..., issuer: _Optional[str] = ..., tenant_id: _Optional[str] = ..., enabled: _Optional[bool] = ..., extra_config: _Optional[str] = ..., meta: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
