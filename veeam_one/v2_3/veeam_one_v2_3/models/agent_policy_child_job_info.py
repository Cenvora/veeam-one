import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.backup_job_status import BackupJobStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentPolicyChildJobInfo")


@_attrs_define
class AgentPolicyChildJobInfo:
    """
    Attributes:
        child_job_uid (Union[None, UUID, Unset]): UID assigned to a job in Veeam Backup & Replication.
        name (Union[None, Unset, str]): Name of a job.
        agent_policy_uid (Union[None, UUID, Unset]): UID assigned to a parent Veeam backup agent policy in Veeam Backup
            & Replication.
        computer_name (Union[None, Unset, str]): Name of a computer protected by a job.
        protected_agent_uid (Union[None, UUID, Unset]): UID assigned to a Veeam backup agent installed on a protected
            computer.
        ip_addresses (Union[None, Unset, list[str]]): IP addresses of a protected computer.
        backup_server_id (Union[Unset, int]): ID assigned to a Veeam Backup & Replication server.
        status (Union[Unset, BackupJobStatus]):
        details (Union[None, Unset, list[str]]): Additional information on a job.
        last_run (Union[None, Unset, datetime.datetime]): Date and time of the latest job session.
        last_run_duration_sec (Union[None, Unset, int]): Duration of the latest job session, in seconds.
        avg_duration_sec (Union[None, Unset, int]): Average job session duration, in seconds.
        last_transferred_data_bytes (Union[None, Unset, int]): Amount of data transferred during the latest job session,
            in bytes.
    """

    child_job_uid: Union[None, UUID, Unset] = UNSET
    name: Union[None, Unset, str] = UNSET
    agent_policy_uid: Union[None, UUID, Unset] = UNSET
    computer_name: Union[None, Unset, str] = UNSET
    protected_agent_uid: Union[None, UUID, Unset] = UNSET
    ip_addresses: Union[None, Unset, list[str]] = UNSET
    backup_server_id: Union[Unset, int] = UNSET
    status: Union[Unset, BackupJobStatus] = UNSET
    details: Union[None, Unset, list[str]] = UNSET
    last_run: Union[None, Unset, datetime.datetime] = UNSET
    last_run_duration_sec: Union[None, Unset, int] = UNSET
    avg_duration_sec: Union[None, Unset, int] = UNSET
    last_transferred_data_bytes: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        child_job_uid: Union[None, Unset, str]
        if isinstance(self.child_job_uid, Unset):
            child_job_uid = UNSET
        elif isinstance(self.child_job_uid, UUID):
            child_job_uid = str(self.child_job_uid)
        else:
            child_job_uid = self.child_job_uid

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        agent_policy_uid: Union[None, Unset, str]
        if isinstance(self.agent_policy_uid, Unset):
            agent_policy_uid = UNSET
        elif isinstance(self.agent_policy_uid, UUID):
            agent_policy_uid = str(self.agent_policy_uid)
        else:
            agent_policy_uid = self.agent_policy_uid

        computer_name: Union[None, Unset, str]
        if isinstance(self.computer_name, Unset):
            computer_name = UNSET
        else:
            computer_name = self.computer_name

        protected_agent_uid: Union[None, Unset, str]
        if isinstance(self.protected_agent_uid, Unset):
            protected_agent_uid = UNSET
        elif isinstance(self.protected_agent_uid, UUID):
            protected_agent_uid = str(self.protected_agent_uid)
        else:
            protected_agent_uid = self.protected_agent_uid

        ip_addresses: Union[None, Unset, list[str]]
        if isinstance(self.ip_addresses, Unset):
            ip_addresses = UNSET
        elif isinstance(self.ip_addresses, list):
            ip_addresses = self.ip_addresses

        else:
            ip_addresses = self.ip_addresses

        backup_server_id = self.backup_server_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        details: Union[None, Unset, list[str]]
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, list):
            details = self.details

        else:
            details = self.details

        last_run: Union[None, Unset, str]
        if isinstance(self.last_run, Unset):
            last_run = UNSET
        elif isinstance(self.last_run, datetime.datetime):
            last_run = self.last_run.isoformat()
        else:
            last_run = self.last_run

        last_run_duration_sec: Union[None, Unset, int]
        if isinstance(self.last_run_duration_sec, Unset):
            last_run_duration_sec = UNSET
        else:
            last_run_duration_sec = self.last_run_duration_sec

        avg_duration_sec: Union[None, Unset, int]
        if isinstance(self.avg_duration_sec, Unset):
            avg_duration_sec = UNSET
        else:
            avg_duration_sec = self.avg_duration_sec

        last_transferred_data_bytes: Union[None, Unset, int]
        if isinstance(self.last_transferred_data_bytes, Unset):
            last_transferred_data_bytes = UNSET
        else:
            last_transferred_data_bytes = self.last_transferred_data_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if child_job_uid is not UNSET:
            field_dict["childJobUid"] = child_job_uid
        if name is not UNSET:
            field_dict["name"] = name
        if agent_policy_uid is not UNSET:
            field_dict["agentPolicyUid"] = agent_policy_uid
        if computer_name is not UNSET:
            field_dict["computerName"] = computer_name
        if protected_agent_uid is not UNSET:
            field_dict["protectedAgentUid"] = protected_agent_uid
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses
        if backup_server_id is not UNSET:
            field_dict["backupServerId"] = backup_server_id
        if status is not UNSET:
            field_dict["status"] = status
        if details is not UNSET:
            field_dict["details"] = details
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if last_run_duration_sec is not UNSET:
            field_dict["lastRunDurationSec"] = last_run_duration_sec
        if avg_duration_sec is not UNSET:
            field_dict["avgDurationSec"] = avg_duration_sec
        if last_transferred_data_bytes is not UNSET:
            field_dict["lastTransferredDataBytes"] = last_transferred_data_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_child_job_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                child_job_uid_type_0 = UUID(data)

                return child_job_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        child_job_uid = _parse_child_job_uid(d.pop("childJobUid", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_agent_policy_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_policy_uid_type_0 = UUID(data)

                return agent_policy_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        agent_policy_uid = _parse_agent_policy_uid(d.pop("agentPolicyUid", UNSET))

        def _parse_computer_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        computer_name = _parse_computer_name(d.pop("computerName", UNSET))

        def _parse_protected_agent_uid(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                protected_agent_uid_type_0 = UUID(data)

                return protected_agent_uid_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        protected_agent_uid = _parse_protected_agent_uid(d.pop("protectedAgentUid", UNSET))

        def _parse_ip_addresses(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ip_addresses_type_0 = cast(list[str], data)

                return ip_addresses_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        ip_addresses = _parse_ip_addresses(d.pop("ipAddresses", UNSET))

        backup_server_id = d.pop("backupServerId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BackupJobStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BackupJobStatus(_status)

        def _parse_details(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                details_type_0 = cast(list[str], data)

                return details_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        details = _parse_details(d.pop("details", UNSET))

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

        def _parse_last_run_duration_sec(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        last_run_duration_sec = _parse_last_run_duration_sec(d.pop("lastRunDurationSec", UNSET))

        def _parse_avg_duration_sec(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        avg_duration_sec = _parse_avg_duration_sec(d.pop("avgDurationSec", UNSET))

        def _parse_last_transferred_data_bytes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        last_transferred_data_bytes = _parse_last_transferred_data_bytes(d.pop("lastTransferredDataBytes", UNSET))

        agent_policy_child_job_info = cls(
            child_job_uid=child_job_uid,
            name=name,
            agent_policy_uid=agent_policy_uid,
            computer_name=computer_name,
            protected_agent_uid=protected_agent_uid,
            ip_addresses=ip_addresses,
            backup_server_id=backup_server_id,
            status=status,
            details=details,
            last_run=last_run,
            last_run_duration_sec=last_run_duration_sec,
            avg_duration_sec=avg_duration_sec,
            last_transferred_data_bytes=last_transferred_data_bytes,
        )

        return agent_policy_child_job_info
