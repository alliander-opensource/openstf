# SPDX-FileCopyrightText: 2017-2022 Contributors to the OpenSTEF project <korte.termijn.prognoses@alliander.com> # noqa E501>
#
# SPDX-License-Identifier: MPL-2.0

import unittest
import json
import copy
from openstef.data_classes.split_function import SplitFuncDataClass


def dummy_split_func(arg1, arg2, *args, **kwargs):
    pass


def dummy_split_func2(arg1, arg2, *args, **kwargs):
    pass


class TestSplitFuncDataClass(unittest.TestCase):
    def setUp(self) -> None:
        self.arguments = dict(arg1=1, arg2=2, arg3=3)
        self.split_func_with_strings = SplitFuncDataClass(
            function="test.unit.data_classes.test_split_function.dummy_split_func",
            arguments=json.dumps(self.arguments),
        )
        self.split_func_with_objects = SplitFuncDataClass(
            function=dummy_split_func, arguments=self.arguments
        )

    def test_getattr(self):
        self.assertIs(
            self.split_func_with_objects["function"],
            dummy_split_func,
        )

        self.assertEqual(self.split_func_with_objects["arguments"], self.arguments)

    def test_setattr(self):
        split_func = copy.deepcopy(self.split_func_with_objects)
        split_func["function"] = dummy_split_func2

        self.assertIs(
            split_func.function,
            dummy_split_func2,
        )

    def test_load_function(self):
        split_func, args = self.split_func_with_objects.load()
        self.assertIs(split_func, dummy_split_func)
        self.assertEqual(args, self.arguments)

        split_func, args = self.split_func_with_strings.load()
        self.assertIs(split_func, dummy_split_func)
        self.assertEqual(args, self.arguments)

    def test_check_arguments(self):
        # Should not raise exception
        _ = self.split_func_with_strings.load(required_arguments=["arg1", "arg2"])

        with self.assertRaises(ValueError):
            self.split_func_with_strings.load(
                required_arguments=["arg1", "arg2", "arg3"]
            )


if __name__ == "__main__":
    unittest.main()
