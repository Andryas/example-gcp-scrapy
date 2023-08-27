from datetime import datetime

def now(as_date=True):
    """ time without miliseconds """
    x = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    if as_date == True:
        return datetime.strptime(x, "%Y-%m-%d %H:%M:%S")
    else:
        return x