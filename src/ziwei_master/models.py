"""Initial data shapes only. These models do not perform chart calculations."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class TimeBasis(str, Enum):
    CIVIL = "civil"
    TRUE_SOLAR = "true_solar"


class School(str, Enum):
    SAN_HE = "san_he"
    FEI_XING = "fei_xing"
    QIN_TIAN_SI_HUA = "qin_tian_si_hua"
    HE_LUO = "he_luo"


@dataclass(frozen=True)
class BirthInput:
    """Raw supplied birth data; timezone and coordinates are not inferred."""

    local_datetime: datetime
    timezone_name: str
    latitude: float | None = None
    longitude: float | None = None
    source_note: str | None = None


@dataclass(frozen=True)
class ConventionProfile:
    """Name/version for explicit conventions, to be defined before calculation."""

    name: str
    version: str

