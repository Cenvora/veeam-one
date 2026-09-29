from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vb_365_aws_region_type import Vb365AwsRegionType
from ..models.vb_365_object_storage_repository_type import Vb365ObjectStorageRepositoryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365ObjectStorageRepositoryInfo")


@_attrs_define
class Vb365ObjectStorageRepositoryInfo:
    """
    Attributes:
        object_storage_repository_id (int | Unset): ID assigned to an object storage repository.
        object_storage_repository_uid_in_vb_365 (None | Unset | UUID): UID assigned to an object storage repository in
            Veeam Backup for Microsoft 365.
        name (None | str | Unset): Name of an object storage repository.
        vb_365_server_id (int | None | Unset): ID assigned to a Veeam Backup for Microsoft 365 server.
        folder (None | str | Unset): Folder where backups are stored.
        description (None | str | Unset): Description of an object storage repository.
        account_uid (None | Unset | UUID): UID assigned to the account under which an object storage repository was
            added.
        size_limit_enabled (bool | None | Unset): Indicates whether the object storage capacity is limited.
        size_limit_bytes (int | None | Unset): Object storage capacity limit, in bytes.
        used_space_bytes (int | None | Unset): Used space on an object storage repository, in bytes.
        free_space_bytes (int | None | Unset): Available space on an object storage repository, in bytes.
        type_ (Vb365ObjectStorageRepositoryType | Unset):
        glacier_deep_archive_enabled (bool | None | Unset): Indicates whether the Amazon S3 Glacier Deep Archive storage
            class is enabled.
        ia_storage_class_enabled (bool | None | Unset): Indicates whether the Amazon S3 Standard-Infrequent Access
            storage class is enabled for data blocks that are stored in an Amazon S3 object storage.
        use_archiver_appliance (bool | None | Unset): Indicates whether Veeam Backup for Microsoft 365 uses the Amazon
            or Azure archiver appliance when transferring backed-up data to the archive object storage.
        amazon_bucket_s3_compatible_name (None | str | Unset): Name of an S3 Compatible bucket.
        amazon_bucket_s3_compatible_custom_region_id (None | str | Unset): ID assigned to an S3 Compatible bucket
            region.
        amazon_bucket_s3_aws_name (None | str | Unset): Name of an Amazon S3 bucket.
        amazon_bucket_s3_aws_region_type (Vb365AwsRegionType | Unset):
        amazon_bucket_s3_aws_region_name (None | str | Unset): Name of an Amazon S3 bucket region.
        amazon_bucket_s3_aws_region_id (None | str | Unset): ID assigned to an Amazon S3 bucket region.
        azure_container_name (None | str | Unset): Name of a Microsoft Azure container.
        azure_container_region_type (Vb365AwsRegionType | Unset):
    """

    object_storage_repository_id: int | Unset = UNSET
    object_storage_repository_uid_in_vb_365: None | Unset | UUID = UNSET
    name: None | str | Unset = UNSET
    vb_365_server_id: int | None | Unset = UNSET
    folder: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    account_uid: None | Unset | UUID = UNSET
    size_limit_enabled: bool | None | Unset = UNSET
    size_limit_bytes: int | None | Unset = UNSET
    used_space_bytes: int | None | Unset = UNSET
    free_space_bytes: int | None | Unset = UNSET
    type_: Vb365ObjectStorageRepositoryType | Unset = UNSET
    glacier_deep_archive_enabled: bool | None | Unset = UNSET
    ia_storage_class_enabled: bool | None | Unset = UNSET
    use_archiver_appliance: bool | None | Unset = UNSET
    amazon_bucket_s3_compatible_name: None | str | Unset = UNSET
    amazon_bucket_s3_compatible_custom_region_id: None | str | Unset = UNSET
    amazon_bucket_s3_aws_name: None | str | Unset = UNSET
    amazon_bucket_s3_aws_region_type: Vb365AwsRegionType | Unset = UNSET
    amazon_bucket_s3_aws_region_name: None | str | Unset = UNSET
    amazon_bucket_s3_aws_region_id: None | str | Unset = UNSET
    azure_container_name: None | str | Unset = UNSET
    azure_container_region_type: Vb365AwsRegionType | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        object_storage_repository_id = self.object_storage_repository_id

        object_storage_repository_uid_in_vb_365: None | str | Unset
        if isinstance(self.object_storage_repository_uid_in_vb_365, Unset):
            object_storage_repository_uid_in_vb_365 = UNSET
        elif isinstance(self.object_storage_repository_uid_in_vb_365, UUID):
            object_storage_repository_uid_in_vb_365 = str(self.object_storage_repository_uid_in_vb_365)
        else:
            object_storage_repository_uid_in_vb_365 = self.object_storage_repository_uid_in_vb_365

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        vb_365_server_id: int | None | Unset
        if isinstance(self.vb_365_server_id, Unset):
            vb_365_server_id = UNSET
        else:
            vb_365_server_id = self.vb_365_server_id

        folder: None | str | Unset
        if isinstance(self.folder, Unset):
            folder = UNSET
        else:
            folder = self.folder

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        account_uid: None | str | Unset
        if isinstance(self.account_uid, Unset):
            account_uid = UNSET
        elif isinstance(self.account_uid, UUID):
            account_uid = str(self.account_uid)
        else:
            account_uid = self.account_uid

        size_limit_enabled: bool | None | Unset
        if isinstance(self.size_limit_enabled, Unset):
            size_limit_enabled = UNSET
        else:
            size_limit_enabled = self.size_limit_enabled

        size_limit_bytes: int | None | Unset
        if isinstance(self.size_limit_bytes, Unset):
            size_limit_bytes = UNSET
        else:
            size_limit_bytes = self.size_limit_bytes

        used_space_bytes: int | None | Unset
        if isinstance(self.used_space_bytes, Unset):
            used_space_bytes = UNSET
        else:
            used_space_bytes = self.used_space_bytes

        free_space_bytes: int | None | Unset
        if isinstance(self.free_space_bytes, Unset):
            free_space_bytes = UNSET
        else:
            free_space_bytes = self.free_space_bytes

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        glacier_deep_archive_enabled: bool | None | Unset
        if isinstance(self.glacier_deep_archive_enabled, Unset):
            glacier_deep_archive_enabled = UNSET
        else:
            glacier_deep_archive_enabled = self.glacier_deep_archive_enabled

        ia_storage_class_enabled: bool | None | Unset
        if isinstance(self.ia_storage_class_enabled, Unset):
            ia_storage_class_enabled = UNSET
        else:
            ia_storage_class_enabled = self.ia_storage_class_enabled

        use_archiver_appliance: bool | None | Unset
        if isinstance(self.use_archiver_appliance, Unset):
            use_archiver_appliance = UNSET
        else:
            use_archiver_appliance = self.use_archiver_appliance

        amazon_bucket_s3_compatible_name: None | str | Unset
        if isinstance(self.amazon_bucket_s3_compatible_name, Unset):
            amazon_bucket_s3_compatible_name = UNSET
        else:
            amazon_bucket_s3_compatible_name = self.amazon_bucket_s3_compatible_name

        amazon_bucket_s3_compatible_custom_region_id: None | str | Unset
        if isinstance(self.amazon_bucket_s3_compatible_custom_region_id, Unset):
            amazon_bucket_s3_compatible_custom_region_id = UNSET
        else:
            amazon_bucket_s3_compatible_custom_region_id = self.amazon_bucket_s3_compatible_custom_region_id

        amazon_bucket_s3_aws_name: None | str | Unset
        if isinstance(self.amazon_bucket_s3_aws_name, Unset):
            amazon_bucket_s3_aws_name = UNSET
        else:
            amazon_bucket_s3_aws_name = self.amazon_bucket_s3_aws_name

        amazon_bucket_s3_aws_region_type: str | Unset = UNSET
        if not isinstance(self.amazon_bucket_s3_aws_region_type, Unset):
            amazon_bucket_s3_aws_region_type = self.amazon_bucket_s3_aws_region_type.value

        amazon_bucket_s3_aws_region_name: None | str | Unset
        if isinstance(self.amazon_bucket_s3_aws_region_name, Unset):
            amazon_bucket_s3_aws_region_name = UNSET
        else:
            amazon_bucket_s3_aws_region_name = self.amazon_bucket_s3_aws_region_name

        amazon_bucket_s3_aws_region_id: None | str | Unset
        if isinstance(self.amazon_bucket_s3_aws_region_id, Unset):
            amazon_bucket_s3_aws_region_id = UNSET
        else:
            amazon_bucket_s3_aws_region_id = self.amazon_bucket_s3_aws_region_id

        azure_container_name: None | str | Unset
        if isinstance(self.azure_container_name, Unset):
            azure_container_name = UNSET
        else:
            azure_container_name = self.azure_container_name

        azure_container_region_type: str | Unset = UNSET
        if not isinstance(self.azure_container_region_type, Unset):
            azure_container_region_type = self.azure_container_region_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if object_storage_repository_id is not UNSET:
            field_dict["objectStorageRepositoryId"] = object_storage_repository_id
        if object_storage_repository_uid_in_vb_365 is not UNSET:
            field_dict["objectStorageRepositoryUidInVb365"] = object_storage_repository_uid_in_vb_365
        if name is not UNSET:
            field_dict["name"] = name
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id
        if folder is not UNSET:
            field_dict["folder"] = folder
        if description is not UNSET:
            field_dict["description"] = description
        if account_uid is not UNSET:
            field_dict["accountUid"] = account_uid
        if size_limit_enabled is not UNSET:
            field_dict["sizeLimitEnabled"] = size_limit_enabled
        if size_limit_bytes is not UNSET:
            field_dict["sizeLimitBytes"] = size_limit_bytes
        if used_space_bytes is not UNSET:
            field_dict["usedSpaceBytes"] = used_space_bytes
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes
        if type_ is not UNSET:
            field_dict["type"] = type_
        if glacier_deep_archive_enabled is not UNSET:
            field_dict["glacierDeepArchiveEnabled"] = glacier_deep_archive_enabled
        if ia_storage_class_enabled is not UNSET:
            field_dict["iaStorageClassEnabled"] = ia_storage_class_enabled
        if use_archiver_appliance is not UNSET:
            field_dict["useArchiverAppliance"] = use_archiver_appliance
        if amazon_bucket_s3_compatible_name is not UNSET:
            field_dict["amazonBucketS3CompatibleName"] = amazon_bucket_s3_compatible_name
        if amazon_bucket_s3_compatible_custom_region_id is not UNSET:
            field_dict["amazonBucketS3CompatibleCustomRegionId"] = amazon_bucket_s3_compatible_custom_region_id
        if amazon_bucket_s3_aws_name is not UNSET:
            field_dict["amazonBucketS3AwsName"] = amazon_bucket_s3_aws_name
        if amazon_bucket_s3_aws_region_type is not UNSET:
            field_dict["amazonBucketS3AwsRegionType"] = amazon_bucket_s3_aws_region_type
        if amazon_bucket_s3_aws_region_name is not UNSET:
            field_dict["amazonBucketS3AwsRegionName"] = amazon_bucket_s3_aws_region_name
        if amazon_bucket_s3_aws_region_id is not UNSET:
            field_dict["amazonBucketS3AwsRegionId"] = amazon_bucket_s3_aws_region_id
        if azure_container_name is not UNSET:
            field_dict["azureContainerName"] = azure_container_name
        if azure_container_region_type is not UNSET:
            field_dict["azureContainerRegionType"] = azure_container_region_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        object_storage_repository_id = d.pop("objectStorageRepositoryId", UNSET)

        def _parse_object_storage_repository_uid_in_vb_365(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                object_storage_repository_uid_in_vb_365_type_0 = UUID(data)

                return object_storage_repository_uid_in_vb_365_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        object_storage_repository_uid_in_vb_365 = _parse_object_storage_repository_uid_in_vb_365(
            d.pop("objectStorageRepositoryUidInVb365", UNSET)
        )

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_vb_365_server_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vb_365_server_id = _parse_vb_365_server_id(d.pop("vb365ServerId", UNSET))

        def _parse_folder(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        folder = _parse_folder(d.pop("folder", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_account_uid(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                account_uid_type_0 = UUID(data)

                return account_uid_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        account_uid = _parse_account_uid(d.pop("accountUid", UNSET))

        def _parse_size_limit_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        size_limit_enabled = _parse_size_limit_enabled(d.pop("sizeLimitEnabled", UNSET))

        def _parse_size_limit_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        size_limit_bytes = _parse_size_limit_bytes(d.pop("sizeLimitBytes", UNSET))

        def _parse_used_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used_space_bytes = _parse_used_space_bytes(d.pop("usedSpaceBytes", UNSET))

        def _parse_free_space_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        free_space_bytes = _parse_free_space_bytes(d.pop("freeSpaceBytes", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Vb365ObjectStorageRepositoryType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = Vb365ObjectStorageRepositoryType(_type_)

        def _parse_glacier_deep_archive_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        glacier_deep_archive_enabled = _parse_glacier_deep_archive_enabled(d.pop("glacierDeepArchiveEnabled", UNSET))

        def _parse_ia_storage_class_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        ia_storage_class_enabled = _parse_ia_storage_class_enabled(d.pop("iaStorageClassEnabled", UNSET))

        def _parse_use_archiver_appliance(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        use_archiver_appliance = _parse_use_archiver_appliance(d.pop("useArchiverAppliance", UNSET))

        def _parse_amazon_bucket_s3_compatible_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amazon_bucket_s3_compatible_name = _parse_amazon_bucket_s3_compatible_name(
            d.pop("amazonBucketS3CompatibleName", UNSET)
        )

        def _parse_amazon_bucket_s3_compatible_custom_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amazon_bucket_s3_compatible_custom_region_id = _parse_amazon_bucket_s3_compatible_custom_region_id(
            d.pop("amazonBucketS3CompatibleCustomRegionId", UNSET)
        )

        def _parse_amazon_bucket_s3_aws_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amazon_bucket_s3_aws_name = _parse_amazon_bucket_s3_aws_name(d.pop("amazonBucketS3AwsName", UNSET))

        _amazon_bucket_s3_aws_region_type = d.pop("amazonBucketS3AwsRegionType", UNSET)
        amazon_bucket_s3_aws_region_type: Vb365AwsRegionType | Unset
        if isinstance(_amazon_bucket_s3_aws_region_type, Unset):
            amazon_bucket_s3_aws_region_type = UNSET
        else:
            amazon_bucket_s3_aws_region_type = Vb365AwsRegionType(_amazon_bucket_s3_aws_region_type)

        def _parse_amazon_bucket_s3_aws_region_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amazon_bucket_s3_aws_region_name = _parse_amazon_bucket_s3_aws_region_name(
            d.pop("amazonBucketS3AwsRegionName", UNSET)
        )

        def _parse_amazon_bucket_s3_aws_region_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amazon_bucket_s3_aws_region_id = _parse_amazon_bucket_s3_aws_region_id(
            d.pop("amazonBucketS3AwsRegionId", UNSET)
        )

        def _parse_azure_container_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        azure_container_name = _parse_azure_container_name(d.pop("azureContainerName", UNSET))

        _azure_container_region_type = d.pop("azureContainerRegionType", UNSET)
        azure_container_region_type: Vb365AwsRegionType | Unset
        if isinstance(_azure_container_region_type, Unset):
            azure_container_region_type = UNSET
        else:
            azure_container_region_type = Vb365AwsRegionType(_azure_container_region_type)

        vb_365_object_storage_repository_info = cls(
            object_storage_repository_id=object_storage_repository_id,
            object_storage_repository_uid_in_vb_365=object_storage_repository_uid_in_vb_365,
            name=name,
            vb_365_server_id=vb_365_server_id,
            folder=folder,
            description=description,
            account_uid=account_uid,
            size_limit_enabled=size_limit_enabled,
            size_limit_bytes=size_limit_bytes,
            used_space_bytes=used_space_bytes,
            free_space_bytes=free_space_bytes,
            type_=type_,
            glacier_deep_archive_enabled=glacier_deep_archive_enabled,
            ia_storage_class_enabled=ia_storage_class_enabled,
            use_archiver_appliance=use_archiver_appliance,
            amazon_bucket_s3_compatible_name=amazon_bucket_s3_compatible_name,
            amazon_bucket_s3_compatible_custom_region_id=amazon_bucket_s3_compatible_custom_region_id,
            amazon_bucket_s3_aws_name=amazon_bucket_s3_aws_name,
            amazon_bucket_s3_aws_region_type=amazon_bucket_s3_aws_region_type,
            amazon_bucket_s3_aws_region_name=amazon_bucket_s3_aws_region_name,
            amazon_bucket_s3_aws_region_id=amazon_bucket_s3_aws_region_id,
            azure_container_name=azure_container_name,
            azure_container_region_type=azure_container_region_type,
        )

        return vb_365_object_storage_repository_info
