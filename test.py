#!/usr/bin/env python3

from commandler import (
    register,
    execute,
    enable_debug,
    func_name,
    list_commands,
)

# -----------------------------------------------------------------------------

@register
def something(s=None):
    print(f"invoked - {func_name():20}   with args - '{s}'")

# -----------------------------------------------------------------------------

@register
def otherthing(s=None):
    print(f"invoked - {func_name():20}   with args - '{s}'")

# -----------------------------------------------------------------------------


def main():

    # enable_debug()
    print()

    execute('something')
    execute('something comes')
    execute('something comes and goes')
    execute('otherthing came and went')

    print()
    print()

    cmds = list_commands()

    print("Registered commands:")

    for cmd in cmds:
        print(f"  {cmd}")

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# -----------------------------------------------------------------------------

