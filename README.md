## Tool for converting time interval to regular expression

Situation, that i faced many times, when you know exactly what time interval you looking for potential causes of some incident or random 5xx statuses spike. And all you have is raw logs of your balancer of choice (e.g nginx).

It's common to include timestamp in log rows in format like `2022-11-11T10:12:12`. So with this tool you don't need to reinvent regular expression for particular interval each time to filter these logs.

```
% ./main.py --from 01:13:24 --to 21:18:03
(01:(13:(2[4-9]|3[0-9]|4[0-9]|5[0-9])|14:[0-5][0-9]|15:[0-5][0-9]|16:[0-5][0-9]|17:[0-5][0-9]|18:[0-5][0-9]|19:[0-5][0-9]|20:[0-5][0-9]|21:[0-5][0-9]|22:[0-5][0-9]|23:[0-5][0-9]|24:[0-5][0-9]|25:[0-5][0-9]|26:[0-5][0-9]|27:[0-5][0-9]|28:[0-5][0-9]|29:[0-5][0-9]|30:[0-5][0-9]|31:[0-5][0-9]|32:[0-5][0-9]|33:[0-5][0-9]|34:[0-5][0-9]|35:[0-5][0-9]|36:[0-5][0-9]|37:[0-5][0-9]|38:[0-5][0-9]|39:[0-5][0-9]|40:[0-5][0-9]|41:[0-5][0-9]|42:[0-5][0-9]|43:[0-5][0-9]|44:[0-5][0-9]|45:[0-5][0-9]|46:[0-5][0-9]|47:[0-5][0-9]|48:[0-5][0-9]|49:[0-5][0-9]|50:[0-5][0-9]|51:[0-5][0-9]|52:[0-5][0-9]|53:[0-5][0-9]|54:[0-5][0-9]|55:[0-5][0-9]|56:[0-5][0-9]|57:[0-5][0-9]|58:[0-5][0-9]|59:[0-5][0-9])|0[2-9]:[0-5][0-9]:[0-5][0-9]|1[0-9]:[0-5][0-9]:[0-5][0-9]|20:[0-5][0-9]:[0-5][0-9]|21:(00:[0-5][0-9]|01:[0-5][0-9]|02:[0-5][0-9]|03:[0-5][0-9]|04:[0-5][0-9]|05:[0-5][0-9]|06:[0-5][0-9]|07:[0-5][0-9]|08:[0-5][0-9]|09:[0-5][0-9]|10:[0-5][0-9]|11:[0-5][0-9]|12:[0-5][0-9]|13:[0-5][0-9]|14:[0-5][0-9]|15:[0-5][0-9]|16:[0-5][0-9]|17:[0-5][0-9]|18:(0[0-3])))
```

In example above you can notice a common pattern of minutes plus `[0-5][0-9]` seconds that can be reduced to simplier expression, so there is an option for the optimization.

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
