"""Print out all the melons in our inventory."""

from melons import melons



def print_all_melon(melons):
    """ Print each melon and its associated characteristics. """

    for melon, attributes in melons.items():
        print melon.upper()
        for attribute, value in attributes.items():
            print "  {}: {}".format(attribute, value)
        print




print_all_melon(melons)
