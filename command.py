#!/usr/bin/env python3
# encoding: utf-8
#
#
# -----------------------------------------------------------------------------

import sys
import inspect

# =============================================================================

class Node:
    parent   = None
    char     = None
    children = None
    func     = None

    # ----------------------------------------------------------------------

    def __init__(self, ch=None, fn=None):
        self.char     = ch
        self.children = {}
        self.func     = fn
        self.parent   = None

    # ----------------------------------------------------------------------

    def __str__(self):
        return f"ch |{self.char}|  # Nodes |{len(self.children)}|  Chars |{list(self.children)}|"

    # ----------------------------------------------------------------------

    def __repr__(self):
        return f"""
  ch |{self.ch}|
  cn |{self.cn}|
  fn |{self.fn}|"""


# =============================================================================

COMMANDS = Node()

DEBUG    = False


# =============================================================================

def register(fn):
    """
       This converts any string up to the first space into a command reference
    """

    s = fn.__name__

    print(f"Adding command - |{s}|")

    node = COMMANDS
    last = node
    current_node = COMMANDS

    depth = 0

    l = len(s)

    for idx in range(l):
       ch = s[idx]

       # print(f"depth |{depth}| ch |{ch}|")

       if depth > 0 and ch == ' ':
           last_node.func = fn
           break

       if not ch in current_node.children:     # If there isn't a ch registered in the current level add it
           new_node            = Node(ch=ch)
           new_node.parent     = current_node
           current_node.children[ch] = new_node

       last_node      = current_node   # Save the current level
       current_node   = current_node.children[ch]    # Recurse to the next level
       depth         += 1

       if idx == l - 1:  # At end
           current_node.func = fn

           if DEBUG:
               print(f"  last_node children |{list(last_node.children)}|")
               print(f"      last_node char |{last_node.char}|")
               print(f"current_node chldren |{list(current_node.children)}|")
               print(f"   current_node char |{current_node.char}|")
               print(f"   current_node func |{current_node.func}|")

    return fn


# -----------------------------------------------------------------------------

def execute(s):
    """
       This works through the hash tree for a record matching the string provided and invokes that function
    """

    last    = None
    last_node = None
    current = COMMANDS.children  # So a dict!
    depth   = 0
    l       = len(s)

    for idx in range(l):

       ch = s[idx]

       print(f"depth |{depth}| ch |{ch}|")

       if depth > 0 and ch == ' ':
           # print(last_node.func)
           txt = s[idx+1:]
           # print(f"Invoking from beginning of a string -  {txt}")
           last_node.func(txt)
           return

       if not ch in current:     # If there isn't a ch registered in the current level add it
           print(f"Unable to locate command - {s}")
           return

       last_node = current[ch]
       last      = current
       current   = current[ch].children  # Recurse to the next level
       depth    += 1

       if idx == l - 1:  # At end
           node = last[ch]

           if DEBUG:
               print("Invoking from an exact match")
               print(list(current))
               print(node.func)

           node.func()

# -----------------------------------------------------------------------------

def func_name(): 
    return inspect.getouterframes(inspect.currentframe())[1].function
    # return inspect.stack()[1][3]
    # return inspect.getframeinfo(inspect.currentframe()).function

# -----------------------------------------------------------------------------

@register
def something():
    print(f"invoked - {func_name()}")

# -----------------------------------------------------------------------------

register(something)

# -----------------------------------------------------------------------------

def test_functions():

    print()
    print("Invoking functions to test them")
    print()

    something()

# -----------------------------------------------------------------------------

def test_execution():
    print()
    print("Testing execution")
    print()

    execute('something')
    execute('something comes')
    execute('something comes and goes')

# -----------------------------------------------------------------------------

def main():
    test_execution()

# -----------------------------------------------------------------------------

if__name__== “__main__”:
    main()

# -----------------------------------------------------------------------------

