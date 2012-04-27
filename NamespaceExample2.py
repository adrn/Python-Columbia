import NamespaceExample1

def print_list(the_list):
    """ Given a list of values, print each value on a new line, padded with whitespace """
    for item in the_list:
        print("    {}".format(item))

a = 148
b = 11
print_list([a,b])