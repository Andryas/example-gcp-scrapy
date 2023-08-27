#!/bin/bash
cd /home/wavrzenczak/scraping
source venv/bin/activate

# get the start date and time
start_datetime=$(date '+%m_%d_%Y_%H_%M_%S')
echo "${start_datetime} - starting spider"

# prevent click, which pipenv relies on, from freaking out to due to lack of locale info https://click.palletsprojects.com/en/7.x/python3/
export LC_ALL=en_US.utf-8

scrapy crawl $1

# -a debug=$DEBUG &> "logs/log_${start_datetime}.txt"
# get the end date and time
end_datetime=$(date '+%m_%d_%Y_%H_%M_%S')
echo "${end_datetime} - spider finished successfully"
root shutdown
