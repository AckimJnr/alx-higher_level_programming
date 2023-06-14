#!/usr/bin/python3
import builtins
print(*getattr(builtins, '__import__')('string').ascii_uppercase, sep='', end='\n')
