from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.vb_365_backup_repository_object_storage_type import Vb365BackupRepositoryObjectStorageType
from ..models.vb_365_backup_repository_retention_daily_type import Vb365BackupRepositoryRetentionDailyType
from ..models.vb_365_backup_repository_retention_frequency_type import Vb365BackupRepositoryRetentionFrequencyType
from ..models.vb_365_backup_repository_retention_period_type import Vb365BackupRepositoryRetentionPeriodType
from ..models.vb_365_backup_repository_retention_type import Vb365BackupRepositoryRetentionType
from ..models.vb_365_backup_repository_retention_yearly_period_type import (
    Vb365BackupRepositoryRetentionYearlyPeriodType,
)
from ..models.vb_365_day_of_week import Vb365DayOfWeek
from ..models.vb_365_monthly_day_number import Vb365MonthlyDayNumber
from ..types import UNSET, Unset

T = TypeVar("T", bound="Vb365BackupRepositoryInfo")


@_attrs_define
class Vb365BackupRepositoryInfo:
    """
    Attributes:
        backup_repository_id (Union[Unset, int]): ID assigned to a backup repository.
        backup_repository_uid_in_vb_365 (Union[None, UUID, Unset]): UID assigned to a backup repository in Veeam Backup
            for Microsoft 365.
        name (Union[None, Unset, str]): Name of a backup repository.
        vb_365_server_id (Union[None, Unset, int]): ID assigned to a Veeam Backup for Microsoft 365 server.
        is_out_of_sync (Union[None, Unset, bool]): Indicates whether a backup repository is not synchronized with an
            object storage.
        capacity_bytes (Union[None, Unset, int]): Storage capacity of a backup repository, in bytes.
        free_space_bytes (Union[None, Unset, int]): Available space on a backup repository, in bytes.
        description (Union[None, Unset, str]): Description of a backup repository.
        path (Union[None, Unset, str]): Path to a directory where backups are stored.
        retention_type (Union[Unset, Vb365BackupRepositoryRetentionType]):
        retention_period_type (Union[Unset, Vb365BackupRepositoryRetentionPeriodType]):
        retention_daily_period (Union[None, Unset, int]): Daily retention period, in days.
        retention_monthly_period (Union[None, Unset, int]): Monthly retention period, in months.
        retention_yearly_period (Union[Unset, Vb365BackupRepositoryRetentionYearlyPeriodType]):
        retention_frequency_type (Union[Unset, Vb365BackupRepositoryRetentionFrequencyType]):
        retention_daily_type (Union[Unset, Vb365BackupRepositoryRetentionDailyType]):
        retention_monthly_day_number (Union[Unset, Vb365MonthlyDayNumber]):
        retention_monthly_day_of_week (Union[Unset, Vb365DayOfWeek]):
        proxy_id (Union[None, Unset, int]): ID assigned to a backup proxy server.
        object_storage_id (Union[None, Unset, int]): ID assigned to an object storage repository.
        object_storage_type (Union[Unset, Vb365BackupRepositoryObjectStorageType]):
        object_storage_cache_path (Union[None, Unset, str]): Object storage cache path.
        is_long_term (Union[None, Unset, bool]): Indicates whether a backup repository is extended with an archive
            object storage.
        retention_daily_time (Union[None, Unset, int]): Daily retention time, in seconds.
        retention_monthly_time (Union[None, Unset, int]): Monthly retention time, in seconds.
    """

    backup_repository_id: Union[Unset, int] = UNSET
    backup_repository_uid_in_vb_365: Union[None, UUID, Unset] = UNSET
    name: Union[None, Unset, str] = UNSET
    vb_365_server_id: Union[None, Unset, int] = UNSET
    is_out_of_sync: Union[None, Unset, bool] = UNSET
    capacity_bytes: Union[None, Unset, int] = UNSET
    free_space_bytes: Union[None, Unset, int] = UNSET
    description: Union[None, Unset, str] = UNSET
    path: Union[None, Unset, str] = UNSET
    retention_type: Union[Unset, Vb365BackupRepositoryRetentionType] = UNSET
    retention_period_type: Union[Unset, Vb365BackupRepositoryRetentionPeriodType] = UNSET
    retention_daily_period: Union[None, Unset, int] = UNSET
    retention_monthly_period: Union[None, Unset, int] = UNSET
    retention_yearly_period: Union[Unset, Vb365BackupRepositoryRetentionYearlyPeriodType] = UNSET
    retention_frequency_type: Union[Unset, Vb365BackupRepositoryRetentionFrequencyType] = UNSET
    retention_daily_type: Union[Unset, Vb365BackupRepositoryRetentionDailyType] = UNSET
    retention_monthly_day_number: Union[Unset, Vb365MonthlyDayNumber] = UNSET
    retention_monthly_day_of_week: Union[Unset, Vb365DayOfWeek] = UNSET
    proxy_id: Union[None, Unset, int] = UNSET
    object_storage_id: Union[None, Unset, int] = UNSET
    object_storage_type: Union[Unset, Vb365BackupRepositoryObjectStorageType] = UNSET
    object_storage_cache_path: Union[None, Unset, str] = UNSET
    is_long_term: Union[None, Unset, bool] = UNSET
    retention_daily_time: Union[None, Unset, int] = UNSET
    retention_monthly_time: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        backup_repository_id = self.backup_repository_id

        backup_repository_uid_in_vb_365: Union[None, Unset, str]
        if isinstance(self.backup_repository_uid_in_vb_365, Unset):
            backup_repository_uid_in_vb_365 = UNSET
        elif isinstance(self.backup_repository_uid_in_vb_365, UUID):
            backup_repository_uid_in_vb_365 = str(self.backup_repository_uid_in_vb_365)
        else:
            backup_repository_uid_in_vb_365 = self.backup_repository_uid_in_vb_365

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        vb_365_server_id: Union[None, Unset, int]
        if isinstance(self.vb_365_server_id, Unset):
            vb_365_server_id = UNSET
        else:
            vb_365_server_id = self.vb_365_server_id

        is_out_of_sync: Union[None, Unset, bool]
        if isinstance(self.is_out_of_sync, Unset):
            is_out_of_sync = UNSET
        else:
            is_out_of_sync = self.is_out_of_sync

        capacity_bytes: Union[None, Unset, int]
        if isinstance(self.capacity_bytes, Unset):
            capacity_bytes = UNSET
        else:
            capacity_bytes = self.capacity_bytes

        free_space_bytes: Union[None, Unset, int]
        if isinstance(self.free_space_bytes, Unset):
            free_space_bytes = UNSET
        else:
            free_space_bytes = self.free_space_bytes

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        path: Union[None, Unset, str]
        if isinstance(self.path, Unset):
            path = UNSET
        else:
            path = self.path

        retention_type: Union[Unset, str] = UNSET
        if not isinstance(self.retention_type, Unset):
            retention_type = self.retention_type.value

        retention_period_type: Union[Unset, str] = UNSET
        if not isinstance(self.retention_period_type, Unset):
            retention_period_type = self.retention_period_type.value

        retention_daily_period: Union[None, Unset, int]
        if isinstance(self.retention_daily_period, Unset):
            retention_daily_period = UNSET
        else:
            retention_daily_period = self.retention_daily_period

        retention_monthly_period: Union[None, Unset, int]
        if isinstance(self.retention_monthly_period, Unset):
            retention_monthly_period = UNSET
        else:
            retention_monthly_period = self.retention_monthly_period

        retention_yearly_period: Union[Unset, str] = UNSET
        if not isinstance(self.retention_yearly_period, Unset):
            retention_yearly_period = self.retention_yearly_period.value

        retention_frequency_type: Union[Unset, str] = UNSET
        if not isinstance(self.retention_frequency_type, Unset):
            retention_frequency_type = self.retention_frequency_type.value

        retention_daily_type: Union[Unset, str] = UNSET
        if not isinstance(self.retention_daily_type, Unset):
            retention_daily_type = self.retention_daily_type.value

        retention_monthly_day_number: Union[Unset, str] = UNSET
        if not isinstance(self.retention_monthly_day_number, Unset):
            retention_monthly_day_number = self.retention_monthly_day_number.value

        retention_monthly_day_of_week: Union[Unset, str] = UNSET
        if not isinstance(self.retention_monthly_day_of_week, Unset):
            retention_monthly_day_of_week = self.retention_monthly_day_of_week.value

        proxy_id: Union[None, Unset, int]
        if isinstance(self.proxy_id, Unset):
            proxy_id = UNSET
        else:
            proxy_id = self.proxy_id

        object_storage_id: Union[None, Unset, int]
        if isinstance(self.object_storage_id, Unset):
            object_storage_id = UNSET
        else:
            object_storage_id = self.object_storage_id

        object_storage_type: Union[Unset, str] = UNSET
        if not isinstance(self.object_storage_type, Unset):
            object_storage_type = self.object_storage_type.value

        object_storage_cache_path: Union[None, Unset, str]
        if isinstance(self.object_storage_cache_path, Unset):
            object_storage_cache_path = UNSET
        else:
            object_storage_cache_path = self.object_storage_cache_path

        is_long_term: Union[None, Unset, bool]
        if isinstance(self.is_long_term, Unset):
            is_long_term = UNSET
        else:
            is_long_term = self.is_long_term

        retention_daily_time: Union[None, Unset, int]
        if isinstance(self.retention_daily_time, Unset):
            retention_daily_time = UNSET
        else:
            retention_daily_time = self.retention_daily_time

        retention_monthly_time: Union[None, Unset, int]
        if isinstance(self.retention_monthly_time, Unset):
            retention_monthly_time = UNSET
        else:
            retention_monthly_time = self.retention_monthly_time

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if backup_repository_id is not UNSET:
            field_dict["backupRepositoryId"] = backup_repository_id
        if backup_repository_uid_in_vb_365 is not UNSET:
            field_dict["backupRepositoryUidInVb365"] = backup_repository_uid_in_vb_365
        if name is not UNSET:
            field_dict["name"] = name
        if vb_365_server_id is not UNSET:
            field_dict["vb365ServerId"] = vb_365_server_id
        if is_out_of_sync is not UNSET:
            field_dict["isOutOfSync"] = is_out_of_sync
        if capacity_bytes is not UNSET:
            field_dict["capacityBytes"] = capacity_bytes
        if free_space_bytes is not UNSET:
            field_dict["freeSpaceBytes"] = free_space_bytes
        if description is not UNSET:
            field_dict["description"] = description
        if path is not UNSET:
            field_dict["path"] = path
        if retention_type is not UNSET:
            field_dict["retentionType"] = retention_type
        if retention_period_type is not UNSET:
            field_dict["retentionPeriodType"] = retention_period_type
        if retention_daily_period is not UNSET:
            field_dict["retentionDailyPeriod"] = retention_daily_period
        if retention_monthly_period is not UNSET:
            field_dict["retentionMonthlyPeriod"] = retention_monthly_period
        if retention_yearly_period is not UNSET:
            field_dict["retentionYearlyPeriod"] = retention_yearly_period
        if retention_frequency_type is not UNSET:
            field_dict["retentionFrequencyType"] = retention_frequency_type
        if retention_daily_type is not UNSET:
            field_dict["retentionDailyType"] = retention_daily_type
        if retention_monthly_day_number is not UNSET:
            field_dict["retentionMonthlyDayNumber"] = retention_monthly_day_number
        if retention_monthly_day_of_week is not UNSET:
            field_dict["retentionMonthlyDayOfWeek"] = retention_monthly_day_of_week
        if proxy_id is not UNSET:
            field_dict["proxyId"] = proxy_id
        if object_storage_id is not UNSET:
            field_dict["objectStorageId"] = object_storage_id
        if object_storage_type is not UNSET:
            field_dict["objectStorageType"] = object_storage_type
        if object_storage_cache_path is not UNSET:
            field_dict["objectStorageCachePath"] = object_storage_cache_path
        if is_long_term is not UNSET:
            field_dict["isLongTerm"] = is_long_term
        if retention_daily_time is not UNSET:
            field_dict["retentionDailyTime"] = retention_daily_time
        if retention_monthly_time is not UNSET:
            field_dict["retentionMonthlyTime"] = retention_monthly_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        backup_repository_id = d.pop("backupRepositoryId", UNSET)

        def _parse_backup_repository_uid_in_vb_365(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                backup_repository_uid_in_vb_365_type_0 = UUID(data)

                return backup_repository_uid_in_vb_365_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        backup_repository_uid_in_vb_365 = _parse_backup_repository_uid_in_vb_365(
            d.pop("backupRepositoryUidInVb365", UNSET)
        )

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_vb_365_server_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        vb_365_server_id = _parse_vb_365_server_id(d.pop("vb365ServerId", UNSET))

        def _parse_is_out_of_sync(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_out_of_sync = _parse_is_out_of_sync(d.pop("isOutOfSync", UNSET))

        def _parse_capacity_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        capacity_bytes = _parse_capacity_bytes(d.pop("capacityBytes", UNSET))

        def _parse_free_space_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        free_space_bytes = _parse_free_space_bytes(d.pop("freeSpaceBytes", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        path = _parse_path(d.pop("path", UNSET))

        _retention_type = d.pop("retentionType", UNSET)
        retention_type: Union[Unset, Vb365BackupRepositoryRetentionType]
        if isinstance(_retention_type, Unset):
            retention_type = UNSET
        else:
            retention_type = Vb365BackupRepositoryRetentionType(_retention_type)

        _retention_period_type = d.pop("retentionPeriodType", UNSET)
        retention_period_type: Union[Unset, Vb365BackupRepositoryRetentionPeriodType]
        if isinstance(_retention_period_type, Unset):
            retention_period_type = UNSET
        else:
            retention_period_type = Vb365BackupRepositoryRetentionPeriodType(_retention_period_type)

        def _parse_retention_daily_period(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        retention_daily_period = _parse_retention_daily_period(d.pop("retentionDailyPeriod", UNSET))

        def _parse_retention_monthly_period(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        retention_monthly_period = _parse_retention_monthly_period(d.pop("retentionMonthlyPeriod", UNSET))

        _retention_yearly_period = d.pop("retentionYearlyPeriod", UNSET)
        retention_yearly_period: Union[Unset, Vb365BackupRepositoryRetentionYearlyPeriodType]
        if isinstance(_retention_yearly_period, Unset):
            retention_yearly_period = UNSET
        else:
            retention_yearly_period = Vb365BackupRepositoryRetentionYearlyPeriodType(_retention_yearly_period)

        _retention_frequency_type = d.pop("retentionFrequencyType", UNSET)
        retention_frequency_type: Union[Unset, Vb365BackupRepositoryRetentionFrequencyType]
        if isinstance(_retention_frequency_type, Unset):
            retention_frequency_type = UNSET
        else:
            retention_frequency_type = Vb365BackupRepositoryRetentionFrequencyType(_retention_frequency_type)

        _retention_daily_type = d.pop("retentionDailyType", UNSET)
        retention_daily_type: Union[Unset, Vb365BackupRepositoryRetentionDailyType]
        if isinstance(_retention_daily_type, Unset):
            retention_daily_type = UNSET
        else:
            retention_daily_type = Vb365BackupRepositoryRetentionDailyType(_retention_daily_type)

        _retention_monthly_day_number = d.pop("retentionMonthlyDayNumber", UNSET)
        retention_monthly_day_number: Union[Unset, Vb365MonthlyDayNumber]
        if isinstance(_retention_monthly_day_number, Unset):
            retention_monthly_day_number = UNSET
        else:
            retention_monthly_day_number = Vb365MonthlyDayNumber(_retention_monthly_day_number)

        _retention_monthly_day_of_week = d.pop("retentionMonthlyDayOfWeek", UNSET)
        retention_monthly_day_of_week: Union[Unset, Vb365DayOfWeek]
        if isinstance(_retention_monthly_day_of_week, Unset):
            retention_monthly_day_of_week = UNSET
        else:
            retention_monthly_day_of_week = Vb365DayOfWeek(_retention_monthly_day_of_week)

        def _parse_proxy_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        proxy_id = _parse_proxy_id(d.pop("proxyId", UNSET))

        def _parse_object_storage_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        object_storage_id = _parse_object_storage_id(d.pop("objectStorageId", UNSET))

        _object_storage_type = d.pop("objectStorageType", UNSET)
        object_storage_type: Union[Unset, Vb365BackupRepositoryObjectStorageType]
        if isinstance(_object_storage_type, Unset):
            object_storage_type = UNSET
        else:
            object_storage_type = Vb365BackupRepositoryObjectStorageType(_object_storage_type)

        def _parse_object_storage_cache_path(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        object_storage_cache_path = _parse_object_storage_cache_path(d.pop("objectStorageCachePath", UNSET))

        def _parse_is_long_term(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_long_term = _parse_is_long_term(d.pop("isLongTerm", UNSET))

        def _parse_retention_daily_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        retention_daily_time = _parse_retention_daily_time(d.pop("retentionDailyTime", UNSET))

        def _parse_retention_monthly_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        retention_monthly_time = _parse_retention_monthly_time(d.pop("retentionMonthlyTime", UNSET))

        vb_365_backup_repository_info = cls(
            backup_repository_id=backup_repository_id,
            backup_repository_uid_in_vb_365=backup_repository_uid_in_vb_365,
            name=name,
            vb_365_server_id=vb_365_server_id,
            is_out_of_sync=is_out_of_sync,
            capacity_bytes=capacity_bytes,
            free_space_bytes=free_space_bytes,
            description=description,
            path=path,
            retention_type=retention_type,
            retention_period_type=retention_period_type,
            retention_daily_period=retention_daily_period,
            retention_monthly_period=retention_monthly_period,
            retention_yearly_period=retention_yearly_period,
            retention_frequency_type=retention_frequency_type,
            retention_daily_type=retention_daily_type,
            retention_monthly_day_number=retention_monthly_day_number,
            retention_monthly_day_of_week=retention_monthly_day_of_week,
            proxy_id=proxy_id,
            object_storage_id=object_storage_id,
            object_storage_type=object_storage_type,
            object_storage_cache_path=object_storage_cache_path,
            is_long_term=is_long_term,
            retention_daily_time=retention_daily_time,
            retention_monthly_time=retention_monthly_time,
        )

        return vb_365_backup_repository_info
