House-keeping 
=========================

If you see ">>>", this means you should follow along with the code by
typing and executing code directly in the Python interpreter (e.g., type
`python` in your terminal and type into the new prompt). If you see a
code block formatted like this::
        
    

The Basics
=========================

*   Python is a dynamically typed, interepreted language; variables are
    not declared before use, and you don't have to specify strict types:
    ::
    
    >>> a = 15
    >>> a = "I'm here for an argument"

*   This is nice for brevity, but means that code is not (for most
    cases) checked at compile time. One consequence of this is that the
    following script will run fine, unless `name` is changed to "Arthur"
    ::
    
        # Basic1_runtime_checking.py
    
        name = "Zaphod"
    
        if name == "Arthur":
            print nzme
        else:
            print name + " Beeblebrox"
