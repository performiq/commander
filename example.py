#!/usr/bin/env python3
# encoding: utf-8
#
#
# -----------------------------------------------------------------------------

import inspect

from command import (
    register,
    execute,
    func_name
)

# -----------------------------------------------------------------------------

@register
def one():
    print(f"invoked - {func_name()}")

# -----------------------------------------------------------------------------

@register
def two():
    print(f"invoked - {func_name()}")

# -----------------------------------------------------------------------------

@register
def three():
    print(f"invoked - {func_name()}")

# -----------------------------------------------------------------------------

@register
def four():
    print(f"invoked - {func_name()}")

# -----------------------------------------------------------------------------

@register
def slack():
    print(f"invoked - {func_name()}")

# -----------------------------------------------------------------------------

def something(s=None):
    print(f"invoked - {func_name()}   with args - '{s}'")

# -----------------------------------------------------------------------------

@register
def test():
    print(f"invoked - {func_name()}")

# -----------------------------------------------------------------------------

@register
def tasty():
    print(f"invoked - {func_name()}")

# -----------------------------------------------------------------------------

@register
def testy():
    print(f"invoked - {func_name()}")

# -----------------------------------------------------------------------------

# register('one', one)
# register('two', two)
# register('three', three)
# register('four', four)

# register('test', test)
# register('tasty', testy)
# register('testy', testy)
# register('slack', slack)
register(something)

# -----------------------------------------------------------------------------

def test_functions():

    print()
    print("Invoking functions to test them")
    print()

    one()
    two()
    three()
    four()
    test()
    tasty()
    testy()
    slack()
    something()

# -----------------------------------------------------------------------------

def test_execution():
    print()
    print("Testing execution")
    print()


    # execute('testy')
    # execute('tasty')
    execute('something')
    execute('something comes')
    execute('something comes and goes')

# -----------------------------------------------------------------------------

test_execution()

# -----------------------------------------------------------------------------
