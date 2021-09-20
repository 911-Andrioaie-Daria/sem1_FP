"""
    The complex number class is implemented here
"""


class ComplexNumber:
    """
    Represents one complex number in the form a+bi
    """

    def __init__(self, real_part, imaginary_part=0.0):
        """
        :param real_part: the real part of the number entered by the user -> must be a float number
        :param imaginary_part: the imaginary part entered by the user -> must be a float number. In case the imaginary
                               part is not entered by the user, it is by default considered to be 0.0
        """

        self.__real = float(real_part)
        self.__imaginary = float(imaginary_part)

    @property
    def real_part(self):
        """
        The 'getter' of the real part of the complex number
        """
        return self.__real

    @property
    def imaginary_part(self):
        """
        The 'getter' of the imaginary part of the complex number
        """
        return self.__imaginary

    def __str__(self):
        """
        Converts the complex number into a readable string of the form 'real_part + imaginary_part i'
        :return: the string in the expected form
        """

        # if the imaginary part is negative, the number is converted to a string of the form 'a - bi'
        if self.imaginary_part < 0:
            return str(self.real_part) + ' - ' + str(abs(self.imaginary_part)) + 'i'

        # if the imaginary part is 0, only the real part is converted to a string of the form 'a'
        elif self.imaginary_part == 0:
            return str(self.real_part)

        # string has the standard form of a complex number: a+bi
        else:
            return str(self.real_part) + ' + ' + str(self.imaginary_part) + 'i'


def test_complex_number():
    """
    Test for the ComplexNumber class
    """
    number1 = ComplexNumber(1, -2)
    number2 = ComplexNumber(7.2, 0)

    assert number1.real_part == 1
    assert number1.imaginary_part == -2

    assert number2.real_part == 7.2
    assert number2.imaginary_part == 0


test_complex_number()
