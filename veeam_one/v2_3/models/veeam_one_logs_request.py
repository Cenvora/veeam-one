import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VeeamOneLogsRequest")


@_attrs_define
class VeeamOneLogsRequest:
    """
    Attributes:
        from_date (Union[None, Unset, datetime.datetime]): Start date and time of the period for which a log archive
            must be collected.
    """

    from_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from_date: Union[None, Unset, str]
        if isinstance(self.from_date, Unset):
            from_date = UNSET
        elif isinstance(self.from_date, datetime.datetime):
            from_date = self.from_date.isoformat()
        else:
            from_date = self.from_date

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if from_date is not UNSET:
            field_dict["fromDate"] = from_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_from_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_date_type_0 = isoparse(data)

                return from_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        from_date = _parse_from_date(d.pop("fromDate", UNSET))

        veeam_one_logs_request = cls(
            from_date=from_date,
        )

        return veeam_one_logs_request
