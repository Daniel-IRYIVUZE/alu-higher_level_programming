#!/usr/bin/python3
'''Defines a class that specifies test cases for Rectangle class
'''
import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO



class TestRectangle(unittest.TestCase):
    '''TestRectangle inherits from unittest class
    '''

    def setUp(self):
        '''Sets up a test environment before each test case if run

        '''
        self.rectangle_t = Rectangle(2, 3, 1, 6, 13)

    #--------------------------------------------------------------------------
    #Tests for id attribute inherited from Base class, which can be passed as an
    #argument or is assigned by default to the number of existing instances
    #--------------------------------------------------------------------------

    def test_id(self):
        '''Ensures id argument was assigned correctly
        '''
        self.assertEqual(self.rectangle_t.id, 13)

    #--------------------------------------------------------------------------
    #The width argument only accepts positive integers, it does not accept zero
    #or values less that zero, raises TypeError/ValueError
    #TestCases that raise ValueError
    #--------------------------------------------------------------------------

    def test_width_negative_int(self):
        '''Tests the setter for width argument
        Ensure width validation raises the right error
        '''
        with self.assertRaises(ValueError):
            self.rectangle_t.width = -2

    def test_width_as_zero(self):
        '''Tests the setter for width argument
        Ensure width validation raises the right error
        '''
        with self.assertRaises(ValueError):
            self.rectangle_t.width = 0

    def test_width_as_negative_float(self):
        '''Tests the setter for width argument
        Ensure width validation raises the right error
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.width = -3.2

    #--------------------------------------------------------------------------
    #The height argument only accepts positive integers, it does not accept zero
    #or values less that zero, raises TypeError/ValueError
    #TestCases that raise ValueError
    #--------------------------------------------------------------------------

    def test_height_as_negative_float(self):
        '''Tests the setter for height argument
        Ensure width validation raises the right error
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.height = -3.2

    def test_height_negative_int(self):
        '''Tests the setter for height argument
        Ensure height validation raises right error
        '''
        with self.assertRaises(ValueError):
            self.rectangle_t.height = -2

    def test_height_as_zero(self):
        '''Tests the setter for height argument
        Ensure height validation raises right error
        '''
        with self.assertRaises(ValueError):
            self.rectangle_t.height = 0

    #--------------------------------------------------------------------------
    #The width argument only accepts positive integers, it does not accept zero
    #or values less that zero, raises TypeError/ValueError
    #--------------------------------------------------------------------------

    def test_width_as_positive_int(self):
        '''Tests width setter by assigning positive int argument
        '''
        self.rectangle_t.width = 4 #Width was formerly equal to 2
        self.assertEqual(self.rectangle_t.width, 4)

    def test_width_as_str(self):
        '''Width setter raises TypeError if width is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.width = "str"

    def test_width_as_float(self):
        '''Width setter raises TypeError if width is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.width = 2.2

    def test_width_as_inf(self):
        '''Width setter raises TypeError if width is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.width = float('inf')

    def test_width_as_nan(self):
        '''Width setter raises TypeError if width is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.width = float('nan')

    def test_width_as_bool(self):
        '''Width setter raises TypeError if width is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.width = True

    #--------------------------------------------------------------------------
    #The height argument only accepts positive integers, it does not accept zero
    #or values less that zero, raises TypeError/ValueError
    #--------------------------------------------------------------------------

    def test_height_as_positive_int(self):
        '''Tests height setter by assigning positive int argument
        '''
        self.rectangle_t.height = 4 #Height was formerly equal to 3
        self.assertEqual(self.rectangle_t.height, 4)

    def test_height_as_str(self):
        '''Height setter raises TypeError if height is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.height = "str"

    def test_height_as_float(self):
        '''Height setter raises TypeError if height is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.height = 2.2

    def test_height_as_inf(self):
        '''Height setter raises TypeError if height is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.height = float('inf')

    def test_height_as_nan(self):
        '''Height setter raises TypeError if height is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.height = float('nan')

    def test_height_as_bool(self):
        '''Height setter raises TypeError if height is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.height = True

    #------------------------------------------------------
    #The X argument only accepts positive integers and zero,
    #otherwise it returns a TypeError/ValueError
    #------------------------------------------------------

    def test_x_as_positive_int(self):
        '''Tests x setter by assigning positive int argument
        '''
        self.rectangle_t.x = 2 #X was formerly equal to 1
        self.assertEqual(self.rectangle_t.x, 2)

    def test_x_as_zero(self):
        '''Tests x setter by assigning zero argument
        '''
        self.rectangle_t.x = 0 #X was formerly equal to 2
        self.assertEqual(self.rectangle_t.x, 0)

    def test_x_as_str(self):
        '''X setter raises TypeError if x is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.x = "str"

    def test_x_as_float(self):
        '''X setter raises TypeError if x is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.x = 2.2

    def test_x_as_inf(self):
        '''X setter raises TypeError if x is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.x = float('inf')

    def test_x_as_nan(self):
        '''X setter raises TypeError if x is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.x = float('nan')

    def test_x_as_bool(self):
        '''X setter raises TypeError if x is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.x = True

    #---------------------------------------------------
    #The Y argument accepts only positive integers and 0
    #returns TypeError/ValueError otherwise
    #---------------------------------------------------

    def test_y_as_positive_int(self):
        '''Tests y setter by assigning positive int argument
        '''
        self.rectangle_t.y = 4 #Y was formerly equal to 6
        self.assertEqual(self.rectangle_t.y, 4)

    def test_y_as_zero(self):
        '''Tests y setter by assigning zero argument
        '''
        self.rectangle_t.y = 0 #Y was formerly equal to 4
        self.assertEqual(self.rectangle_t.y, 0)

    def test_y_as_str(self):
        '''Y setter raises TypeError if y is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.y = "str"

    def test_y_as_float(self):
        '''Y setter raises TypeError if y is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.y = 2.2

    def test_y_as_inf(self):
        '''Y setter raises TypeError if y is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.y = float('inf')

    def test_y_as_nan(self):
        '''Y setter raises TypeError if y is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.y = float('nan')

    def test_y_as_bool(self):
        '''Y setter raises TypeError if y is not an integer
        '''
        with self.assertRaises(TypeError):
            self.rectangle_t.y = True

    #-------------------------------------------------------------------------
    # Area (public instance method) returns the area of the rectangle instance
    #it is called from
    #-------------------------------------------------------------------------

    def test_area(self):
        '''Checks that the right value is returned for the area of
        rectangle instance
        '''
        self.rectangle_t.width = 6
        self.rectangle_t.height = 4
        self.assertEqual(self.rectangle_t.area(), 24)

    #--------------------------------------------------------------------------
    #display (public instance method) prints out the pictoral representation of
    #rectange
    #--------------------------------------------------------------------------

    @patch('sys.stdout', new_callable = StringIO)
    def test_display(self, stdout):
        '''display() methods prints out a pictoral representation of a rectangle
        using '#' character

        Args:
           stdout: New callable pointed to standard output
        '''
        self.rectangle_t.width = 2
        self.rectangle_t.height = 3
        self.rectangle_t.x = 2
        self.rectangle_t.y = 2
        self.rectangle_t.display()
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(stdout.getvalue(), expected_output)

    #-----------------------------------------------------
    #Testing magic __str__ function for rectangle instance
    #-----------------------------------------------------

    def test_rectangle_str(self):
        '''verifies str representation of rectangle instances
        '''
        self.assertEqual(str(self.rectangle_t), "[Rectangle] (13) 1/6 - 2/3")
        self.rectangle_t.width = 6
        self.rectangle_t.height = 4
        self.rectangle_t.x = 1
        self.rectangle_t.y = 1
        self.rectangle_t.id = 11
        self.assertEqual(str(self.rectangle_t), "[Rectangle] (11) 1/1 - 6/4")

    #------------------------------------------------------------------
    #update takes a list of positional no-keyword arguments, or keyword
    #arguments and reassigns the rectangle instance attributes.
    #if args exists and is not empty, kwargs must be skipped
    #------------------------------------------------------------------

    def test_update(self):
        '''Tests the update method that reassigns the rectangle
        instance attributes
        '''
        self.rectangle_t.update(1, 6, 4, 1, 1)
        self.assertEqual(str(self.rectangle_t),"[Rectangle] (1) 1/1 - 6/4")
        self.assertEqual(self.rectangle_t.area(), 24)

    def test_update_args_kwargs(self):
        '''Tests the update method with non keyword and
        keyword arguments supplied
        '''
        self.rectangle_t.update(13, 8, 6, 1, 1, id=12,
                                x=2, y=2, height=7, width=9)
        self.assertEqual(str(self.rectangle_t), "[Rectangle] (13) 1/1 - 8/6")

    def test_update_kwargs(self):
        '''Tests the update method with only keyword arguments supplied
        '''
        self.rectangle_t.update(id=12,
                                x=2, y=2, height=7, width=9)
        self.assertEqual(str(self.rectangle_t), "[Rectangle] (12) 2/2 - 9/7")

if __name__ == "__main__":
    unittest.main(verbosity=2)
