import unittest
from unittest import TestCase
import re
from main import get_hours
from datetime import datetime

with open('day_seconds.txt', 'r') as f:
    day_seconds = f.read()

cases = [
    ('00:00:00', '23:59:59'),
    ('11:59:59', '12:12:34'),
    ('09:45:13', '15:23:04'),
    ('11:00:23', '11:00:23'),
    ('11:12:23', '11:12:25'),
    ('13:20:20', '14:20:20'),
    ('13:20:20', '13:21:20'),
    ('23:58:59', '23:59:58'),
    ('01:13:24', '21:18:03')
]

class RegexpUsageTest(TestCase):
    def test_match_all_seconds(self):
        for case in cases:
            start, end = case
            with self.subTest(f"start={start}, end={end}"):
                regexp = f'({get_hours(start, end)})'
                actual = len(re.findall(regexp, day_seconds))
                diff = datetime.strptime(end, '%H:%M:%S') - datetime.strptime(start, '%H:%M:%S')
                expected = diff.total_seconds() + 1
                self.assertEqual(expected, actual, regexp)

if __name__ == '__main__':
    unittest.main()