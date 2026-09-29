from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VmDatastoreUsage")


@_attrs_define
class VmDatastoreUsage:
    """
    Attributes:
        datastore_mo_ref (Union[None, Unset, str]): MoRef ID assigned to a datastore.
        commited_bytes (Union[Unset, int]): Datastore storage space that is used by a VM, in bytes.
        uncommited_bytes (Union[Unset, int]): Datastore storage space that can be used by a VM, in bytes.
        unshared_bytes (Union[Unset, int]): Datastore storage space that is used by a VM and is not shared with other
            VMs, in bytes.
    """

    datastore_mo_ref: Union[None, Unset, str] = UNSET
    commited_bytes: Union[Unset, int] = UNSET
    uncommited_bytes: Union[Unset, int] = UNSET
    unshared_bytes: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        datastore_mo_ref: Union[None, Unset, str]
        if isinstance(self.datastore_mo_ref, Unset):
            datastore_mo_ref = UNSET
        else:
            datastore_mo_ref = self.datastore_mo_ref

        commited_bytes = self.commited_bytes

        uncommited_bytes = self.uncommited_bytes

        unshared_bytes = self.unshared_bytes

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if datastore_mo_ref is not UNSET:
            field_dict["datastoreMoRef"] = datastore_mo_ref
        if commited_bytes is not UNSET:
            field_dict["commitedBytes"] = commited_bytes
        if uncommited_bytes is not UNSET:
            field_dict["uncommitedBytes"] = uncommited_bytes
        if unshared_bytes is not UNSET:
            field_dict["unsharedBytes"] = unshared_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_datastore_mo_ref(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        datastore_mo_ref = _parse_datastore_mo_ref(d.pop("datastoreMoRef", UNSET))

        commited_bytes = d.pop("commitedBytes", UNSET)

        uncommited_bytes = d.pop("uncommitedBytes", UNSET)

        unshared_bytes = d.pop("unsharedBytes", UNSET)

        vm_datastore_usage = cls(
            datastore_mo_ref=datastore_mo_ref,
            commited_bytes=commited_bytes,
            uncommited_bytes=uncommited_bytes,
            unshared_bytes=unshared_bytes,
        )

        return vm_datastore_usage
