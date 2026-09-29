from enum import Enum


class VeeamOneLicenseType(str, Enum):
    EVALUATION = "Evaluation"
    FREE = "Free"
    NFR = "Nfr"
    PERPETUAL = "Perpetual"
    RENTAL = "Rental"
    SUBSCRIPTION = "Subscription"
    TRIAL = "Trial"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
