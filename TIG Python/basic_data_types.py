
#comment

#integer
a = 28

#float
b = 2.8

#string
c = "Hello World"

#string with escape characters
d = 'I\'m\tStefan!\nNice to meet you'

#string demonstrating single and double quote behaviour
e = '"Moo" said the cow'

#boolean
f = True
g = False

#list
h = ["hello", 9, b, e, g, ["inception", "BWAAAAAH"]] #talk about indexing

#dictionary
i = {"Donald": "Cool", "Benita": "Really Cool", "Stefan": "The Coolest"} #explain keys

#function
type(i)

#method
h.append("I'm new here")
print(h)

# MATHS ------------------------------

a = "2"
a+a

b = 2
b+b

b+b-1

b*b

b/b

b^b

3%b

# FOR LOOPS -----------------------------

a = ["HI", "I'M", "STEFAN"]
for word in a:
    print(word)


for number in range(1, 11):
    print(number)


# CONDITIONAL LOGIC --------------------

a = 3
b = 5

a == b

a != b

not 1 == 2

not 1 != 2

a > b

a < b

a >= b

a <= b

# IF -----------------------------------

a = 2
b = 3

if a<b:
    print("a is smaller than b")

if a>b:
    print("a is bigger than b")
elif a<b:
    print("a is smaller than b")
else:
    print("a is equal to b")


# WHILE -------------------------------

a = 0
while a<5:
    print(a)
    a+=1 # same as a = a+1

# warn about infinite loops
# talk about ctrl c

# CUSTOM FUNCTIONS --------------------

def fibonacci(n):
    prev_number = 0
    current_number = 1
    for _ in range(1,n):
        fibonacci_number = current_number + prev_number
        prev_number = current_number
        current_number = fibonacci_number
    return fibonacci_number

