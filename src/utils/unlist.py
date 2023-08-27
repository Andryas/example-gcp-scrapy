# TODO generalize to return string or the minimal possible list
def unlist_recursive(lst):
    return sum(([x] if not isinstance(x, list) else unlist_recursive(x)
                for x in lst), [])
def unlist(lst):
    if bool(lst) == False:
        return ("")
    elif type(lst) == str:
        return (lst)
    else:
        return (' '.join(unlist_recursive(lst)))
