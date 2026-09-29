from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

from ..models.async_task_state import AsyncTaskState
from ..types import UNSET, Unset

T = TypeVar("T", bound="AsyncTaskStatus")


@_attrs_define
class AsyncTaskStatus:
    """
    Attributes:
        id (UUID | Unset): UID assigned to an asynchronous task.
        state (AsyncTaskState | Unset):
        result (Any | Unset): Result of an asynchronous task.
    """

    id: UUID | Unset = UNSET
    state: AsyncTaskState | Unset = UNSET
    result: Any | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        state: str | Unset = UNSET
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
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        _state = d.pop("state", UNSET)
        state: AsyncTaskState | Unset
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
