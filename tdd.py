def add_two_numbers(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    elif type(a) == str and type(b) == int:
        c = str(b)
        return a + c
    elif type(a) == str and type(b) == str:
        return a + b
    else:
        print("Invalid inputs for a and b.")

add_two_numbers(6, 3)

# Write a number of unit tests to test the following scenarios:

# adds two whole numbers
# def test_add_two_numbers():
#     # Arrange
#     a = 7
#     b = 6
#     expected = 13

#     # Act
#     actual = add_two_numbers(a, b)

#     # Assert - pass
#     assert expected == actual

# test_add_two_numbers()

# adds a positive whole number to a negative whole number
# def test_add_posandneg():
#     # Arrange
#     a = 7
#     b = -6
#     expected = 1

#     # Act
#     actual = add_two_numbers(a, b)

#     # Assert - pass
#     assert expected == actual

# test_add_posandneg()

# adds two floating point numbers
# def test_add_twofloatnum():
#     # Arrange
#     a = 7.0
#     b = 6.0
#     expected = 13.0

#     # Act
#     actual = add_two_numbers(a, b)

#     # Assert - pass
#     assert expected == actual

# test_add_twofloatnum()

# adds a string to a whole number
# def test_add_strtonum():
#     # Arrange
#     a = 'Die Hard '
#     b = 3
#     c = str(b)
#     expected = 'Die Hard 3'

#     # Act
#     actual = add_two_numbers(a, c)

#     # Assert - pass
#     assert expected == actual

# test_add_strtonum()

# adds two strings
# def test_add_twostring():
#     # Arrange
#     a = 'Die Hard '
#     b = '4'
#     expected = 'Die Hard 4'

#     # Act
#     actual = add_two_numbers(a, b)

#     # Assert - pass
#     assert expected == actual

# test_add_twostring()