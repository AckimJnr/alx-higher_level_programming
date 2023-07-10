#!/usr/bin/python3
""" Contains an implementantion of inheritance of the int class """


class MyInt(int):
    """ The class """

    def __eq__(self, other_ops):
        """
        Inverts the behaviour of the '==' operator
        """
        return super().__ne__(other_ops)

    def __ne__(self, other_ops):
        """
        inverts the behaviour of '!=' operator
        """
        return super().__eq__(other_ops)
