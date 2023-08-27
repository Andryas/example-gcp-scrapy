import datetime

def destymd(bucket, extension):
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    return f"{bucket}/{year}/{month:02}/{day:02}." + extension