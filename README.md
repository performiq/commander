# commander

A Python module to handle command line requests.

Command actions - methods - are registered with the decorator - @register

```
from command-handler import (
    register,
    execute,
    func_name
)

...

@register
def something():
    ...

```


They are executed as:

```
some_string = "something comes..."

execute(some_string)
```

if the initial characters of the string either to its end or the
first space match a registered command, the associated function
will be executed - passing in any text after the initial command
name from the evaluated string, if any remainbs.


