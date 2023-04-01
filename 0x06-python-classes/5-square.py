#!/usr/bin/python3
class Square:

    """creating the sqaure of a Square"""

    def __init__(self, size=0):
        """initiating the square """

        if type(size) != int:
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size >= 0")
        else:
            self.__size = size

            @property
            """ indicating the getter method """
            def size(self):
                return(self.__size)

            @size.setter
            """ indicating the setter method """
            def size(self, value):

                if type(size) != int:
                    raise TypeError("size must be an int")
                elif size < 0:
                    raise ValueError("size >= 0")
                else:
                    self.__size = value

            def my_print(self):
                if size == 0:
                    print(' ')
                for i in range(__self.size):
                    for j in range(__self.size):
                        print('#', end='')
                    print('')

