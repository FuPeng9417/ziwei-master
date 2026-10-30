"""Engine entry points reserved for future verified implementations."""

from .models import BirthInput, ConventionProfile, TimeBasis


def build_chart(
    birth: BirthInput,
    *,
    time_basis: TimeBasis,
    conventions: ConventionProfile,
) -> None:
    """TODO: implement only after conventions and independent fixtures are approved."""
    raise NotImplementedError(
        "Chart calculation is not implemented or verified in this scaffold."
    )
