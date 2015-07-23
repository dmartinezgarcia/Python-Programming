# 0. Python-Programming
Python Programming, Third Edition by Michael Dawson

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
|upper()|Returns the uppercase version of the string|
|lower()|Returns the lowercase version of the string|
|swapcase()|Returns a new string where each uppercase character becomes lowercase and vice versa|
|capitalize()|Returns a new string where the first character is capitalized and the rest are lowercase|
|title()|Returns a new string where the first character of each word is capitalized and the rest are lowercase|
|strip()|Returns a string where all the tabs, spaces and new lines at the beginning and the end of the string are removed|
|replace(*old*, *new*, [,*max*])|Returns a string where all the *old* occurrences are replaced with the *new* ones, the optional argument *max* limits the number of replacements.|

## 2.5 Conversion between types

These are the functions that convert values to a specific type:

|Function|Description|Example|Result|
|:-|:-|:-|:-|
|`float(*x*)`|Returns the floating-point value associated to *x*|`float("10.0")`|10.0|
|`int(*x*)`|Returns the integer value associated to *x*|`int("10")`|10|
|`str(*x*)`|Returns the string value associated to *x*|`str(10)`|"10"|

## 2.6 Augmented assignment operators

These are just a shortcut for a calculation and assignment operation, the ones in this table are the ones related to 
the arithmetical operators:

|Operator|Example|Is equivalent to|
|:-|:-|:-|
|\*=|a \*= 10|a = a \* 10|
|/=|a /= 10|a = a / 10|
|%=|a %= 10|a = a % 10|
|+=|a += 10|a = a + 10|
|-=|a -= 10|a = a - 10|

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