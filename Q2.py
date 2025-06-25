def foo():
    print("foo")
    return False

def bar():
    print("bar")
    return True

if foo() and bar():
    print("Hello")
#First, foo() runs. It prints "foo" and returns False.

#Because and needs both sides to be True to run the next part, Python stops there.

# It doesn’t run bar() because foo() already returned False.

# This is called short-circuiting — Python stops early if it knows the result.
