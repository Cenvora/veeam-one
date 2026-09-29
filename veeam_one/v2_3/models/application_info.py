from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.application_platform import ApplicationPlatform
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_group import ProtectionGroup


T = TypeVar("T", bound="ApplicationInfo")


@_attrs_define
class ApplicationInfo:
    """
    Attributes:
        application_id (int | Unset): ID assigned to an application.
        application_uid_in_vbr (None | Unset | UUID): UID assigned to an application in Veeam Backup & Replication.
        backup_server_id (int | None | Unset): ID assigned to the Veeam Backup & Replication server.
        name (None | str | Unset): Name of an application.
        platform (ApplicationPlatform | Unset):
        protection_groups (list[ProtectionGroup] | None | Unset): Array of protection groups that include the
            application.
        ip_address (None | str | Unset): IP address of an application.
        business_view_group_ids (list[int] | None | Unset): Array of IDs assigned to Business View groups that include
            the application.
    """

    application_id: int | Unset = UNSET
    application_uid_in_vbr: None | Unset | UUID = UNSET
    backup_server_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    platform: ApplicationPlatform | Unset = UNSET
    protection_groups: list[ProtectionGroup] | None | Unset = UNSET
    ip_address: None | str | Unset = UNSET
    business_view_group_ids: list[int] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        application_uid_in_vbr: None | str | Unset
        if isinstance(self.application_uid_in_vbr, Unset):
            application_uid_in_vbr = UNSET
        elif isinstance(self.application_uid_in_vbr, UUID):
            application_uid_in_vbr = str(self.application_uid_in_vbr)
        else:
            application_uid_in_vbr = self.application_uid_in_vbr

        backup_server_id: int | None | Unset
        if isinstance(self.backup_server_id, Unset):
            backup_server_id = UNSET
        else:
            backup_server_id = self.backup_server_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        platform: str | Unset = UNSET
        if not isinstance(self.platform, Unset):
            platform = self.platform.value

        protection_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.protection_groups, Unset):
            protection_groups = UNSET
        elif isinstance(self.protection_groups, list):
            protection_groups = []
            for protection_groups_type_0_item_data in self.protection_groups:
                protection_groups_type_0_item = protection_groups_type_0_item_data.to_dict()
                protection_groups.append(protection_groups_type_0_item)

        else:
            protection_groups = self.protection_groups

        ip_address: None | str | Unset
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = self.ip_address

        business_view_group_ids: list[int] | None | Unset
        if isinstance(self.business_view_group_ids, Unset):
            business_view_group_ids = UNSET
        elif isinstance(self.business_view_group_ids, list):
            business_view_group_ids = self.business_view_group_ids

        else:
            business_view_group_ids = self.business_view_group_ids

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_uid_in_vbr is not UNSET:
            field_dict["applicationUidInVbr"] = application_uid_in_vbr
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if name is not UNSET:
            field_dict["name"] = name
        if platform is not UNSET:
            field_dict["platform"] = platform
        if protection_groups is not UNSET:
            field_dict["protectionGroups"] = protection_groups
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if business_view_group_ids is not UNSET:
            field_dict["businessViewGroupIds"] = business_view_group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_group import ProtectionGroup  # noqa: PLC0415

        d = dict(src_dict)
        application_id = d.pop("applicationId", UNSET)

        def _parse_application_uid_in_vbr(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                application_uid_in_vbr_type_0 = UUID(data)

                return application_uid_in_vbr_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        application_uid_in_vbr = _parse_application_uid_in_vbr(d.pop("applicationUidInVbr", UNSET))

        def _parse_backup_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        backup_server_id = _parse_backup_server_id(d.pop("backupServerId", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _platform = d.pop("platform", UNSET)
        platform: ApplicationPlatform | Unset
        if isinstance(_platform, Unset):
            platform = UNSET
        else:
            platform = ApplicationPlatform(_platform)

        def _parse_protection_groups(data: object) -> list[ProtectionGroup] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                protection_groups_type_0 = []
                _protection_groups_type_0 = data
                for protection_groups_type_0_item_data in _protection_groups_type_0:
                    protection_groups_type_0_item = ProtectionGroup.from_dict(protection_groups_type_0_item_data)

                    protection_groups_type_0.append(protection_groups_type_0_item)

                return protection_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ProtectionGroup] | None | Unset, data)

        protection_groups = _parse_protection_groups(d.pop("protectionGroups", UNSET))

        def _parse_ip_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_address = _parse_ip_address(d.pop("ipAddress", UNSET))

        def _parse_business_view_group_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                business_view_group_ids_type_0 = cast(list[int], data)

                return business_view_group_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        business_view_group_ids = _parse_business_view_group_ids(d.pop("businessViewGroupIds", UNSET))

        application_info = cls(
            application_id=application_id,
            application_uid_in_vbr=application_uid_in_vbr,
            backup_server_id=backup_server_id,
            name=name,
            platform=platform,
            protection_groups=protection_groups,
            ip_address=ip_address,
            business_view_group_ids=business_view_group_ids,
        )

        return application_info
