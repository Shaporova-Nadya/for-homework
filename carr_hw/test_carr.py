from carrying import curry, uncurry, sum_three_args, multiply_four

def test_curry():
    curried_sum = curry(sum_three_args, 3)
    
    result = curried_sum(1)(2)(3)
    assert result == 6

def test_curry_four():
    curried_mul = curry(multiply_four, 4)
    
    result = curried_mul(2)(3)(4)(5)
    assert result == 120 

def test_uncurry_sum():
    curried_sum = curry(sum_three_args, 3)
    uncurried_sum = uncurry(curried_sum, 3)
    
    result = uncurried_sum(1, 2, 3)
    assert result == 6

def test_uncurry_four():
    curried_mul = curry(multiply_four, 4)
    uncurried_mul = uncurry(curried_mul, 4)

    result = uncurried_mul(2, 3, 4, 5)
    assert result == 120
