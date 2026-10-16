from common.v1 import meta_pb2 as _meta_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_STATUS_UNSPECIFIED: _ClassVar[UserStatus]
    USER_STATUS_ACTIVE: _ClassVar[UserStatus]
    USER_STATUS_SUSPENDED: _ClassVar[UserStatus]
    USER_STATUS_PENDING_VERIFICATION: _ClassVar[UserStatus]
    USER_STATUS_DELETED: _ClassVar[UserStatus]
USER_STATUS_UNSPECIFIED: UserStatus
USER_STATUS_ACTIVE: UserStatus
USER_STATUS_SUSPENDED: UserStatus
USER_STATUS_PENDING_VERIFICATION: UserStatus
USER_STATUS_DELETED: UserStatus

class User(_message.Message):
    __slots__ = ("id", "email", "email_verified", "phone_number", "phone_verified", "username", "display_name", "given_name", "family_name", "middle_name", "picture_url", "locale", "tenant_id", "status", "idp_identities", "meta")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PHONE_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    GIVEN_NAME_FIELD_NUMBER: _ClassVar[int]
    FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PICTURE_URL_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IDP_IDENTITIES_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    email_verified: bool
    phone_number: str
    phone_verified: bool
    username: str
    display_name: str
    given_name: str
    family_name: str
    middle_name: str
    picture_url: str
    locale: str
    tenant_id: str
    status: UserStatus
    idp_identities: _containers.RepeatedCompositeFieldContainer[UserIdpIdentity]
    meta: _meta_pb2.Meta
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., email_verified: _Optional[bool] = ..., phone_number: _Optional[str] = ..., phone_verified: _Optional[bool] = ..., username: _Optional[str] = ..., display_name: _Optional[str] = ..., given_name: _Optional[str] = ..., family_name: _Optional[str] = ..., middle_name: _Optional[str] = ..., picture_url: _Optional[str] = ..., locale: _Optional[str] = ..., tenant_id: _Optional[str] = ..., status: _Optional[_Union[UserStatus, str]] = ..., idp_identities: _Optional[_Iterable[_Union[UserIdpIdentity, _Mapping]]] = ..., meta: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...

class UserIdpIdentity(_message.Message):
    __slots__ = ("idp_provider_id", "subject", "raw_profile", "meta")
    IDP_PROVIDER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    RAW_PROFILE_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    idp_provider_id: str
    subject: str
    raw_profile: str
    meta: _meta_pb2.Meta
    def __init__(self, idp_provider_id: _Optional[str] = ..., subject: _Optional[str] = ..., raw_profile: _Optional[str] = ..., meta: _Optional[_Union[_meta_pb2.Meta, _Mapping]] = ...) -> None: ...
