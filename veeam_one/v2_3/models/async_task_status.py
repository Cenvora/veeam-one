from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.async_task_state import AsyncTaskState
from ..types import UNSET, Unset

T = TypeVar("T", bound="AsyncTaskStatus")


@_attrs_define
class AsyncTaskStatus:
    """
    Attributes:
        id (Union[Unset, UUID]): UID assigned to an asynchronous task.
        state (Union[Unset, AsyncTaskState]):
        result (Union[Unset, Any]): Result of an asynchronous task.
    """

    id: Union[Unset, UUID] = UNSET
    state: Union[Unset, AsyncTaskState] = UNSET
    result: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        result = self.result

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if state is not UNSET:
            field_dict["state"] = state
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: Union[Unset, UUID]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _state = d.pop("state", UNSET)
        state: Union[Unset, AsyncTaskState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = AsyncTaskState(_state)

        result = d.pop("result", UNSET)

        async_task_status = cls(
            id=id,
            state=state,
            result=result,
        )

        return async_task_status
