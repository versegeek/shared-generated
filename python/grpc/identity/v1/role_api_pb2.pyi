from identity.v1 import role_pb2 as _role_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRoleRequest(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: _role_pb2.Role
    def __init__(self, role: _Optional[_Union[_role_pb2.Role, _Mapping]] = ...) -> None: ...

class CreateRoleResponse(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: _role_pb2.Role
    def __init__(self, role: _Optional[_Union[_role_pb2.Role, _Mapping]] = ...) -> None: ...

class GetRoleByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetRoleByIDResponse(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: _role_pb2.Role
    def __init__(self, role: _Optional[_Union[_role_pb2.Role, _Mapping]] = ...) -> None: ...

class UpdateRoleByIDRequest(_message.Message):
    __slots__ = ("id", "role")
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    role: _role_pb2.Role
    def __init__(self, id: _Optional[str] = ..., role: _Optional[_Union[_role_pb2.Role, _Mapping]] = ...) -> None: ...

class UpdateRoleByIDResponse(_message.Message):
    __slots__ = ("role",)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: _role_pb2.Role
    def __init__(self, role: _Optional[_Union[_role_pb2.Role, _Mapping]] = ...) -> None: ...

class DeleteRoleByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteRoleByIDResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRolesRequest(_message.Message):
    __slots__ = ("tenant_id", "page_size", "page_token")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    page_size: int
    page_token: str
    def __init__(self, tenant_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListRolesResponse(_message.Message):
    __slots__ = ("roles", "next_page_token")
    ROLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[_role_pb2.Role]
    next_page_token: str
    def __init__(self, roles: _Optional[_Iterable[_Union[_role_pb2.Role, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class CreatePermissionRequest(_message.Message):
    __slots__ = ("permission",)
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    permission: _role_pb2.Permission
    def __init__(self, permission: _Optional[_Union[_role_pb2.Permission, _Mapping]] = ...) -> None: ...

class CreatePermissionResponse(_message.Message):
    __slots__ = ("permission",)
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    permission: _role_pb2.Permission
    def __init__(self, permission: _Optional[_Union[_role_pb2.Permission, _Mapping]] = ...) -> None: ...

class GetPermissionByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetPermissionByIDResponse(_message.Message):
    __slots__ = ("permission",)
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    permission: _role_pb2.Permission
    def __init__(self, permission: _Optional[_Union[_role_pb2.Permission, _Mapping]] = ...) -> None: ...

class DeletePermissionByIDRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeletePermissionByIDResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPermissionsRequest(_message.Message):
    __slots__ = ("tenant_id", "resource", "page_size", "page_token")
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    resource: str
    page_size: int
    page_token: str
    def __init__(self, tenant_id: _Optional[str] = ..., resource: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListPermissionsResponse(_message.Message):
    __slots__ = ("permissions", "next_page_token")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[_role_pb2.Permission]
    next_page_token: str
    def __init__(self, permissions: _Optional[_Iterable[_Union[_role_pb2.Permission, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AssignRoleRequest(_message.Message):
    __slots__ = ("user_id", "role_id", "tenant_id", "resource_scope")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    role_id: str
    tenant_id: str
    resource_scope: str
    def __init__(self, user_id: _Optional[str] = ..., role_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., resource_scope: _Optional[str] = ...) -> None: ...

class AssignRoleResponse(_message.Message):
    __slots__ = ("role_binding",)
    ROLE_BINDING_FIELD_NUMBER: _ClassVar[int]
    role_binding: _role_pb2.RoleBinding
    def __init__(self, role_binding: _Optional[_Union[_role_pb2.RoleBinding, _Mapping]] = ...) -> None: ...

class RevokeRoleRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class RevokeRoleResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListRoleBindingsRequest(_message.Message):
    __slots__ = ("user_id", "role_id", "tenant_id", "page_size", "page_token")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    role_id: str
    tenant_id: str
    page_size: int
    page_token: str
    def __init__(self, user_id: _Optional[str] = ..., role_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListRoleBindingsResponse(_message.Message):
    __slots__ = ("role_bindings", "next_page_token")
    ROLE_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    role_bindings: _containers.RepeatedCompositeFieldContainer[_role_pb2.RoleBinding]
    next_page_token: str
    def __init__(self, role_bindings: _Optional[_Iterable[_Union[_role_pb2.RoleBinding, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetUserPermissionsRequest(_message.Message):
    __slots__ = ("user_id", "tenant_id", "resource_scope")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    tenant_id: str
    resource_scope: str
    def __init__(self, user_id: _Optional[str] = ..., tenant_id: _Optional[str] = ..., resource_scope: _Optional[str] = ...) -> None: ...

class GetUserPermissionsResponse(_message.Message):
    __slots__ = ("permissions",)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[_role_pb2.Permission]
    def __init__(self, permissions: _Optional[_Iterable[_Union[_role_pb2.Permission, _Mapping]]] = ...) -> None: ...
