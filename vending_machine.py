from byotest import * 

usd_coins = [100, 50, 20, 10, 5, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]

# Function 1
def get_change(amount, coins=eur_coins): 
        
    change = []
    for coin in coins:
        while coin <= amount:   # Change is always going to be less, or in rare occasions, equal to amount spent
            amount -= coin   # Required to ensure the code deducts the amount of the coin from what was sent into the vending machine  
            change.append(coin)
        
        return change
# Test 1 = When the amount of chnage we require is zero, then no coins are returned back
test_are_equal(get_change(0),[])

# Test 2 = The money required is represented by a single coin. Test is passed by creating if statement for Test 1, then return [1] for Test 2.
test_are_equal(get_change(1),[1])

# Test 3 = To send in a different coin to the vending machine. Test is passed by changing 'return [1] to return [amount]'. 
# The Tests are now repeated to cover all coin values.
test_are_equal(get_change(2),[2]) 
test_are_equal(get_change(5),[5]) 
test_are_equal(get_change(10),[10]) 
test_are_equal(get_change(20),[20]) 
test_are_equal(get_change(50),[50]) 
test_are_equal(get_change(100),[100]) 

# Test 4 = Create a test where we need change in more than 1 coin. Below = 3p change, in 2p + 1p. 
test_are_equal(get_change(3),[2,1])

# Test 5 = Similar to Test 4. However, need to create a generic code and ensure correct change is given from valuie sent into machine.
test_are_equal(get_change(7),[5,2])

# Test 6 = Create a test to check where we require more than 1 of a perticular denomination of coin.
test_are_equal(get_change(9),[5,2,2])

# Test 7 = Override current coin denominations
test_are_equal(get_change(35, usd_coins),[25,10])

print("All tests pass!")

