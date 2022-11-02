import time


def dynamic_fib(n, memo={}):
    """Assumes n is an int >= 0, memo used only by recursive calls
       Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = dynamic_fib(n-1, memo) + dynamic_fib(n-2, memo)
        memo[n] = result
        return result


start_time = time.time()
print(dynamic_fib(998))
print(f"--- {(time.time() - start_time)} seconds ---")


# Result:
# 26863810024485359386146727202142923967616609318986952340123175997617981700247881689338369654483356564191827856161443356312976673642210350324634850410377680367334151172899169723197082763985615764450078474174626
# --- 0.003131866455078125 seconds ---
