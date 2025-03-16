# This document is designed to encapsulate the best practices for working with annotations dicts. If you write Python code that examines __annotations__ on Python objects, we encourage you to follow the guidelines described below.

# The document is organized into four sections: best practices for accessing the annotations of an object in Python versions 3.10 and newer, best practices for accessing the annotations of an object in Python versions 3.9 and older, other best practices for __annotations__ that apply to any Python version, and quirks of __annotations__.

# Note that this document is specifically about working with __annotations__, not uses for annotations. If you’re looking for information on how to use “type hints” in your code, please see the typing module.

def increment(n:int) -> int:
    return n+1

count: int = 0






