# https://www.codegrepper.com/code-examples/python/split+a+list+in+100+each
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]