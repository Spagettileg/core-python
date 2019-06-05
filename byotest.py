def number_of_evens(numbers):
    return 0
    
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)
    
def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1} instead".format(a, b)
    
def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(collection, item):
    assert item not in collection, "{0} is not in {1}".format(
        item, collection)
        
def test_between(upper_limit, lower_limit, actual):
    assert lower_limit <= actual <= upper_limit, "{0} is not between {1} and {2}".format(actual, lower_limit, upper_limit)

    
# Test to fail the `test_are_equal` function
test_are_equal(number_of_evens([1,2,3,4,5]), 2)

# Test to fail the `test_not_equal` function
test_not_equal(0, 0)

# Test to fail the `test_is_in` function
test_is_in([1], 2)

# Test to fail the `test_not_in` function
test_not_in([1], 1)

# Test to fail the `test_between` function
test_between(10, 1, 200)




