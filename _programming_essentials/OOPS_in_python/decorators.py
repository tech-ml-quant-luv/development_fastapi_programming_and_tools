import time

def timer_dec(fx):
    def enhanced_function():
        start_time = time.time()
        fx()
        end_time = time.time()
        print(end_time - start_time)
    return enhanced_function

def brew_tea():
    print("Brewing tea...")
    time.sleep(1)
    print("Tea is ready...")


# There are two ways to call the enhanced function

#Method 1
print(timer_dec(brew_tea)) #This will return a function object
brew_tea= timer_dec(brew_tea)
brew_tea()

#Method 2
@timer_dec
def brew_tea():
    print("Brewing tea...")
    time.sleep(1)
    print("Tea is ready...")
brew_tea()




