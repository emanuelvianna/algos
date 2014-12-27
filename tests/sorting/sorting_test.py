import unittest

from algo.sorting.sorting import sort
from algo.utils.test_utils import ExtendedTestCase


class Sort(ExtendedTestCase):

    def test_entries_not_list(self):
        self.assertRaisesWithMessage(
            exc=TypeError,
            msg="`entries` should be a list",
            func=sort,
            entries={}
        )

    def test_entry_is_not_a_number(self):
        self.assertRaisesWithMessage(
            exc=ValueError,
            msg="entry `wat` is not a number",
            func=sort,
            entries=['wat']
        )
