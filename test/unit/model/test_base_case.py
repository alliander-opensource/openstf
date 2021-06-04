from test.utils import BaseTestCase, TestData
import pytz
import pytest

import numpy as np
import pandas as pd

from datetime import datetime, timezone, timedelta

from openstf.model.basecase import BaseCaseModel

NOW = datetime.now(timezone.utc)


class TestBaseCaseForecast(BaseTestCase):
    def test_basecase_raises_value_error_too_early_start(self):
        # Test if ValueError is raised when forecast start is earlier than allowed
        forecast_input = TestData.load("reference_sets/307-test-data.csv")
        # Shift example data to match current time interval as code expects data
        # available relative to the current time.
        utc_now = (
            pd.Series(datetime.utcnow().replace(tzinfo=pytz.utc))
            .min()
            .round("15T")
            .to_pydatetime()
        )
        most_recent_date = forecast_input.index.max().round("15T").to_pydatetime()
        delta = utc_now - most_recent_date + timedelta(3)

        forecast_input.index = forecast_input.index.shift(delta, freq=1)

        with pytest.raises(ValueError):
            BaseCaseModel().predict(forecast_input)

    def test_basecase_raises_value_error_missing_features(self):
        # Test if ValueError is raised when T-7d or T-14 are not pressent.
        forecast_input = TestData.load("reference_sets/307-test-data.csv")
        # Shift example data to match current time interval as code expects data
        # available relative to the current time.
        utc_now = (
            pd.Series(datetime.utcnow().replace(tzinfo=pytz.utc))
            .min()
            .round("15T")
            .to_pydatetime()
        )
        most_recent_date = forecast_input.index.max().round("15T").to_pydatetime()
        delta = (
            utc_now - most_recent_date + timedelta(35)
        )  # This will make it pass the first input vallidation

        forecast_input.index = forecast_input.index.shift(delta, freq=1)
        with pytest.raises(ValueError):
            BaseCaseModel().predict(forecast_input)
