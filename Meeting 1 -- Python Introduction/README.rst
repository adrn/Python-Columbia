The Basics
=========================
    
    Note: *Everything mentioned below refers to core-Python, not Scipy 
            / Numpy.*

*   Python is a dynamically typed, interepreted language. This means
    that variables are not declared before use, i.e. you don't have to
    allocate your own memory, and you don't have to specify strict data
    types. Variables are defined in-place, and can be overwritten like 
    this:
    ::
    
        >>> a = 15
        >>> a = "I'm here for an argument"

*   Variable types in Python are shown below.
    ::
        
        # Basics_VariableTypes.py
        
        # int
        a = 15
        print "An integer! ", a
        
        # long
        b = 1312412401240124139414
        # or
        b = 1312412401240124139414L
        print "A long! ", b
        
    * Integers are created by setting a variable equal to a number with no 
      decimal.
    * Long's are integers with unlimited precision, and are
      differentiated from integers by an L at the end of the number. If you
      don't specify the L, Python will assume you meant to put it there for
      any number larger than the maximum integer (see below in the ``Built-in
      Packages`` section for a way to check your system's maximum int!).
    

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