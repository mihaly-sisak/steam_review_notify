# steam_review_notify
Get a notification on bad steam reviews

## Motivation
As an indie dev, monitoring the first few reviews and responding to bad ones is important. However I did not find a feature to get notifications on bad reviews. I just noticed (2024-10-07) 2 bad reviews from early summer. This is bad. This script, ran as a cronjob, will notify me when a new bad review pops up, so I can react faster.

## Script settable variables
`bad_review_num`: The number of bad reviews you expect to see, the script will notify if there is less (script could not fetch data/some other error occured), or more (a new bad review, needs dev input).

`bad_review_url`: From your app Steam page -> Community hub -> Reviews -> Set filter: Most helpful (all time), Negative only -> copy URL

## Use
Add a cron job `0 18 * * * env DISPLAY=:0.0 /usr/bin/python3 /home/user/steam_review_notify.py`, this will check the reviews every day at 6 pm. As with every scraper, please do not abuse it, do not check the bad review count every milisecond, there is no need.
