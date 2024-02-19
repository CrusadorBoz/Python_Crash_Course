global_var = 10

# from @bOO1 YouTube
# variables inside functions search inside before going outside.
# by creating a local variable inside the function tied to the global
# increases the performance +10%


def func():
    ans = 0
    local_var = global_var  # include this before the for loop
    for i in range(1000):
        ans += global_var * i
    return ans
    

func()
print("Function is completed")
