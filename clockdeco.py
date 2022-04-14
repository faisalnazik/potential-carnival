
import time
import functools


def clock(func):
    """simple decorator to show the running time of functions"""
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = [repr(arg) for arg in args]
        arg_lst.extend(f'{k}={v!r}' for k, v in kwargs.items())
        arg_str = ', '.join(arg_lst)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))


# Output

'''
$ python clockdeco.py
**************************************** Calling snooze(.123)
[0.13589510s] snooze(0.123) -> None
**************************************** Calling factorial(6)
[0.00000160s] factorial(1) -> 1
[0.00029400s] factorial(2) -> 2
[0.00081220s] factorial(3) -> 6
[0.00122600s] factorial(4) -> 24
[0.00152290s] factorial(5) -> 120
[0.00225510s] factorial(6) -> 720
6! = 720

'''
