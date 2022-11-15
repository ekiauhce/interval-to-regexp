## Tool for converting time interval to regular expression

Situation, that i faced many times, when you know exactly what time interval you looking for potential causes of some incident or random 5xx statuses spike. And all you have is raw logs of your balancer of choice (e.g nginx).

It's common to include timestamp in log rows in format like `2022-11-11T10:12:12`. So with this tool you don't need to reinvent regular expression for particular interval each time to filter these logs.

```
% ./main.py --from 01:13:24 --to 21:18:03
(01:(13:(2[4-9]|3[0-9]|4[0-9]|5[0-9])|(1[4-9]|2[0-9]|3[0-9]|4[0-9]|5[0-8]):[0-5][0-9]|59:[0-5][0-9])|0[2-9]:[0-5][0-9]:[0-5][0-9]|1[0-9]:[0-5][0-9]:[0-5][0-9]|20:[0-5][0-9]:[0-5][0-9]|21:(00:[0-5][0-9]|(0[1-9]|1[0-7]):[0-5][0-9]|18:(0[0-3])))
```

### Usage

File `day_seconds.txt` is an example of file with timestamps in it (strictly speaking only the time part).

```
% cat day_seconds.txt | grep -E "$(./main.py --from 01:13:24 --to 21:18:03)" | head -n 5
01:13:24
01:13:25
01:13:26
01:13:27
01:13:28
% cat day_seconds.txt | grep -E "$(./main.py --from 01:13:24 --to 21:18:03)" | tail -n 5
21:17:59
21:18:00
21:18:01
21:18:02
21:18:03
```
