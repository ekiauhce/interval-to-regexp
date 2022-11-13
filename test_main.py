import unittest
from unittest import TestCase
import re
from main import get_hours
from datetime import datetime

with open('day_seconds.txt', 'r') as f:
    day_seconds = [line.strip('\n') for line in f.readlines()]

day_seconds_plain = '\n'.join(day_seconds)

class RegexpUsageTest(TestCase):
    def test_match_all_seconds(self):
        for i in range(len(day_seconds)):
            start = day_seconds[i]

            for j in range(i, len(day_seconds)):
                end = day_seconds[j]
                with self.subTest(f"start={start}, end={end}"):
                    regexp = get_hours(start, end)
                    actual = len(re.findall(regexp, day_seconds_plain))
                    diff = datetime.strptime(end, '%H:%M:%S') - datetime.strptime(start, '%H:%M:%S')
                    expected = diff.total_seconds() + 1
                    self.assertEqual(expected, actual, f"start={start}, end={end}")

if __name__ == '__main__':
    unittest.main()