The Basics
=========================
    
    Note: Everything mentioned below refers to core Python, not Scipy 
    / Numpy.

*   Python is a dynamically typed, interepreted language. This means
    that variables are not declared before use, i.e. you don't have to
    allocate your own memory, and you don't have to specify strict data
    types. Variables are defined in-place, and can be overwritten like 
    this:
    ::
    
        >>> a = 15
        >>> a = "I'm here for an argument"

*   Some basic variable types in Python are shown in the example script below.
    
    * Integers are created by setting a variable equal to a number with no 
      decimal.
    * Long's are integers with unlimited precision, and are
      differentiated from integers by an L at the end of the number. If you
      don't specify the L, Python will assume you meant to put it there for
      any number larger than the maximum integer (see below in the ``Built-in
      Packages`` section for a way to check your system's maximum int!).
    * Floating point numbers are created by setting a variable equal to a 
      decimal number.
    * Complex numbers can be created using a lower-case letter j, as below.
      
    ::
        
        # Basics_BasicVariableTypes.py
        
        # int
        a = 15
        print "An integer! ", a
        
        # long
        b = 1312412401240124139414L
        # or
        b = 1312412401240124139414
        print "A long! ", b
        
        # float
        c = 13.124
        print "A float! ", c
        
        # complex
        d = 14.123 + 16.0j
        print "A complex number! ", d

*   There are also sequence- and collection-type variables in Python.
    All of the following objects can be *iterated* over. For example, I can
    loop through all values in a list without ever touching the indices of
    the values (see adrn/PythonBeer/Meeting 1\ --\ Python Introduction/Basics_SequenceVariableTypes.py).
    
    * Strings (``str``) are sequences of characters, and are created
      with either single or double quotes. By default they are ASCII strings,
      but by placing a ``U`` in front of the quotes when declaring a variable
      you can make it a Unicode (UTF-8) string.
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
    
    ::
        
        # Basics_SequenceVariableTypes.py
        
        # list
        aList = [1, 15, "Munier"]
        
        # Because list objects are iterable, I can loop through the values like this:
        for value in aList:
            print value
        
        # List objects are also mutable, meaning I can change them in place
        aList[1] = 35
        print aList
        
        # ---------------------------------------------------------------------------
        # str
        aString = "This is a string!"
        
        # String objects are also iterable, so I can equivalently loop through the
        #   characters in a string
        for character in aString:
            print character
        
        # But strings are just like in other languages, so you can do all the usual things
        print aString.split("a")
        print aString.replace("i", "EYE")
        
        # ---------------------------------------------------------------------------
        
        # tuple
        aTuple = (1, 15, "Munier")
        
        # Tuples are iterable just like lists, but are immutable so item assignment fails
        aTuple[1] = 999 # THIS WILL FAIL! Comment it out to run the code successfully.
            

*   This is nice for brevity, but means that code is not (for most
    cases) checked at compile time. One consequence of this is that the
    following script will run fine, unless ``name`` is changed to "Arthur"
    ::
    
        # Basic1_runtime_checking.py
    
        name = "Zaphod"
    
        if name == "Arthur":
            print nzme
        else:
            print name + " Beeblebrox"
    
    We clearly mistyped the variable ``name`` in the first clause of the
    ``if`` statement (``nzme``), but this code will run because the
    program won't enter the ``if`` blocks until the condition ``name ==
    "Arthur"`` is evaluated.