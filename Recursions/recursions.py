# Understand Recursion by printing something N times
count = 0
def f():
    global count
    if count >= 11:
        return
    print(count)
    count+=1
    f()
      
f()