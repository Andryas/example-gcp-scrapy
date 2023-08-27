# Quick tutorial for scraping with GCP with no database

Long story short, the idea is to schedule a machine to start and die after webscraping. To avoid having a database, we create a JSON and insert which page crawled inside this json, and after it finishes collecting, we send it to the bucket. 

- create a VM
- create a schedule for the VM usign crontab
- create a bucket, get this bucket name and use in the next step
- create a file .env in this repository and set BUCKET=bucket-name
- send this repository to the vm,
  - sudo bash setup.sh
  - config crontab, for instance, `15 12 * * MON bash /home/wavrzenczak/scraping/crawl.sh test`
- Note that the crontab for schedule machine need to be close to the crontab setting in the VM, I'd put 15 minutes from each other just in case.

Now, see how is create the `src/spiders/test.py`,  create another one following
the structure, `pipeline.py`, and be happy.


