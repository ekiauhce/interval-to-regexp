#!/usr/bin/env python3
import re
import argparse

def time(x: str):
    if re.match(r'([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]', x):
        return x
    raise ValueError

parser = argparse.ArgumentParser()
parser.add_argument('--start', '--from', type=time, required=True)
parser.add_argument('--end', '--to', type=time, required=True)

# e.g '45', '27'
def get_seconds(start: str, end: str):
    if start == end:
        return start
    i_start = int(start)
    i_end = int(end)

    start_div, start_rem = i_start // 10, i_start % 10
    end_div, end_rem = i_end // 10, i_end % 10

    if start_div == end_div:
        return f'{start_div}[{start_rem}-{end_rem}]'

    return f'{start_div}[{start_rem}-9]' + '|' + get_seconds(f'{start_div+1}0', end)

# e.g '11:45', '13:21'
def get_minutes(start: str, end: str):
    if start == end:
        return start

    start_mins, start_secs = start.split(':')
    end_mins, end_secs = end.split(':')


    if start_mins == end_mins:
        if start_secs == '00' and end_secs == '59':
            return f'{start_mins}:[0-5][0-9]'
        return f'{start_mins}:({get_seconds(start_secs, end_secs)})'


    i_start_mins = int(start_mins)
    i_end_mins = int(end_mins)
    result = get_minutes(start, f'{start_mins}:59')
    if i_start_mins < 59 and i_end_mins > 0 and i_end_mins - i_start_mins > 1:
        result += '|' + get_minutes(f'{i_start_mins+1:02d}:00', f'{i_end_mins-1:02d}:59')
    result += '|' + get_minutes(f'{end_mins}:00', end)
    return result


# e.g 09:12:24, 14:03:18
def get_hours(start: str, end: str):
    if start == end:
        return start

    start_hours, start_mins, start_secs = start.split(':')
    end_hours, end_mins, end_secs = end.split(':')

    is_mins_and_secs_full_range = start_mins == '00' and start_secs == '00' and end_mins == '59' and end_secs == '59'
    i_start_hours = int(start_hours)
    i_end_hours = int(end_hours)
    i_start_hours_div, i_start_hours_rem = i_start_hours // 10, i_start_hours % 10
    i_end_hours_div, i_end_hours_rem = i_end_hours // 10, i_end_hours % 10
    if start_hours == end_hours:
        if is_mins_and_secs_full_range:
            return f'{start_hours}:[0-5][0-9]:[0-5][0-9]'
        return f'{start_hours}:({get_minutes(f"{start_mins}:{start_secs}", f"{end_mins}:{end_secs}")})'
    elif is_mins_and_secs_full_range:
        if i_start_hours_div == i_end_hours_div:
            return f'{i_start_hours_div}[{i_start_hours_rem}-{i_end_hours_rem}]:[0-5][0-9]:[0-5][0-9]'
        if i_start_hours_div == 0 and i_end_hours_div == 1:
            return get_hours(start, '09:59:59') + '|' + get_hours('10:00:00', end)
        elif i_start_hours_div == 1 and i_end_hours_div == 2:
            return get_hours(start, '19:59:59') + '|' + get_hours('20:00:00', end)
        elif i_start_hours_div == 0 and i_end_hours_div == 2:
            return get_hours(start, '19:59:59') + '|' + get_hours('20:00:00', end)

    result = get_hours(f'{start_hours}:{start_mins}:{start_secs}', f'{start_hours}:59:59')
    if i_start_hours < 23 and i_end_hours > 0 and i_end_hours - i_start_hours > 1:
        result += '|' + get_hours(f'{i_start_hours+1:02d}:00:00', f'{i_end_hours-1:02d}:59:59')
    result += '|' + get_hours(f'{end_hours}:00:00', end)

    return result

def main(args):
    result = get_hours(args.start, args.end)
    print(f'({result})')

if __name__ == "__main__":
    args = parser.parse_args()
    main(args)