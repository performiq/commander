===============
Command Handler
===============

Overview
========

A framework for registering command actions and then invoking them
by passing in a text string, which could either be from the script
comand line or some other source - say a slack api call.

Command actions - methods - are registered with the decorator - @register

 from command-handler import (
     register,
     execute,
     func_name
 )
 
 ...
 
 @register
 def something():
     ...



They are executed as:

 some_string = "something comes..."
 
 execute(some_string)

if the initial characters of the string either to its end or the
first space match a registered command, the associated function
will be executed - passing in any text after the initial command
name from the evaluated string, if any remainbs.


