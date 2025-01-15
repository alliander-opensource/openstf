# SPDX-FileCopyrightText: 2017-2023 Contributors to the OpenSTEF project <korte.termijn.prognoses@alliander.com> # noqa E501>
#
# SPDX-License-Identifier: MPL-2.0
import unittest
from test.unit.utils.base import BaseTestCase

from openstef.feature_engineering.lag_features import extract_lag_features


class TestGeneralExtractMinuteFeatures(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.feature_names = [
            "day-ahead-electricity-price",
            "clouds",
            "radiation",
            "temp",
            "winddeg",
            "windspeed",
            "pressure",
            "humidity",
            "rain",
            "mxlD",
            "snowDepth",
            "clearSky_ulf",
            "clearSky_dlf",
            "ssrunoff",
            "windspeed_100m",
            "sjv_E1A",
            "sjv_E1B",
            "sjv_E1C",
            "sjv_E2A",
            "sjv_E2B",
            "sjv_E3A",
            "sjv_E3B",
            "sjv_E3C",
            "sjv_E3D",
            "sjv_E4A",
            "T-900min",
            "T-780min",
            "T-15min",
            "T-1425min",
            "T-660min",
            "T-540min",
            "T-30min",
            "T-420min",
            "T-1320min",
            "T-300min",
            "T-45min",
            "T-1200min",
            "T-2865min",
            "T-180min",
            "T-1080min",
            "T-60min",
            "T-960min",
            "T-840min",
            "T-720min",
            "T-600min",
            "T-480min",
            "T-1380min",
            "T-360min",
            "T-1260min",
            "T-240min",
            "T-1140min",
            "T-120min",
            "T-1020min",
            "T-1d",
            "T-2d",
            "T-3d",
            "T-4d",
            "T-5d",
            "T-6d",
            "T-7d",
            "T-8d",
            "T-9d",
            "T-10d",
            "T-11d",
            "T-12d",
            "T-13d",
            "T-14d",
            "IsWeekendDay",
            "IsWeekDay",
            "IsMonday",
            "IsTuesday",
            "IsWednesday",
            "IsThursday",
            "IsFriday",
            "IsSaturday",
            "IsSunday",
            "Month",
            "Quarter",
            "IsChristmas",
            "Is00Hour",
            "Is01Hour",
            "Is02Hour",
            "Is03Hour",
            "Is04Hour",
            "Is05Hour",
            "Is06Hour",
            "Is07Hour",
            "Is08Hour",
            "Is09Hour",
            "Is10Hour",
            "Is11Hour",
            "Is12Hour",
            "Is13Hour",
            "Is14Hour",
            "Is15Hour",
            "Is16Hour",
            "Is17Hour",
            "Is18Hour",
            "Is19Hour",
            "Is20Hour",
            "Is21Hour",
            "Is22Hour",
            "Is23Hour",
            "windspeed_100mExtrapolated",
            "windPowerFit_extrapolated",
            "windpowerFit_harm_arome",
            "saturation_pressure",
            "vapour_pressure",
            "dewpoint",
            "air_density",
            "dtemp_quarter",
            "dtemp_hour",
            "dtemp_day",
            "dtemp_week",
            "dwindspeed_quarter",
            "dwindspeed_hour",
            "dwindspeed_day",
            "dwindspeed_week",
            "dwindspeed_100m_quarter",
            "dwindspeed_100m_hour",
            "dwindspeed_100m_day",
            "dwindspeed_100m_week",
            "dwinddeg_quarter",
            "dwinddeg_hour",
            "dwinddeg_day",
            "dwinddeg_week",
            "dpressure_quarter",
            "dpressure_hour",
            "dpressure_day",
            "dpressure_week",
            "dhumidity_quarter",
            "dhumidity_hour",
            "dhumidity_day",
            "dhumidity_week",
            "dair_density_quarter",
            "dair_density_hour",
            "dair_density_day",
            "dair_density_week",
        ]

    def test_extract_minute_features_short_horizon(self):
        testlist_minutes, testlist_days = extract_lag_features(
            self.feature_names, horizon=0.25
        )

        self.assertEqual(
            testlist_minutes,
            [
                900,
                780,
                15,
                1425,
                660,
                540,
                30,
                420,
                1320,
                300,
                45,
                1200,
                2865,
                180,
                1080,
                60,
                960,
                840,
                720,
                600,
                480,
                1380,
                360,
                1260,
                240,
                1140,
                120,
                1020,
            ],
        )
        self.assertEqual(testlist_days, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

    def test_extract_minute_features_long_horizon(self):
        testlist_minutes, testlist_days = extract_lag_features(
            self.feature_names, horizon=47
        )
        self.assertEqual(testlist_minutes, [2865])
        self.assertEqual(testlist_days, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])


if __name__ == "__main__":
    unittest.main()
