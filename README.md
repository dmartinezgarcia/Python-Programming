# 0. Python-Programming
Book: **Python Programming**, Third Edition by Michael Dawson

This repository contains the solutions to the exercises and my own notes intended to be used for quick 
reference or for future reference in case I forget something.

So far the repository contains notes and exercises for the following topics:

- Chapter 1: Getting started
- Chapter 2: Types, variables and simple I/O
- Chapter 3: Branching and while loops
- Chapter 4: For loops, strings and tuples
- Chapter 5: Lists and dictionaries
- Chapter 6: Functions
- Chapter 7: Files and Exceptions

# 1. Getting Started

By learning Python, one can create something as simple as a game to a business product with a full-featured 
graphical interface (GUI). In this chapter you will learn:

- What Python is and what's so great about it
- How to print text to the screen
- What comments are and how to use them

## 1.1 Facts about Python

**Python is easy to use**: Python has clear and simple rules, its programs are shorter and take less time to create
than programs in many other languages.

**Python is powerful**: You can write programs that employ a GUI, that process files and that use a variety of data 
structures.

**Python is Object-Oriented and flexible**: *Object-oriented programming* is a modern approach to programming, its
 an approach that allows programmers to represent information and actions in a program intuitively. In many other 
languages, OOP is not optional, which makes short programs unnecessarily complex. In Python, OOP is optional.

**Python can be integrated with other languages**: This means that a programmer can take advantage of work already 
done in another language.

**Python runs everywhere**: Python programs are *platform independent*, this means that it will run in any computer 
where Python is installed, independently of the operating system.

**Python has a strong community**: Refer to the [Python Tutor mailing](http://www.mail.python
.org/mailman/listinfo/tutor). Anyone, from novice to expert, can ask and answer any questions.

**Python is Free and Open Source**: Python is free, you can copy or modify Python, you could even resell Python if you
want.

## 1.2 The print function

The `print()` function can display text enclosed in quotes, if you just put the parentheses, it will print a blank line.

```python
>>> print("Hello, World")
Hello, World
```

This is just a brief explanation of the `print()` function.

## 1.3 Interactive and script mode

Most Python IDE's have a console where you can quickly test an idea, this is *interactive mode* as you get inmmediate
feedback. You use *script mode* to make programs than you can execute later on.

Using both modes at the same time is a great way to code, you can use interactive mode to get the function to work 
the way you actually expect it to work before implementing it in your system, for which you should be using script mode.

## 1.4 Comments

The *comments* are notes for human readers, they are ignored by the computer.

To create a comment in Python you use the `#` symbol. Anything after the symbol (except when used in a string) on the 
rest of the line is a comment.

```python
# This is a comment.
```

# 2. Types, Variables and Simple I/O

In this chapter, you will learn about the following:

- Use triple-quoted strings and escape sequences to gain more control over text
- Make your programs do math
- Store data in the computer's memory
- Use variable to access and manipulate data
- Get input from users to create interactive programs

## 2.1 Strings and the print function

You can use either a pair of single quotes, `'`, or a pair of double quotes, `"`, to create string values. If you use
double quotes to begin and end your string, then you can use single quotes anywhere within the string, and vice 
versa, but you can't use inside the string the quotes you have used to delimit the string.

```python
>>> print("'hello'")
'hello'
>>> print('"hello"')
"hello"
```

You can print multiple values with a single call to the `print()` function, like this:

```python
>>> print('hello', 'I', 'am', 'someone.')
hello I am someone.
```

By default, each value is printed with a space as a separator.

By default the `print()` function prints the new line character at the end of the string, you can specify the final 
character to print in a string using the `end` keyword, like this:

```python
>>> print("Hey, ", end="")
>>> print("Is that you?")
Hey, Is that you?
```

*Triple-quoted* strings work the same way as the strings previously defined but are delimited with the `"""` combination
of characters. Something truly useful with this kind of strings is that they can span multiple lines:

```python
""" This is 
a triple quoted
string """
```

You can use *escape sequences* to put special characters in your strings. These are a combination of two characters, 
a backslash `\` and another character. Some common examples of escape sequences are the following:

| Escape sequence | Description |
| :---------------: | :------------- |
| \\ | Backslash. Prints one backslash. |
| \' | Single quote. Prints a single quote. |
| \" | Double quote. Prints a double quote. |
| \a | Bell. Sounds the system bell. |
| \n | Newline. Moves cursor to beginning of next line. |
| \t | Horizontal tab. Moves cursor forward one tab stop. |

You can concatenate strings to create a whole new string, using the `+` operator as follows:

```python
>>> print("Hello, this is " + "a concatenated string.")
Hello, this is a concatenated string.
```

You can use the repetition operator, `*` to print a string multiple times, for example:

```python
>>> print("Hey, three times! " * 3)
Hey, three times! Hey, three times! Hey, three times! 
```

## 2.2 Numbers

Python has several ways of dealing with numbers to fit all the programming needs of its users. The most common are 
*integers*, numbers with no fractional part, and *floats*, numbers with fractional part.

Example of integer numbers are the following: 1, 30, -50. Examples of float numbers are the following: 1.23, 821.23, 
-54.1;

### 2.2.1 Mathematical operators

These are some of the most common and useful mathematical operators in Python:

|Operator|Description|Example|Result|
|:-:|:-:|:-:|:-:|
|+|Addition|7+3|10|
|-|Subtraction|7-3|4|
|*|Multiplication|7*3|21|
|/|Division (Float)|7/3|2.3333333|
|//|Division (Integer)|7//3|2|
|%|Modulus|7%3|1|

The float division is not exact, you can use the *decimal* module that provides support for accurate decimal 
floating-point arithmetic.

## 2.3 Variables

Variables allow the programmer to store and manipulate information. A *variable* provides a way to label and access 
information.

### 2.3.1 Creating variables

You can create a variable like this:

```python
var_name = "val"
```

In the statement above and assuming the variable `var_name` has not been created previously, the variable `var_name` is 
created and assigned the a reference to the string literal `"val"`.

### 2.3.2 Using variables

The convenience of using variables is that they can be used the same way as the value they refer to, following from 
our previous example:

```python
>>> print(var_name)
val
```

or:

```python
>>> print("What?,", var_name)
What?, val
```

### 2.3.3 Naming variables

The following are the two most important rules to keep in mind, otherwise Python will show an error:

1. A variable name can contain only numbers, letters and underscores.
2. A variable name can't start with a number.

Programmers also tend to follow these guidelines:

1. **Descriptive names**, variable names should give an idea of what they represent.
2. **Consistency**, for example,with multi-word variables you can use the underscore style (`high_score`) or the 
capital letter style (`highScore`), but be consistent with your style of coding.
3. **Traditions of the language**, for example, all variables start with a lowercase letter or avoid using 
underscores as the first character of the name of a variable.
4. **Length**, as a guideline, try to keep your variable names under 15 characters.

### 2.3.4 Input

Information that the user inputs can be stored in variables, using the `input()` function.

```python
name = input("Hey, input something and press enter")
```

The `input()` function gets information from the user and returns it as a string once the user presses the enter key,
it takes an argument that is used as prompt for the user.

## 2.4 String methods

*Methods* are similar to functions, they need to be called trough a particular data type. You *invoke* a method by 
adding a dot, following the name of the method, following by a pair of parentheses, where to include the necessary 
arguments for the method. For example:

```python
>>> print("Hey, print this in capital letters.".upper())
HEY, PRINT THIS IN CAPITAL LETTERS.
```

Some of the most common string methods are the following:

|Method|Description|
|:-----:|:------|
|`upper()`|Returns the uppercase version of the string|
|`lower()`|Returns the lowercase version of the string|
|`swapcase()`|Returns a new string where each uppercase character becomes lowercase and vice versa|
|`capitalize()`|Returns a new string where the first character is capitalized and the rest are lowercase|
|`title()`|Returns a new string where the first character of each word is capitalized and the rest are lowercase|
|`strip()`|Returns a string where all the tabs, spaces and new lines at the beginning and the end of the string are removed|
|`replace(old, new, [,max])`|Returns a string where all the *old* occurrences are replaced with the *new* ones, the optional argument *max* limits the number of replacements.|

## 2.5 Conversion between types

These are the functions that convert values to a specific type:

|Function|Description|Example|Result|
|:---|:----|:----|:----|
|`float(x)`|Returns the floating-point value associated to *x*|`float("10.0")`|10.0|
|`int(x)`|Returns the integer value associated to *x*|`int("10")`|10|
|`str(x)`|Returns the string value associated to *x*|`str(10)`|"10"|

## 2.6 Augmented assignment operators

These are just a shortcut for a calculation and assignment operation, the ones in this table are the ones related to 
the arithmetical operators:

|Operator|Example|Is equivalent to|
|:----|:-----|:------|
|\*=|a \*= 10|a = a \* 10|
|/=|a /= 10|a = a / 10|
|%=|a %= 10|a = a % 10|
|+=|a += 10|a = a + 10|
|-=|a -= 10|a = a - 10|

# 3. Branching and while loops

In this chapter you will learn how to selectively execute certain portions of your code and repeat parts of your 
program. You will learn how to do the following:

- Generate random numbers with `randint()` and `randrange()`
- Use `if`, `else`, `elif` statements to execute code statements, or not.
- Use `while` loops to execute certain parts of your code as many times as you want

## 3.1 Generating random numbers

Python provides an easy way to generate *pseudorandom* numbers, for this, you need to use the `random` module using 
the import statement.

```python
import random
```

Then you can have access to the `randint()` function, which generates a random integer between two numbers provided 
by the user, including those two numbers.

```python
>>> random.randint(1, 10)
3
```

And access to the `randrange()` function, which can be used to generate a random number between zero and a number 
positive number provided by the user, not including this number.

```python
>>> random.randrange(10)
8
```

## 3.2 Comparison operators

Conditions are commonly created by comparing values, these are the most common comparison operators:

|Operator|Meaning|Sample Condition|Evaluates To|
|:----:|:----|:-----|:-------|
|`==`|Equal to|`1 == 1`|True|
|`!=`|Not equal to|`1 != 2`|True|
|`>`|Greater than|`3 > 10`|False|
|`<`|Less than|`5 < 9`|True|
|`>=`|Greater than or equal to|`2 >= 4`|False|
|`<=`|Less than or equal to|`2 <= 2`|True|

You perform comparisons on many types but Python won't let you make comparisons for objects of different types that 
don't have an established definition for order. For example, you can't compare integers and strings.

## 3.3 The If statement

Branching is fundamental to programming, it basically means executing a section of code or skipping it, based on a 
condition or set of conditions. You can use the `if` statement to assist you in branching.

All `if` statements have at least one condition, something that evaluates to true or false. The keyword `True` in 
python means true, and the keyword `False` means false.

You can construct an `if` statement by using the `if` keyword, followed by a condition or set of conditions followed 
by a colon, followed by a block of one or more statements. If the condition evaluates to true, the block of 
statements will be executed, otherwise they will be skipped.

```python
if "One string" == "Two strings":
  print("Will never print this")
```

In case you want to execute a set of programming statements if the condition evaluates to false, you can use the 
`else` statement like this:

```python
if "One string" == "Two strings":
  print("Will never print this")
else:
  print("Will print this")
```

Note that the `else` must be in the same block as the associated `if`, this also means that both block statements must
be indented by the same amount of spaces.

You can use the `elif` clause following the same rules as with the `else` clause to evaluate more conditions, for 
example:

```python
if "One string" == "Two strings":
  print("Will never print this")
elif "One string" == "One string":
  print("Will print this")
elif "Two strings" == "Two strings":
  print("Will never print this, in fact, this condition is not evaluated")
else:
  print("Same as above, but in this case there is no condition to evaluate")
```

In this case, once a condition evaluates to true, the associated block of statements is executed and program flow 
jumps to the next statements after the `if` statement. This means, that at most, only one block of code is executed, 
even if several conditions would evaluate to true, only the first one that evaluates to true gets his associated 
programming statements executed.

While the `else` clause is not necessary in some `if` statements, it is usually useful to use to catch that 
impossible case that you might think never happen, this way you can keep track of errors and bugs easily.

## 3.4 While loops

The `while` loop lets you execute certain parts of code a defined number of times, based on the evaluation of a 
condition. It can be written as follows:

```python
input_var = ""
while input_var != "hello":
  response = input("Hello...")
```

A `while` loop executes the associated block of statements while the condition evaluates to true, if it evaluates to 
false, the program flow jumps to the first statement after the `while` loop body. This means that the user must make 
sure that the condition evaluates to true at least once, otherwise the `while` loop never executes.

You can use a `break` statement to exit the loop at any time, for example:

```python
count = 0
while True:
  count = count + 1
  if count == 10:
    break
```

And you can use the `continue` statement to return to the top of the loop, the evaluation of the condition, at any 
time, for example:

```python
count = 10
while count != 0:
  if count == 5:
    continue
  print("Count value is: ")
  print(count)
  count = count - 1
```

In the code above, when `count` equals five, nothing is printed.

The `break` and `continue` statements make it harder for the reader to follow the program flow, however there are 
cases when using this statements that make the loop become more clearer. It's up to the user to use these statements,
as usually any `while` loop can be written by just evaluating a condition.

## 3.5 Compound conditions and logical operators

You can combine simple conditions together with *logical* operators. This way your programs can make decisions based 
on multiple conditions.

### 3.5.1 The not logical operator

The `not` operator can be used for example in this way:

```python
var = 0
if not var:
  print("This is printed")
```

The value of `var` is set to zero, which evaluates to false, however the `not` operator makes it evaluate to the 
opposite of the original. Here is the truth table for the `not` operator:

|Input|Output|
|:-----:|:------:|
|False|True|
|True|False|

### 3.5.2 The and logical operator

The `and` operator can be used for example in this way:

```python
var0 = 10
var1 = 0
if var0 == 10 and var1 == 0:
  print("This is printed")
```
The `and` operator can be used to combine multiple simple conditions. The truth table associated to the `and` 
operator is the following:

|Input 0|Input 1|Output|
|:------:|:------:|:-------:|
|True|True|True|
|True|False|False|
|False|True|False|
|False|False|False|

### 3.5.3 The or logical operator

The `or` logical operator can be used for example in this way:

```python
var0 = 0
var1 = 10
if var0 == 0 or var1 == 20
  print("This is printed")
```

As with the `and` operator, the `or` operator can be used to combine multiple simple conditions. The truth table 
associated with the `or` operator is the following:

|Input 0|Input 1|Output|
|:------:|:------:|:--------:|
|True|True|True|
|True|False|True|
|False|True|True|
|False|False|False|

# 4. For loops, strings and tuples

In this chapter you will learn to do the following:

- Construct `for` loops to move through a sequence
- Use the `range()` function to create a sequence of numbers
- Treat strings as sequences
- Use tuples to harness the power of sequences
- Use sequence functions and operators
- Index and slice sequences

## 4.1 For loops

The `for` loop repeats some code based on a *sequence*, an ordered list of things. It repeats some code for each 
element in the sequence and once it reaches the end of the sequence the program flow exits from the loop.

An example of a sequence could be a string, a string is a sequence of characters. We can use a `for` loop to iterate 
over a sequence like this:

```python
for a in "This is a string":
  print(a, end="")
print("\n")
```

For the previous example, the variable `a` is created in case it wasn't created before the `for` loop. This 
variable contains the elements of the sequence, in this case the string `"This is a string"`, as the loop is executed.
Inside the loop body, the character is printed, once there are no elements in the sequence to process, the program 
flow exits from the loop.

You can also use a `for` loop in its traditional form, in which a counter variable is incremented or decreased. For 
this you can use the `range()` function, which takes three arguments like this, although there are more possibilities 
for the range function that the reader can check for himself.

```python
start = 0
end = 10
step = 2
for a in range(lower_bound, upper_bound, step):
  print(a, end=" ")
```

This function doesn't generate a sequence of numbers but the next number in the sequence, it generates an iterator, 
see **Note 11** to know more. However to understand this form of the `for` loop it's fine to think that it generates 
a sequence of numbers. In the previous example, the output is the following: `0 2 4 6 8 `.

With the possibilities that the `range()` function admits, you can count forwards, count backwards and count in steps
. Also, there is no need to use the variable defined in the loop inside the loop, for example:

```python
for i in range(20, 0, -2):
  print("Print this ten times")
```

## 4.2 Sequence operators

The *sequence operators* can tell you simple but important things about sequences.

### 4.2.1 The len() function

The `len()` function returns the length of a sequence. For example, with a string:

```python
>>> len("This is a string")
16
```

### 4.2.2 The in operator

You can use the `in` operator anywhere in your program to see if something is included in a sequence, this operator 
creates a condition that evaluates to `True` or `False`. We have seen examples with the `for` loops about the usage of
the `in` operator.

```python
if 5 in range(0, 10, 1):
  print("This is printed")
```

### 4.2.3 Indexing

What we have been doing so far is known as *sequential access*, but what if you want to access an specific element in
a sequence without iterating through the elements, this is called *random access*, you can achieve it by **indexing**.

Think of a sequence, for example an string, each element of the sequence has a numbered position, starting from zero.
So for example the string `"This"` has a length of four and the last character, `'s'`, is at position three. To 
access any particular element of a sequence you enclose the position number in brackets like this:
 
```python
>>> text = "0123456789"
>>> print(text[0])
0
>>> print(text[1])
1
>>> print(text[2])
2
```

With positive numbers, the counting starts at the beginning of the sequence. You can work with negative position 
numbers as well, in this case the counting starts at the end of the sequence, so the position numbered `-1` returns the
last element of the sequence and the position numbered `-2` returns the second to the last element of the sequence, 
following from our previous example:

```python
>>> text = "0123456789"
>>> print(text[-1])
9
>>> print(text[-2])
8
>>> print(text[-5])
5
```

Basically, this table defines all the possibilities:

|Positive numbers|0|1|2|3|4|5|6|7|8|9|
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|Text|`0`|`1`|`2`|`3`|`4`|`5`|`6`|`7`|`8`|`9`|
|Negative numbers|-10|-9|-8|-7|-6|-5|-4|-3|-2|-1|

### 4.2.4 Slicing

With the indexing you can access one element at a time, by slicing, you can access multiple elements in a sequence at a
time. For slicing, you need to provide an starting position number and an ending position number, enclosed in 
brackets and separated with a colon, for example:

```python
>>> text = "0123456789"
>>> print(text[3:8])
34567
```

It's important to note that you can combine positive and negative position numbers, however, if you create an 
"impossible" combination (for example that the starting point is bigger than the ending point), Python will just 
return an empty sequence.

There are shortcuts that you should remember regarding slicing, these are the most common ones:

```python
>>> text = "0123456789"
# Omitting the starting point means the slicing will start at zero.
>>> print(text[:5])
01234
# Omitting the ending point means the slicing wil end at the end of sequence.
>>> print(text[3:])
3456789
# Omitting both numbers means the slicing will start at zero and end at the end of the sequence.
>>> print(text[:])
0123456789
```

## 4.3 Mutable and immutable sequences

Sequences can be classified in two groups, **mutable** or **immutable**. Mutable sequences are those that can be 
changed, while immutable means the opposite.

An example of an immutable sequence is a string, you can't modify the elements of a string like this:

```python
text = "012345"
text[3] = "5"
```

The code above will just generate an error. An example of mutable sequences are lists, which we shall see in the 
future. It's important to note that when you concatenate strings, you are creating strings, not changing an already 
existing string.

## 4.4 Tuples

**Tuples** are a type of **immutable sequence** that can contain elements of any type, these elements don't have to be
of the same type. Tuples are similar to *vectors* or *arrays* in other languages, however these structures do not 
provide the flexibility that Python offers with tuples.

To create a tuple, you just enclose in parentheses a sequence of values separated by commas, for example:

```python
ex_tuple = (1, "Tuple_String", 1.40)
```

You can create an empty tuple by just using the parentheses:

```python
ex_tuple = ()
```

A tuple, just like any other type, can be used as a condition. When a tuple has no elements, its empty, it evaluates 
to `False`, while it evaluates to `True` if it has at least one element.

```python
ex_tuple = ()
if ex_tuple:
  print("This is not printed")
else:
  print("This is printed")
```

When using the `print()` function with a tuple, it processes every element in the tuple and returns enclosed in 
parentheses each result separated by commas.

```python
>>> ex_tuple = (1, "String", 30.21)
>>> print(ex_tuple)
(1, 'String', 30.21)
```

Since tuples are just a type of sequence, you can do operations such as indexing, slicing and those that we have 
defined till now with them.

# 5. List and dictionaries

In this chapter you will work with **lists** and **dictionaries**, specifically, you will learn about the following:

- Create, index and slice a list
- Add and delete elements from a list
- Use list methods to append and sort a list
- Use nested sequences to represent even more complex information
- Use dictionaries to work with pairs of data
- Add and delete dictionary items

## 5.1 Lists

In this chapter we introduce another type of sequence, *lists*. They are just like tuples but **lists are mutable**. 
The fact that they are like tuples means that everything you learned for tuples also works with lists.

To create a list, you enclose the elements in square brackets and separated by commas, for example:

```python
ex_list = ["String", 2, 30.0]
```

You can create an empty list by not supplying any value:

```python
ex_list = []
```

Other operations like the `len()` function, indexing, slicing... works the same as with tuples. The main difference 
is that list are mutable, and these permits other possibilities.

### 5.1.1 Assigning new elements by indexing and slicing

You can assign an existing a new value by indexing like this:

```python
>>> ex_list = ["String", 1, 2.0]
>>> print(ex_list)
['String', 1, 2.0]
>>> ex_list[0] = "Changed"
>>> ex_list[2] = "Changed too"
>>> print(ex_list)
['Changed', 1, 'Changed too']
```

You can do the same by slicing:

```python
>>> ex_list = ["Hey", 2, 3.0, "Another hey"]
>>> print(ex_list)
['Hey', 2, 3.0, 'Another hey']
# Replacing two elements
>>> ex_list[0:2] = [0, "D"]
>>> print(ex_list)
[0, 'D', 3.0, 'Another hey']
# Replacing two elements by just one element, the list size is decreased
>>> ex_list[1:3] = ["A"]
>>> print(ex_list)
[0, 'A', 'Another hey']
```

In any case, you can only do this with existing elements, you can't make operations that result in the list 
increasing its size or new elements being added to the size, this will result in an error.

### 5.1.2 Deleting elements from a list

You can delete elements from a list with the `del` keyword in combination with either indexing or slicing:

```python
>>> ex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> del ex_list[0]
>>> print(ex_list)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> del ex_list[:3]
>>> print(ex_list)
[4, 5, 6, 7, 8, 9]
```

As you can see, deleting elements don't create gaps, the size of the list is decreased by the amount of elements you 
delete and elements change their positions.

### 5.1.3 List methods

Through list methods, you can do things such as adding elements, deleting elements based on its value, sort the list 
or even reverse the order of the list.

With the `append()` method, you can add an element at the end of the list, which makes the size of the list increase 
by one.

```python
>>> ex_list = [1, 2, 3, 4]
>>> print(ex_list)
[1, 2, 3, 4]
>>> ex_list.append(5)
>>> print(ex_list)
[1, 2, 3, 4, 5]
```

With the `remove()` method, you can remove the first occurrence of an element from the list, and the size of the list
is therefore decreased by one.

```python
>>> ex_list = [0, 1, 2, 2, 2, 3, 4]
>>> ex_list.remove(2)
>>> print(ex_list)
[0, 1, 2, 2, 3, 4]
>>> ex_list.remove(2)
>>> print(ex_list)
```

In contrast with the `del` keyword, this deletes an element based on its value and not on its position. It is important
to note that the `remove()` method, if the element supplied is not in the list, returns an error. So a safer way to 
remove an element could be this:

```python
if 2 in ex_list:
  ex_list.remove(2)
```

With the `sort()` method you can order a list, keep in mind that the original order of the elements is as the user 
entered them. You can sort in ascending order (default) or in descending order (using the `reverse` parameter), the 
following is an example of both possibilities:

```python
>>> ex_list = [3, 5, 4, 1, 2, 0]
# Sort in ascending order
>>> ex_list.sort()
>>> print(ex_list)
[0, 1, 2, 3, 4, 5]
# Sort in descending order
>>> ex_list.sort(reverse=True)
>>> print(ex_list)
[5, 4, 3, 2, 1, 0]
```

Here is a table with the most used functions for lists:

|Method|Description|
|:-------:|:--------:|
|append(*value*)|Adds value to end of a list|
|sort()|Sorts the elements, ascending order (smallest value first). For descending order, use the `reverse` parameter.|
|reverse()|Reverses the order of a list.|
|count(*value*)|Returns the number of occurrences of value.|
|index(*value*)|Returns the first position number of where value occurs.|
|insert(*i*, *value*)|Inserts value at position i.|
|pop([*i*])|Returns value at position *i* and removes value from the list.|
|remove(value)|Removes the first occurrence of value from the list.|

## 5.2 When to use tuples and when to use lists

Lists can do everything tuples can and even more, since they are mutable sequences. But these are some of the 
advantages of tuples over lists:

1. **Tuples are faster than lists**: Because the computer knows they won't change. For simple programs this might not
make a difference but for larger problems it could be very useful.

2. **Safety and clarity**: Tuples are immutable, which makes them perfect for creating constants. This can add a 
level of safety and clarity to your code.

3. **Sometimes tuples are required**: For example, Python with certain functions or types requires immutable sequences.

But since lists are so flexible, it's probably best to use them rather than tuples the majority of the time.

## 5.3 Nested sequences

List and tuples are sequences of any type, this means that lists and tuples can contain other tuples and lists, this 
is what we refer to when we talk about **nested sequences**. Nested sequences are sequences inside other sequences.

### 5.3.1 Creating nested sequences

Creating nested sequences is done following the same rules we defined in previous chapters, for example:

```python
>>> ex_list = ["S1", ("S2", "S3"), ["S4", "S5", "S6"]]
>>> print(ex_list[0])
S1
>>> print(ex_list[1])
('S2', 'S3')
>>> print(ex_list[2])
['S4', 'S5', 'S6']
```

As you can see, the list `ex_list` has three elements:

1. The string `"S1"`.
2. The tuple with two elements: `("S2", "S3")`.
3. The list with three elements: `["S4", "S5", "S6"]`.

It is more common to find nested sequences that follow a consistent pattern, like this:

```python
>>> ex_list = [("Carlsberg", 2), ("Amstel", 4), ("Mahou", 10)]
>>> print(ex_list[0])
('Carlsberg', 2)
```

Also, you can create nested sequences inside nested sequences many times, however it can be confusing even for 
experienced programmers, usually you won't need more than one level of nesting. This is an example of four levels of 
nesting:

```python
crazy_tuple = ("T1", ("T2", ("T3" , ("T4", "T4"))))
```

### 5.3.2 Accessing nested elements

You access elements of a nested sequence just like with any other sequence, through indexing:

```python
>>> ex_list = [("Carlsberg", 2), ("Amstel", 4), ("Mahou", 10)]
>>> print(ex_list[0])
('Carlsberg', 2)
```

In case you want to access the element of a nested sequence, you can use an intermediate variable:

```python
>>> ex_list = [("Carlsberg", 2), ("Amstel", 4), ("Mahou", 10)]
>>> var = ex_list[0]
>>> print(var[0])
Carlsberg
```

Or you can use multiple indexing to access an element directly:

```python
>>> ex_list = [("Carlsberg", 2), ("Amstel", 4), ("Mahou", 10)]
>>> print(ex_list[0][0])
Carlsberg
```

A more elaborated example of multiple indexing is the following, in this case, we are using a nested sequence with 
four levels of nesting (the same as in the previous paragraph):

```python
>>> crazy_tuple = ("T1", ("T2", ("T3" , ("T4", "T4"))))
>>> print(crazy_tuple[0])
T1
>>> print(crazy_tuple[1])
('T2', ('T3', ('T4', 'T4')))
>>> print(crazy_tuple[1][0])
T2
>>> print(crazy_tuple[1][1])
('T3', ('T4', 'T4'))
>>> print(crazy_tuple[1][1][0])
T3
>>> print(crazy_tuple[1][1][1])
('T4', 'T4')
>>> print(crazy_tuple[1][1][1][0])
T4
>>> print(crazy_tuple[1][1][1][1])
T4
```

## 5.4 Unpacking a sequence

Unpacking means assigning each element of a sequence to a different variable, it works with any type of sequence and 
the number of elements in the sequence must be the same as the number of variables, otherwise an error is generated.

```python
>>> ex_list = [("Carlsberg", 2), ("Amstel", 4), ("Mahou", 10)]
>>> beer_name, beer_amount = ex_list[2]
>>> print(beer_name)
Mahou
>>> print(beer_amount)
10
```

## 5.5 Shared references

A variable refers to a value, this means that the variable doesn't store a copy of the value but just refers to the 
place in the computer's memory where the value is stored. For immutable types, this is not very important, but for 
mutable types, it is.

```python
# In this example, var refers to the location in memory where the string "Hey" is stored.
var = "Hey"
```

When several variable refer to the same mutable value, **they share the same reference**, which means that a change 
to that value through any of the variables means the value changes for all the variables. This can be better 
explained with an example:

```python
>>> beer_0 = ["Carlsberg"]
>>> beer_1 = beer_0
>>> beer_2 = beer_0
>>> beer_0[0] = "Soda"
>>> print(beer_0)
['Soda']
>>> print(beer_1)
['Soda']
>>> print(beer_2)
['Soda']
```

The important thing to note is to be aware of shared references when using mutable values, as if you change the value
through one of the variables, it will change for all of the variables. You can avoid this effect by just making a 
copy of the mutable object, one way to achieve it is by slicing:

```python
>>> beer_0 = ["Carlsberg"]
>>> beer_1 = beer_0[:]
>>> beer_2 = beer_0[:]
>>> beer_0[0] = "Soda"
>>> print(beer_0)
['Soda']
>>> print(beer_1)
['Carlsberg']
>>> print(beer_2)
['Carlsberg']
```

## 5.6 Dictionaries

Lists and tuples let your organize things into sequences, with *dictionaries* you store information in pairs. 
Compared to real dictionaries, where you look up a word to get its definition, in Python you look up a `key` and its 
`value`.

### 5.6.1 Creating a dictionary

To creaet a dictionary, you have to write a `key`, followed by a colon, followed by a `value`, all of this creates a 
dictionary `item`, you separate `items` with commas and enclosed all of them in curly brackets to create a dictionary
. As an example, the following code creates a dictionary:

```python
ex_dic = {0 : "Zero", 1 : "One", 2 : "Two", 3 : "Three", 4 : "Four", 5 : "Five"}
```

This code creates a dictionary of six pairs, called `items`. Each item is made of a `key` and a `value`, `keys` are on 
the left side of the colons and the `values` are on the right side of the colons. The table below serves as more 
clarification:

|Items|Keys|Values|
|:----:|:----:|:----:|
|0 : "Zero"|0|"Zero"|
|1 : "One"|1|"One"|
|2 : "Two"|2|"Two"|
|3 : "Three"|3|"Three"|
|4 : "Four"|4|"Four"|
|5 : "Five"|5|"Five"|

### 5.6.2 Operations with dictionaries

To add an `item` to a dictionary, you do the following:

```python
>>> ex_dic = {"Carlsberg" : "Tesco", "Mahou" : "Asda", "Estrella" : "Cooperative Food"}
>>> ex_dic["Bavaria"] = "Sansburys"
>>> print(ex_dic)
{'Carlsberg': 'Tesco', 'Estrella': 'Cooperative Food', 'Bavaria': 'Sansburys', 'Mahou': 'Asda'}
```

In case you attempt to do this with an already existing `key`, you replace the `value` associated with that `key`, 
for example:

```python
>>> ex_dic = {"Carlsberg" : "Tesco", "Mahou" : "Asda", "Estrella" : "Cooperative Food"}
>>> ex_dic["Estrella"] = "Spar"
>>> print(ex_dic)
{'Carlsberg': 'Tesco', 'Estrella': 'Spar', 'Mahou': 'Asda'}
```

To delete an item from a dictionary, you can use the `del` keyword, for example:

```python
del ex_dic["Carlsberg"]
```

It's important to note that trying to delete a dictionary item through a key that doesn't exist will give you an 
error, so it's better to know if the key you're using exists or not.

### 5.6.3 Accessing dictionary values

There are many ways to access a dictionary value. The most direct one is to use the `key` to retrieve the value, to 
get the `value` associated to a `key`, write they `key` in brackets right to the name of the dictionary, similar 
syntax to indexing, for example:

```python
>>> ex_dic = {"Carlsberg" : "Tesco", "Mahou" : "Asda", "Estrella" : "Cooperative Food"}
>>> ex_dic["Carlsberg"]
'Tesco'
```

In case you write a `key` that doesn't exist in the dictionary, python will return an error. In order to avoid this, 
you can use the `in` operator to check if the `key` is in the dictionary before trying to use to to access the 
`value`, for example:

```python
if "Carlsberg" in ex_dic:
  print("This is printed")
else:
  print("This is not printed")
```

Keep in mind that this only tests for `keys` in the dictionary, it doesn't check for values. Accessing through the 
`key` to the `value` looks similar to indexing, but it's important to note that dictionaries do not have position 
numbers and therefore indexing will give an error.

You can use the built-in method `get()` of dictionaries to get the value associated to a key without fear of writing 
a `key` that doesn't exist as this method has safety for those scenarios, for example:

```python
>>> ex_dic = {"Carlsberg" : "Tesco", "Mahou" : "Asda", "Estrella" : "Cooperative Food"}
>>> ex_dic.get("Carlsberg")
'Tesco'
>>> ex_dic.get("Amstel", "Will return this if key not found")
'Will return this if key not found'
```

If you specify a second argument for the `get()` method, it will return that argument if the `key` specified doesn't 
exist in the dictionary. If you don't supply a second argument and the `key` specified doesn't exist in the 
dictionary, the return value will be `None`.

### 5.6.4 Accessing dictionary keys

It's not possible to access dictionary keys through the values, that's all there is to it.

### 5.6.5 Dictionary requirements

These are things to keep in mind when using dictionaries:

1. **A dictionary can't contain multiple items with the same key**.
2. **Keys have to be immutable**
3. **Values don't have to be unique, they can be mutable or immutable.**

### 5.6.6 Dictionary summary of operations

The following table describes the most common dictionary methods:

|Methods|Description|
|:----:|:----:|
|get(key, [default])|Returns the value of `key` if it exists, otherwise the optional `default` is returned, or `None`.|
|keys()|Returns a view of all the keys in a dictionary.|
|values()|Returns a view of all the values in a dictionary.|
|items()|Returns a view of all the items in a dictionary.|

As you can see, we have introduced a new concept, `views`, views are dependent to the dictionary (If the dictionary 
changes the view will also change) and they can be iterated over with a `for` loop for example. As with dictionaries,
they can't be indexed.

# 6. Functions

**Functions** are ways to break up big programs into smaller and more manageable pieces of code. You will learn to do
the following:

- Write your own functions
- Accept values into your functions through parameters
- Return information from your functions through return values
- Work with global variables and constants
- Create a computer opponent that plays a strategy game

## 6.1 Creating functions

The functions `len()` and `range()` are examples of built-in functions, Python lets you create your own functions so 
you can better manage your code. Functions should do one job well.

By creating and using functions you using what is known as *abstraction*. It lets you think about the big picture 
without worrying about the details. 

A principal of *abstraction* is the *encapsulation*, in a function, no variable you create inside or any of its 
parameters can be accessed outside of the function, this is encapsulation, this helps keep independent code separated
and only the information that is needed by the function is passed and only information that is needed by the program 
is returned.

Another great thing about functions is that they can be *reused*, functions you write for some projects can be used 
in another projects as well, so writing good functions can save you time in your current projects and future 
projects, for more information about *software reuse*, read **Note 15**.

It's important to note that functions can be grouped into modules, that can be imported into your programs.

## 6.2 Defining a function

To define a function you use the `def` keyword, followed by your function name, and by a pair of parentheses with the
arguments enclosed, followed by a colon and by an indented block of statements. Naming functions follows the same 
rules as naming variables, you should try to use names that describe what the function does.

```python
def ex_function():
  print("This is an example function.")
```

The line with the `def` keyword and the block that follows are called a *function definition*. They define what the 
function does but no code is executed.

To call a function, you use a pair of parentheses, like this:

```python
>>> ex_function()
this is an example function
```

## 6.3 Documenting a function

Functions can be documented with what is called a documentation string, called a *docstring*, this is just a triple 
quoted string that must be the first line of the function. It appears in the interactive documentation in some IDEs.

```python
def ex_function():
  """ This is just an example function that prints a predefined text """
  print("this is an example function")
```

Now if I type `help(ex_function)`, in the command line I get the triple quoted string as a result, specifically:

```python
>>> help(ex_function)
Help on function ex_function:

ex_function()
    This is just an example function that prints a predefined text
```

## 6.4 Function parameters

Parameters are basically variables names inside the parentheses in a function, for example in this case:

```python
def ex_function(param1, param2):
  print("Param one value is : " + str(param1) + "\nParam two value is : " + str(param2))
```

In this case, `param1` and `param2` are *parameters*. Parameters exist only through the function and they are 
assigned the value of the arguments when a function is called, following from our previous example:

```python
>>> ex_function(1, "One")
Param one value is : 1
Param two value is : One
```

## 6.5 Return values

Functions that return values make use of the `return` statement, for example:

```python
def ex_function(param1, param2):
  sum = param1 + param2
  return sum
```

When a `return` line runs, the function passes the value to the part of the program that called it, and the function 
ends. So, a call to the function above results in the following:

```python
>>> ex_function(1, 2)
3
```

You can pass more than one return value in a function, but make sure that you have enough variables to store the 
returned information, for example:

```python
def ex_function(param1, param2):
  sum = param1 + param2
  return sum, param1, param2

>>> sum, param1, param2 = ex_function(1, 2)
>>> print(sum, param1, param2)
3 1 2
```

If there are not enough variables to store the returned values, an error will be generated.

## 6.6 Keyword arguments and default parameter values

When you just list parameters separated by commas in a function definition, you create *positional parameters*, for 
example:

```python
def ex_function(param1, param2):
  print(param1, param2)
```

When you call this function, with just arguments separated by commas, you create *positional arguments*, following 
from the previous example:

```python
>>> ex_function("arg1", "arg2")
arg1 arg2
```

*Positional arguments* and *positional parameters* are what we have defined so far, when these two are positional, it
means that the value of the parameters depends on the position of the arguments sent, the first parameter is assigned
the first argument, the second parameter is assigned the second argument... and so on.

Another possibility is to use keyword arguments, in this case you use the parameter names from the function 
definition to assign the value of the parameters, you can change the order of the assignments if you wish, for example:

```python
>>> ex_function(param1 = "arg1", param2 = "arg2")
arg1 arg2
>>> ex_function(param2 = "arg2", param1 = "arg1")
arg1 arg2
```

By using the parameter names you give clarity to your code, however it might get unnecesary long.You can combine both 
forms, but it is not advisable, as it gets tricky and confusing.

Finally, you can create parameters that are assigned default values in case they aren't assigned any values, for this
you just need to modify the function definition like this:

```python
def ex_function(param1, param2 = "No value passed for param2"):
  print(param1, param2)
```

Now, when you call the function, you can omit the second argument:

```python
>>> ex_function("arg1")
arg1 No value passed for param2
>>> ex_function("arg1", "arg2")
arg1 arg2
```

It's important to note that once you define a parameter as a default parameter, all the parameters that follow must 
be default parameters as well, otherwise Python will generate an error. Default parameters are useful when a function
gets called many times with the same one or more parameters.

## 6.7 Using global variables and constants

There is another way you can share information with functions other than parameters and return values, and these are 
global variables.

### 6.7.1 Scopes

*Scopes* represent the different areas of your program that are separate from each other. A program gets 
automatically a *global* scope, variables defined within this scope are called *global variables*, they can be 
accessed from anywhere within that scope.

When you create a function, you create another scope, variables defined within the function are only accessible in 
the scope of the function, these are *local variables* and, in this case, local to the function, however, global 
variables can still be accessed from inside the function.

### 6.7.2 Global variables and functions

As mentioned earlier, global variables can be accessed from inside a function, you can read its value but you can't 
change it directly, for example this code will work:

```python
global_var = 10

def ex_function():
  print(global_var)
```

But this one will not:

```python
global_var = 10

def ex_function():
  global_var = 5
```

For this last code to work, you need to use the `global` keyword inside the function, this way you it gains full 
access to the variable, this is the solution:

```python
global_var = 10

def ex_function():
  global global_var
  global_var = 5
```

It's important to note that if you create inside a function a local variable with the same name as a global variable,
the local variable has preference, this means that you *shadow* the global variable, the operations you do on the 
variable only affect the local variable inside the function.

### 6.7.3 When to use global variables and constants

Global variables make programs confusing, because its hard to keep track of where the global variable might change, 
on the other hand, global constants make the program gain clarity, for example, imagine a program where you have to 
use in many places a constant value, instead of repeating it over and over, you can just use a global constant.

# 7. Files and exceptions

In this chapter you will learn how to use files for permanent storage and how to handle errors that your code may 
generate. Specifically, you will learn to do the following:

- Read from text files
- Write to text files
- Read and write more complex data with files
- Intercept and handle errors during a program's execution

## 7.1 Opening and closing a file

The first step to work with a file is to open it, using the `open()` function. This function takes two arguments, the 
first one is path to the file. Python first looks in the current directory for the file if no full path is specified.

The second one is the access permisions, which can be any from the following table:

|Mode|Description|
|:------:|:------:|
|"r"|Read from a text file. If the file doesn't exist, Python will complain with an error|
|"w"|Write to a text file. If the file exists, its contents are overwritten. If the file doesn't exist, it's created.|
|"a"|Append a text file. If the file exists, new data is appended to it. If the file doesn't exist, it's created.|
|"r+"|Read from and write to a text file. If the file doesn't exist, Python will complain with an error.|
|"w+"|Write to and read from a text file. If the file exists, its contents are overwritten. If the file doesn't exist, it's created|
|"a+"|Append and read from a text file. If the file exists, new data is appended to it. If the file doesn't exist, it's created.|

This function then returns a `file` object, which includes many useful methods. This is an example of opening a file:

```python
>>> text_file = open("text_file.txt", "r")
```

Once you finish working with a file, it's a good programming practice to close it, you can do it with the following 
method of the `file` object.

```python
>>> text_file.close()
```

## 7.2 Reading from a text file

It's easy to read strings from 'plain text files', they are the same under Windows, Mac or Unix and these operating 
systems come with tools to edit them.

### 7.2.1 Reading characters from a file

To read characters from a file you use the `read()` method of a `file` object, the `read()` method accepts one 
argument which tells it the number of characters to read from the file, if this parameter is not specified, the whole
file will be returned as a string:

```python
>>> route = "dat.txt"
>>> file_obj = open(route, "r+")
>>> print(file_obj.read(4))
Firs
>>> print(file_obj.read(4))
t li
>>> file_obj.close()
```

It is important to note that each time you use the `read()` method the read pointer advances the same number of 
positions as the amount of characters read, to reset the pointer, you can close and open the file again using the 
functions seen before. Any subsequent reads after there is no more data to read will just return the empty string.

### 7.2.2 Reading characters from a line

Sometimes you just want to work with lines, for this you use the `readline()` method. In this method, you specify the
number of characters you want to read from the current line, as before, if you don't pass a number it will return the
whole line.

```python
>>> route = "dat.txt"
>>> file_obj = open(route, "r+")
>>> print(file_obj.readline(4))
Firs
>>> print(file_obj.readline(100))
t line

>>> print(file_obj.readline(100))
Second line

>>> file_obj.close()
```

As you can see, once a complete line has been read, it continues with the next line.

### 7.2.3 Reading all the lines into a list

You can read all the lines from a file and create a list with them using hte `readlines()` method. Each line becomes 
a string object inside the list, for example:

```python
>>> route = "dat.txt"
>>> file_obj = open(route, "r+")
>>> print(file_obj.readlines())
['First line\n', 'Second line\n', 'Third line\n']
>>> file_obj.close()
```

### 7.2.4 Looping through a file

When using a `file` object as a condition in a loop, it returns the lines of the associated text file in succession, 
for example:

```python
>>> route = "dat.txt"
>>> file_obj = open(route, "r+")
>>> for a in file_obj:
...     print(a)
...     
First line

Second line

Third line
>>> file_obj.close()
```

## 7.3 Writing to a text file

There are two basic ways to write strings to a text file.

### 7.3.1 Writing strings to a file

Just as before, the file needs to be opened with correct access permissions, then you use the `write()` operator to 
write strings to the file:

```python
>>> route = "tad.txt"
>>> file_obj = open(route, "w")
>>> file_obj.write("Write this, and just this")
>>> file_obj.close()
```

As you write things on the file, the write pointer advances. You can also use the `writelines()` method to write a list
of strings to the file, this will be written in succession:

```python
>>> route = "tad.txt"
>>> file_obj = open(route, "w")
>>> list = ["This is a text", "This is another text", "How surprising, this is more text"]
>>> file_obj.writelines(list)
>>> file_obj.close()
```

## 7.4 Reading and writing to a text file summary

This table summarizes every method seen regarding writing to and reading from a text file:

|Method|Description|
|:----|:----|
|`close()`|Closes the file. A closed file cannot be read from or written to until opened again.|
|`read([size])`|Reads *size* characters from a file and returns them as a string. If size is not specified, the method returns all of the characters from the current position to the end of the file.|
|`readline([size])`|Reads size characters from the current line in a file and returns them as a string. If size is not specified, the method returns all of the characters from the current position to the end of the file.|
|`readlines()`|Reads all of the lines in a file and returns them as elements in a list.|
|`write(output)`|Writes the string output to a file.|
|`writelines(output)`|Writes the strings in the list output to a file.|

## 7.5 Storing data in binary files

Python allows to store complex data in a single file that you can retrieve later, for examples lists or dictionaries.

There are two modules that are important regarding this:

- The *pickle* module allows you to preserve and store complex data in a file.
- The *shelve* module allows you to store and randomly access pickled objects in a file.

### 7.5.1 Pickling data and writing/reading to a file

Pickling is very similar to writing characters to a file, but instead of characters you write objects and retrieve 
them sequentially from the file. For this to work, the file must be opened as a binary file, using any of the 
following parameters as the access mode:

|Mode|Description|
|:----|:----|
|"rb"|Read from a binary file. If the file doesn't exist, Python will complain with an error.|
|"wb"|Write to a binary file. If the file exists, its contents are overwritten. If the file doesn't exist, it's created.|
|"ab"|Append a binary file. If the file exists, new data is appended to it. If the file doesn't exist, it's created.|
|"rb+"|Read from and write to a binary file. If the file doesn't exist, Python will complain with an error.|
|"wb+"|Write to and read from a binary file. If the file exists, its contents are overwritten. If the file doesn't exist, it's created.|
|"ab+"|Append and read from a binary file. If the file exists, new data is appended to it. If the file doesn't exist, it's created.|

The *pickle* module has a method called *dump()*, which can be used to write complex data to a binary file, this 
function requires two arguments, the data to pickle and the file object associated to the file where to store it. As 
an example:

```python
import pickle

file_loc = "C:\\Users\\Diego\\Desktop\\Learning Python\\Chapter 6 - Functions\\tad.txt"
file_obj = open(file_loc, "wb+")

ex_list = ["List 1", "List 2", "List 3"]
ex_tuple = ("Tuple 1", "Tuple 2", "Tuple 3")
ex_dic = {"Key 1": 40, "Key 2": 50, "Key 3": 60} 

pickle.dump(ex_list, file_obj)
pickle.dump(ex_tuple, file_obj)
pickle.dump(ex_dic, file_obj)
file_obj.close()
```

To read these elements, you use the `load()` method of the *pickle* module, it retrieves the pickled elements 
sequentially. Following from our previous example:

```python
>>> import pickle
>>> file_loc = "tad.txt"
>>> file_obj = open(file_loc, "rb+")
>>> ex_list = pickle.load(file_obj)
>>> ex_tuple = pickle.load(file_obj)
>>> ex_dic = pickle.load(file_obj)
>>> file_obj.close()
['List 1', 'List 2', 'List 3']
>>> print(ex_list)
>>> print(ex_tuple)
('Tuple 1', 'Tuple 2', 'Tuple 3')
>>> print(ex_dic)
{'Key 2': 50, 'Key 3': 60, 'Key 1': 40}
```

This table is a summary of what we have seen regarding pickling data:

|Function|Description|
|:------|:------|
|`dump(object, file, [,bin])`|Writes pickled version of `object` to `file`. If `bin` is `True`, `object` is written in binary format. If `bin` is `False`, it is written in a less efficient but readable format. The default value for this parameter is false.|
|`load(file)`|Unpickles and returns the next pickled object in `file`.|

### 7.5.2 Random access and pickling

Using the `shelve` module, you can randomly access pickled data. You creata `shelf` that acts like a dictionary, but 
with pickled objects and files.

Instead of the `open()` function, you use the `open()` method of the `shelve` module. This method takes two 
arguments, first the file location and then the access mode, which can be one of the following:

|Mode|Description|
|:-----|:-----|
|`"c"`|Open a file for reading or writing, if the files doesn't exist, it's created.|
|`"n"`|Create a new file for reading or writing, if the file exists, its contents are overwritten.|
|`"r"`|Read from a file. If the file doesn't exist, Python will complain with an error.|
|`"w"`|Write to a file. If the file doesn't exist, Python will complain with an error.|

By default, the access mode is `"c"`. This is an example on how to use a `shelf`:

```python
>>> import shelve
>>> file_loc = "asd.txt"
# Create the shelf.
>>> s = shelve.open("file_loc", "n")
# Add key : value pairs to the shelf.
>>> s["Colours"] = ("Red", "White", "Black")
>>> s["Feelings"] = ["Angry", "Happy", "Deluded"]
>>> s["Sports"] = {"Football": "Real Madrid", "Basketball": "Lakers"}
# Write everything to the file.
>>> s.sync()
# Retrieve a random object from the file using the key.
>>> ex_feelings = s["Feelings"]
>>> print(ex_feelings)
['Angry', 'Happy', 'Deluded']
# Close the file.
>>> s.close()
```

Regarding the `sync()` method, it is used to flush the buffer of data to the file, otherwise it is done periodically. 
When calling the `close()` method, the same effect is achieved.

It is important to note that when opening a file with the `open()` method of the shelve module, Python might add an 
extension to the file and create additional files, this behaviour is normal. Also, shelf keys can only be strings.

## 7.6 Exceptions

When Python runs into an error, it raises an **exception**. If nothing is done with the exception, it stop what it's 
doing and displays an error message detailing the exception.

With Python exception handling, you can catch and handle exceptions so that your program doesn't crash.

### 7.6.1 The try statement

The most basic way to handle exceptions is to use the *try* statement along with the *except* clause. You use the 
*try* statement for statements that can raise an exception, for example statements that involve external interaction,
and if an exception is raised, the except clause's associated block of statements is executed. This is an example of 
the try statement:

```python
num = A
try:
  num_f = float(num)
except:
  print("Something went wrong when converting to float.")
```

In this code, the *except* clause covers all the exceptions that might be raised, this is usually not a good 
programming practice, each exception should be handled individually. 

### 7.6.2 Exception types

There are many different kinds of exceptions, some are summarized in the following table:

|Exception Type|Description|
|:-----:|:-----|
|`IOError`|Raised when an I/O operation fails, such as when an attempt is made to open a nonexistent file in read mode.|
|`IndexError`|Raised when a sequence is indexed with a number of a nonexistent element.|
|`KeyError`|Raised when a dictionary key is not found.|
|`NameError`|Raised when a name of an object is not found.|
|`SyntaxError`|Raised when a syntax error is encountered.|
|`TypeError`|Raised when a built-in operation or function is applied to an object of inappropriate type.|
|`ValueError`|Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.|
|`ZeroDivisionError`|Raised when the second argument of a division or module operation is zero.|

The *except* clause allows the programmer to catch certain types of exceptions, for example and following from our 
previous piece of code:

```python
num = A
try:
  num_f = float(num)
except ValueError:
  # We can be more specific about what to print, since we are handling a particular type of exception.
  print("The value that you tried to convert is invalid.")
```

You can also handle multiple exception types with just an *except* clause separating them by commas and enclosing in 
parentheses (like a tuple):

```python
num = A
try:
  num_f = float(num)
except (TypeError, ValueError):
  print("The value that you tried to convert is invalid.")
```

Or you can just write multiple exception clauses for the different exceptions you want to handle, there is no limit 
to the number of except clauses in a try statement.

### 7.6.3 Treating an exception as an argument

You can get the value of an exception using the `as` keyword in an `except` clause, following from our previous code:

```python
num = A
try:
  num_f = float(num)
except ValueError as ex_exception:
  print("This is what the exception has to say: ")
  print(ex_exception)
```

The associated value to an exception is usually a text describing the exception.

### 7.6.4 The else clause

You can use the `else` clause in try statements to execute a block of statements in case no exception was raised, 
following from our previous example:

```python
num = A
try:
  num_f = float(num)
except ValueError:
  print("The value that you tried to convert is invalid.")
except TypeError:
  print("There was an error in the types while converting.")
else:
  print("Everything went fine, change the variable num to a number and I will be printed".)
```

So, the block of statements of the `else` clause will be executed only if the try block of statements is successful.

# 20. Notes

**Note 1**: Python is case-sensitive and by convention, function names are in lowercase.

**Note 2**: Save your programs with the `.py` extension, this allows various applications to recognize these files as
Python programs.

**Note 3**: When you have a list of arguments, you can start a new line after any of the comma separators in the 
list, for example:

```python
>>> print("line 1",
          "line 2",
          "line 3")
line 1 line 2 line 3
```

This can make your code easier to read.

**Note 4**: Using the *line continuation character* `\` you can span a single statement across multiple lines, which 
can be useful to improve your readability.

```python
>>> print("Using \
the line \
continuation character")
Using the line continuation character
```

**Note 5**: Self-documenting code is writing code in a way that is easy to understand for other programmers, you 
should strive to write self-documented code.

**Note 6**: Using the same function, operator or the like for values of different types is called *overloading*. For 
example, the plus sign can be used to sum integers or to concatenate strings.

**Note 7**: Putting one function inside another is called nesting functions, this is perfectly fine as long as the 
return value of the inner function can be used by the outer function.

**Note 8**: Modules are files that contain code meant to be used in other programs. Modules need to be imported in 
your program using the `import` statement, then you can access its members using the dot notation. For example:

```python
import random
random.randint(1, 10)
```

**Note 9**: Blocks are a collection of one single statement or multiple consecutive statements indented by the same 
amount of spaces, thus creating a logical unit.

**Note 10**: Indentation can be done with tabs or spaces, it is advisable to use spaces and by consistent with it, 
either two or four, depending on your coding style.

**Note 11**: You can treat any value as a condition, every value, of any type, can be treated as a `True` or `False`.
The principal rule is that any empty or zero value evaluates as `False` while any other value evaluates to `True`. 
For example:

```python
var1 = 10
var2 = 0
if var1:
  print("var1 evaluates to True")
if var2:
  print("var2 evaluates to False")
```

**Note 12**: For more information about the `range()` function, check the following [link](http://www.pythoncentral
.io/pythons-range-function-explained/).

**Note 13**: In Python there isn't a simple way to create constants, a common convention among experienced 
programmers is to create variables names in all caps, however nothing stops you from changing the value of that 
variable. An example of a constant following this convention could be the following:

```python
PI = 3.1416
```

**Note 14**: The keyword `None` is the equivalent to nothing in Python, it can be used to initialize variables for 
example. As is expected, it evaluates to `False` when used as a condition.

**Note 15**: Software reuse is basically not reinventing the wheel, it consists using existing software and other 
project elements in new projects. With software reuse, you can do the following:

1. Increase company productivity, by reusing code the amount of effort decreases.
2. Improve sofware quality, tested pieces of code can be reused knowing that they are bug free.
3. Consistency accross software products, for example sharing user interfaces can make the user feel comfortable with
new programs right out the box.
4. Improve software performance, once a company has a good way of doing something through software, using it again 
saves the trouble of reinventing the wheel, or even worse, of inventing a less efficient wheel.

**Note 16**: When you pass mutable values as arguments to functions be careful not to change its value (unless this is 
intended) as the change will remain after exiting the function. This is considered a *side effect* and it is 
generally frowned upon, you should use return values to communicate with your application.

**Note 17**: If you want to terminate execution, you can call the `sys.exit()` method, which raises an exception that
which results in the end of the program. You must import the `sys` module first.