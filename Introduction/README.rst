House-keeping 
=========================

If you see ">>>", this means you should follow along with the code by
typing and executing code directly in the Python interpreter (e.g., type
``python`` in your terminal and type into the new prompt). If you see a
code block formatted like this::

        # Some_File_Name.py
    
        Code here!

this means you can either create a new Python file ("module") with the
specified name and type the code yourself, or open the file from the
folder you're currently in and just follow along. Either way, you should
try running the script and hopefully with the accompanying explanation
you will understand what is going on. 

    Note: *To run a Python module, you just type ``python
    module_name.py``in your terminal.*
        
    

The Basics
=========================

*   Python is a dynamically typed, interepreted language; variables are
    not declared before use, and you don't have to specify strict types:
    ::
    
        >>> a = 15
        >>> a = "I'm here for an argument"

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