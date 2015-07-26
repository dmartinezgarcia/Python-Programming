# 0. Python-Programming
Book: **Python Programming**, Third Edition by Michael Dawson

This repository contains the solutions to the exercises and my own notes intended to be used for quick 
reference or for future reference in case I forget something.

So far the repository contains notes and exercises for the following topics:

- Chapter 1: Getting started
- Chapter 2: Types, variables and simple I/O
- Chapter 3: Branching and while loops
- Chapter 4: For loops, strings and tuples

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


