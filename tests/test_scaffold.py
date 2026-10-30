"""Regression checks for the implemented project scaffolding only."""

import unittest
from dataclasses import FrozenInstanceError
from datetime import datetime

from ziwei_master.engine import build_chart
from ziwei_master.models import BirthInput, ConventionProfile, School, TimeBasis


class ModelScaffoldTests(unittest.TestCase):
    def test_time_basis_values_are_explicit(self):
        self.assertEqual(TimeBasis.CIVIL.value, "civil")
        self.assertEqual(TimeBasis.TRUE_SOLAR.value, "true_solar")

    def test_school_values_are_separate(self):
        self.assertEqual(
            {school.value for school in School},
            {"san_he", "fei_xing", "qin_tian_si_hua", "he_luo"},
        )

    def test_birth_input_preserves_supplied_values(self):
        birth = BirthInput(
            local_datetime=datetime(2000, 1, 2, 3, 4),
            timezone_name="Asia/Shanghai",
            latitude=31.23,
            longitude=121.47,
            source_note="synthetic test input",
        )
        self.assertEqual(birth.timezone_name, "Asia/Shanghai")
        self.assertEqual(birth.longitude, 121.47)
        with self.assertRaises(FrozenInstanceError):
            birth.timezone_name = "UTC"

    def test_convention_profile_is_versioned_and_immutable(self):
        profile = ConventionProfile(name="placeholder", version="0")
        self.assertEqual((profile.name, profile.version), ("placeholder", "0"))
        with self.assertRaises(FrozenInstanceError):
            profile.version = "1"


class EngineScaffoldTests(unittest.TestCase):
    def test_chart_engine_fails_explicitly_until_verified(self):
        birth = BirthInput(
            local_datetime=datetime(2000, 1, 2, 3, 4),
            timezone_name="Asia/Shanghai",
        )
        profile = ConventionProfile(name="placeholder", version="0")
        with self.assertRaisesRegex(NotImplementedError, "not implemented or verified"):
            build_chart(birth, time_basis=TimeBasis.CIVIL, conventions=profile)


if __name__ == "__main__":
    unittest.main()

