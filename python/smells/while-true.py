# ok
def __main__():
    while True:
        pass


# ruleid: infinite-loop
while True:
    pass


# ok
while True:
    try:
        break
    except Exception:
        pass


# ok
while True:
    if condition:
        return
    do_something

