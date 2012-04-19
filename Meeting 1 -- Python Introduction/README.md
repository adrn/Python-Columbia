The Basics
=========================
    
    Note: Everything mentioned below refers to core Python, not Scipy / Numpy.

*   Python is a dynamically typed, interepreted language. This means
    that variables are not declared before use, i.e. you don't have to
    allocate your own memory, and you don't have to specify strict variable
    types. Variables are defined in-place, and can be overwritten:
    
        >>> a = 15
        >>> a = "I'm here for an argument"

*   Some basic variable types in Python:
    
    *   Integers are just like you would expect. In Python 2 they are automatically
        promoted to *long* if they exceed your system's maximum int value, and in
        Python 3 ints and longs are unified into one great unlimited precision 
        integer data type.
        
            >>> anInt = 1024
            >>> anInt ** 50
            3273390607896141870013189696827599152216642046043064789483291368096133796404674554883270092325904157150886684127560071009217256545885393053328527589376
            
    *   Floating point numbers are created as you might expect, by dealing with
        decimal numbers. They are by default double precision, but we can talk
        more in detail about them if you want..
        
            >>> aFloat = 14.1345124
            
    *   Complex numbers can be created using a lower-case letter j.
        
            >>> aComplex = 14.5 + 11j
            >>> print(aComplex.real)
            14.5
            >>> print(aComplex.imag)
            11.0

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

*   There are also sequence- and collection-type variables in Python. All of 
    the following objects can be *iterated* over. For example, I can loop 
    through all values in a list without ever touching the indices of the 
    values (see example script).
    
    *   Strings (``str``) are sequences of characters, and are created
        with either single or double quotes. 
        
            >>> aString = "An African or European swallow?"
            or
            >>> aString = 'An African or European swallow?'
        
        By default they are ASCII strings, but by placing a ``U`` in front of the 
        quotes when declaring a variable you can make it a Unicode (UTF-8) string, 
        but you must declare the coding of the file to be Unicode by placing this 
        at the very top of your script:
      
            # coding: utf-8
        
    *   Lists (``list``) are ordered, mutable sequences or collections of
        objects. Lists can contain multiple object types, and can be iterated
        over. Lists are mutable, meaning they can be modified in place.
        
            >>> aList = [1, 15, "Munier"]
        
    *   Tuples (``tuple``) are ordered, immutable sequences or collections
        of objects. Tuples can contain multiple object types, and can be
        iterated over. Tuples are very similar to lists, but are immutable.
        
    *   Sets (``set``) are unordered, mutable collectsions of *hashable*
        objects. Sets can contain multiple object types, and can be iterated
        over, but will only maintain one value for any given hash. For this
        reason, sets can be used for quickly getting all unique values of a list.

*   String formatting
    TODO: fill this in

*   Working with sequences

        TODO: fill this in
        
    *   TODO: explain this
        >>> list1 = list2
        vs
        >>> list1 = list2[:]
    *   Operators (+, *, in)
    *   Indexing / slicing

*   

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

*   For any object in Python, there is a built-in function ``dir()`` that will return
    the *namespace* of the object. TODO: explain namespace and dir
    Other built-in functions [are listed here](http://docs.python.org/library/functions.html).

*   Python code is not (ish) checked at compile time. One consequence of this 
    is that some errors can remain hidden until a seemingly benign change in
    code. Consider [this example script](https://github.com/adrn/PythonBeer/blob/master/Meeting%201%20--%20Python%20Introduction/RuntimeChecking.py). 
    We clearly mistyped the variable ``name`` in the first clause of the 
    ``if`` statement (``nzme``), but this code will run because the interpreter 
    won't enter the top ``if`` block until the condition ``name == "Arthur"`` 
    evaluates to ``True``.