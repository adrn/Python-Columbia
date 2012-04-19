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
    Open up [BasicVariableTypes](https://github.com/adrn/PythonBeer/blob/master/Meeting%201%20--%20Python%20Introduction/BasicVariableTypes.py)
    to follow along: 
    
    *   **Python 2.x only!** Integers are created by setting a variable equal to a 
        number with no decimal.
    *   **Python 2.x only!** Long's are integers with unlimited precision, and are 
        only different from integers by an L at the end of the number (e.g. 14L). If 
        you don't specify the L, Python will assume you meant to put it there for any 
        number larger than the maximum integer (see below in the ``Built-in Packages`` 
        section for a way to check your system's maximum int!).
    *   **Python 3.x only!** In Python 3, integers and longs were unified, and now
        all integers behave like longs *when they need to*. Otherwise, they're just
        like ordinary integers.
    *   Floating point numbers are created by setting a variable equal to a 
        decimal number.
    *   Complex numbers can be created using a lower-case letter j, as shown in
        the example script.

*   Arithmetic 
    
        TODO: fill this in...

*   Logical operators are words, not symbols!
        
        >>> a = 1
        >>> b = 42.0
        >>> (a > 0) and (b < 100)
        True
        >>> (a > 0) or (b < 10)
        True
        >>> not a > 0
        False

*   Open up [SequenceVariableTypes](https://github.com/adrn/PythonBeer/blob/master/Meeting%201%20--%20Python%20Introduction/SequenceVariableTypes.py)
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
        
    *   Lists (``list``) are ordered, mutable sequences or collections of
        objects. Lists can contain multiple object types, and can be iterated
        over. Lists are mutable, meaning they can be modified in place.
    *   Tuples (``tuple``) are ordered, immutable sequences or collections
        of objects. Tuples can contain multiple object types, and can be
        iterated over. Tuples are very similar to lists, but are immutable.
    *   Sets (``set``) are unordered, mutable collectsions of *hashable*
        objects. Sets can contain multiple object types, and can be iterated
        over, but will only maintain one value for any given hash. For this
        reason, sets can be used for quickly getting all unique values of a list
        (see example).

*   String formatting
    TODO: fill this in

*   Working with lists

        TODO: fill this in
        
    *   TODO: explain this
        list1 = list2
    vs
        list1 = list2[:]

*   if statements and loops (white space not curly braces!)
    
        TODO: fill this in

*   Comments
    
        TODO: fill this in

*   Assignments and reference semantics. Consider the following example:
    
        >>> a = [1, 2, 3]
        >>> b = a
        >>> a[1] = 100
        >>> print(b)
        [1, 100, 3]
    
    Why does this happen? The assignment operation, ``b = a`` in this case, assigns
    a reference to the memory that ``a`` points to: it **doesn't** copy the contents 
    of ``a``. This is because lists are *mutable* objects. Note that for immutable
    objects, this does not happen:
        
        >>> x = 3
        >>> y = x
        >>> x = 4
        >>> print(y)
        3

*   Python code is not (ish) checked at compile time. One consequence of this 
    is that some errors can remain hidden until a seemingly benign change in
    code. Consider [this example script](https://github.com/adrn/PythonBeer/blob/master/Meeting%201%20--%20Python%20Introduction/RuntimeChecking.py). 
    We clearly mistyped the variable ``name`` in the first clause of the 
    ``if`` statement (``nzme``), but this code will run because the interpreter 
    won't enter the top ``if`` block until the condition ``name == "Arthur"`` 
    evaluates to ``True``.