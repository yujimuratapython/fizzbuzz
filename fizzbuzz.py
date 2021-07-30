for i in range(1, 20):
    if i % 15 == 0:
        print("Fizz Buzz!")
    elif i % 3 == 0:
        print("Fizz!")
    elif i % 5 == 0:
        print("Buzz!")
    else:
        print(i)

l = ["FizzBuzz" if x %3 ==0 and x % 5 ==0 else "Buzz" if x % 5 ==0 else "Fizz" if x% 3 == 0 else x for x in range(1,21)]
print(l)
