def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "Empty String" # "" is an empty string. == means expect
assert count_upper_case("A") == 0, "1 Upper Case" # Set outcome to 0 to fail test, as there is x1 upper case letter "A"
assert count_upper_case("a") == 0, "One lower case" # To confirm count of characters
assert count_upper_case("%$£&^") == 1, "Special characters" # Set outcome to 1 to fail test on Special characters being detected

print("All the tests passed")
# message only confirmed if all tests have been passed. 'Assert' keyword will ensure code stops at point where code failed.

