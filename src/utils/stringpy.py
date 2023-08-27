import re
import traceback

def str_extract(x, pattern):
    try:
        return(re.search(pattern, x).group())
    except:
        traceback.print_exc()
        return("")

def str_replace(x, pattern, replace):
    try:
        return(re.sub(pattern, replace, x))
    except:
        traceback.print_exc()
        return("")
    
def str_detect(x, pattern, negate = False):
    x = re.search(pattern, x) 
    if x:
        x=True
    else:
        x=False
        
    if negate == True:
        x = x == False
    
    return x

def str_strip_white_space(x):
    x = " ".join(x.split())
    return x.strip()