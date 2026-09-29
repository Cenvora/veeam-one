from enum import StrEnum


class SessionsTaskTypes(StrEnum):
    AGGREGATEPROPERTIES = "AggregateProperties"
    BUSINESSVIEWDATA = "BusinessviewData"
    CAPACITYPLANNING = "CapacityPlanning"
    DATAADMINISTRATION = "DataAdministration"
    INDEXESUPGRADE = "IndexesUpgrade"
    SCHEDULEDASHBOARD = "ScheduleDashboard"
    SCHEDULEFOLDER = "ScheduleFolder"
    SCHEDULEREPORTING = "ScheduleReporting"

    def __str__(self) -> str:
        return str(self.value)
