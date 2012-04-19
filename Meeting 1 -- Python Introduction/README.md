The Basics
=========================
    
    Note: Everything mentioned below refers to core Python, not Scipy / Numpy.

*   Python is a dynamically typed, interepreted language. This means
    that variables are not declared before use, i.e. you don't have to
    allocate your own memory, and you don't have to specify strict variable
    types. Variables are defined in-place, and can be overwritten:
    
        >>> a = 15
        >>> a = "I'm here for an argument"

*   Some basic variable types in Python are shown in the first example script.
    Open up [Basics_BasicVariableTypes](https://github.com/adrn/PythonBeer/blob/master/Meeting%201%20--%20Python%20Introduction/Basics_BasicVariableTypes.py)
    to follow along: 
    
    *   Integers are created by setting a variable equal to a number with no 
        decimal.
    *   Long's are integers with unlimited precision, and are only different from 
        integers by an L at the end of the number (e.g. 14L). If you don't specify 
        the L, Python will assume you meant to put it there for any number larger 
        than the maximum integer (see below in the ``Built-in Packages`` section 
        for a way to check your system's maximum int!).
    *   Floating point numbers are created by setting a variable equal to a 
        decimal number.
    *   Complex numbers can be created using a lower-case letter j, as shown in
        the example script.
      
*   Open up [Basics_SequenceVariableTypes](https://github.com/adrn/PythonBeer/blob/master/Meeting%201%20--%20Python%20Introduction/Basics_SequenceVariableTypes.py)
    to follow along. There are also sequence- and collection-type variables in 
    Python. All of the following objects can be *iterated* over. For example, I 
    can loop through all values in a list without ever touching the indices of 
    the values (see example script).
    
    * Strings (``str``) are sequences of characters, and are created
      with either single or double quotes. By default they are ASCII strings,
      but by placing a ``U`` in front of the quotes when declaring a variable
      you can make it a Unicode (UTF-8) string, but you must declare the coding
      of the file to be Unicode by placing this at the very top of your script:
        # coding: utf-8
        
    * Lists (``list``) are ordered, mutable sequences or collections of
      objects. Lists can contain multiple object types, and can be iterated
      over. Lists are mutable, meaning they can be modified in place.
    * Tuples (``tuple``) are ordered, immutable sequences or collections
      of objects. Tuples can contain multiple object types, and can be
      iterated over. Tuples are very similar to lists, but are immutable.
    * Sets (``set``) are unordered, mutable collectsions of *hashable*
      objects. Sets can contain multiple object types, and can be iterated
      over, but will only maintain one value for any given hash. For this
      reason, sets can be used for quickly getting all unique values of a list
      (see example).

*   Python code is not (ish) checked at compile time. One consequence of this 
    is that some errors can remain hidden until a seemingly benign change in
    code. Consider [this example script](https://github.com/adrn/PythonBeer/blob/master/Meeting%201%20--%20Python%20Introduction/Basics_RuntimeChecking.py). 
    We clearly mistyped the variable ``name`` in the first clause of the 
    ``if`` statement (``nzme``), but this code will run because the interpreter 
    won't enter the top ``if`` block until the condition ``name == "Arthur"`` 
    evaluates to ``True``.