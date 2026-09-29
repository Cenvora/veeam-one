import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.failover_plan_state import FailoverPlanState
from ..types import UNSET, Unset

T = TypeVar("T", bound="FailoverPlanInfo")


@_attrs_define
class FailoverPlanInfo:
    """
    Attributes:
        failover_plan_uid (Union[None, UUID, Unset]): UID assigned to a failover plan in Veeam Backup & Replication.
        backup_server_id (Union[Unset, int]): ID assigned to a Veeam Backup & Replication server.
        status (Union[Unset, FailoverPlanState]):
        name (Union[None, Unset, str]): Name of a failover plan.
        description (Union[None, Unset, str]): Failover plan description.
        last_run (Union[None, Unset, datetime.datetime]): Date and time of the latest failover plan session.
    """

    failover_plan_uid: Union[None, UUID, Unset] = UNSET
    backup_server_id: Union[Unset, int] = UNSET
    status: Union[Unset, FailoverPlanState] = UNSET
    name: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    last_run: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        failover_plan_uid: Union[None, Unset, str]
        if isinstance(self.failover_plan_uid, Unset):
            failover_plan_uid = UNSET
        elif isinstance(self.failover_plan_uid, UUID):
            failover_plan_uid = str(self.failover_plan_uid)
        else:
            failover_plan_uid = self.failover_plan_uid

        backup_server_id = self.backup_server_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        last_run: Union[None, Unset, str]
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if failover_plan_uid is not UNSET:
            field_dict["failoverPlanUid"] = failover_plan_uid
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_failover_plan_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                failover_plan_uid_type_0 = UUID(data)

                return failover_plan_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        failover_plan_uid = _parse_failover_plan_uid(d.pop("failoverPlanUid", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, FailoverPlanState]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = FailoverPlanState(_status)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_last_run(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_run_type_0 = isoparse(data)

                return last_run_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_run = _parse_last_run(d.pop("lastRun", UNSET))

        failover_plan_info = cls(
            failover_plan_uid=failover_plan_uid,
            backup_server_id=backup_server_id,
            status=status,
            name=name,
            description=description,
            last_run=last_run,
        )

        return failover_plan_info
