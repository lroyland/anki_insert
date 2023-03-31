import requests

def invoke(action, **params):
    request_data = {'action': action, 'params': params, 'version': 6}
    response = requests.post('http://localhost:8765', json=request_data)
    return response.json()

def create_deck(deck_name, main_deck, subdeck):
    full_deck_name = f'{main_deck}::{subdeck}::{deck_name}'
    result = invoke('createDeck', deck=full_deck_name)
    return full_deck_name

def add_card_to_deck(deck_name, front, back):
    note = {
        'deckName': deck_name,
        'modelName': 'Basic',
        'fields': {
            'Front': front,
            'Back': back
        },
        'options': {
            'allowDuplicate': False
        },
        'tags': []
    }
    result = invoke('addNote', note=note)

main_deck = "Intro to Computation and Programming Using Python"

subdeck1 = "2.1.1 Objects, Expressions, and Numerical Types"
subdeck2 = "2.1.2 Variables and Assignment"
subdeck3 = "2.1.3 Python IDE’s"
subdeck4 = "2.2 Branching Programs"
subdeck5 = "2.3.1 Input"
subdeck6 = "2.3.2 A Digression About Character Encoding"
subdeck7 = "2.4 Iteration"
subdeck8 = "3.1 Exhaustive Enumeration"
subdeck9 = "3.2 For Loops"
subdeck10 = "3.3 Approximate Solutions and Bisection Search"
subdeck11 = "3.4 A Few Words About Using Floats"
subdeck12 ="3.5 Newton-Raphson"
subdeck13 = "4 FUNCTIONS, SCOPING, AND ABSTRACTION"
subdeck14 = "4.1 Functions and Scoping"
subdeck15 = "4.1.1 Function Definitions"
subdeck16 = "4.1.2 Keyword Arguments and Default Values"
#subdeck17 = "4.1.3 Scoping"

""" deck1 = create_deck("Deck1", main_deck, subdeck1)
deck2 = create_deck("Deck2", main_deck, subdeck2)
deck3 = create_deck("Deck3", main_deck, subdeck3)
deck4 = create_deck("Deck4", main_deck, subdeck4)
deck5 = create_deck("Deck5", main_deck, subdeck5)
deck6 = create_deck("Deck6", main_deck, subdeck6)
deck7 = create_deck("Deck7", main_deck, subdeck7)
deck8 = create_deck("Deck8", main_deck, subdeck8)
deck9 = create_deck("Deck9", main_deck, subdeck9)
deck10 = create_deck("Deck10", main_deck, subdeck10)
deck11 = create_deck("Deck11", main_deck, subdeck11)
deck12 = create_deck("Deck12", main_deck, subdeck12)
deck13 = create_deck("Deck13", main_deck, subdeck13) """

decks = [create_deck(f"Deck{i}", main_deck, globals()[f'subdeck{i}']) for i in range(1, 17)]


cards_deck1 = [
    # Add your cards for subdeck1 here, for example:
    {"front": "What are scalar objects in Python?", "back": "Indivisible objects, like the atoms of the language"},
    {"front": "What are non-scalar objects in Python?", "back": "Objects with internal structure, like strings"},
    {"front": "What is a literal in Python?", "back": "A notation for representing a fixed value in the source code"},
    {"front": "What are the four types of scalar objects in Python?", "back": "int, float, bool, None"},
    {"front": "What is the int type in Python?", "back": "A type used to represent integers"},
    {"front": "What is the float type in Python?", "back": "A type used to represent real numbers"},
    {"front": "Why is the float type not called 'real'?", "back": "Because float values are stored as floating-point numbers, which can behave differently from real numbers in certain situations"},
    {"front": "What is the bool type in Python?", "back": "A type used to represent the Boolean values True and False"},
    {"front": "What is the None type in Python?", "back": "A type with a single value, used to represent the absence of a value"},
    {"front": "How can you find out the type of an object in Python?", "back": "Using the built-in 'type()' function"},
    {"front": "What do arithmetic operators have?", "back": "Usual precedence, e.g., * binds more tightly than +"},
    {"front": "How can you change the order of evaluation in Python expressions?", "back": "By using parentheses to group subexpressions"},
    {"front": "What are the three primitive operators on type bool?", "back": "and, or, not"},
    {"front": "When does 'a and b' evaluate to True in Python?", "back": "When both a and b are True"},
    {"front": "When does 'a or b' evaluate to True in Python?", "back": "When at least one of a or b is True"},
    {"front": "When does 'not a' evaluate to True in Python?", "back": "When a is False"},
    {"front": "What is the result of the '==' operator in Python?", "back": "A bool value, either True or False"},
    {"front": "What is the result of the '!=' operator in Python?", "back": "A bool value, either True or False"},
    {"front": "What is the purpose of the 'not' operator in Python?", "back": "To negate a Boolean value"},
    {"front": "What are the two comparison operators in Python?", "back": "== and !="},
    {"front": "What do the comparison operators return in Python?", "back": "A bool value, either True or False"},
    # ...
]

cards_deck2 = [
    # Add your cards for subdeck2 here, for example:

    {"front": "What are variables in Python?", "back": "Variables in Python are just names that provide a way to associate names with objects."},
    {"front": "What is the purpose of an assignment statement in Python?", "back": "An assignment statement associates the name to the left of the '=' symbol with the object denoted by the expression to the right of the '='."},
    {"front": "Can an object in Python have multiple names?", "back": "Yes, an object can have one, more than one, or no name associated with it."},
    {"front": "Are Python variable names case-sensitive?", "back": "Yes, Python variable names are case-sensitive."},
    {"front": "What characters can Python variable names contain?", "back": "Python variable names can contain uppercase and lowercase letters, digits (but they cannot start with a digit), and the special character '_'."},
    {"front": "What are the reserved words in Python 3?", "back": "Reserved words in Python 3 include and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, nonlocal, None, not, or, pass, raise, return, True, try, while, with, and yield."},
    {"front": "How do you add comments in Python?", "back": "In Python, you can add comments by using the '#' symbol. Text following this symbol is not interpreted by Python."},
    {"front": "How does multiple assignment work in Python?", "back": "Multiple assignment in Python allows you to bind multiple variables to multiple values in a single statement. For example, 'x, y = 2, 3' binds x to 2 and y to 3."},
    {"front": "How can you use multiple assignment to swap the bindings of two variables?", "back": "You can use multiple assignment to swap the bindings of two variables like this: 'x, y = y, x'."},
    {"front": "How do variable names affect the readability of code?", "back": "Apt choice of variable names plays an important role in enhancing the readability of code."},
    {"front": "What is the role of a variable in the code 'pi = 3.14159'?", "back": "In this code, 'pi' is a variable that is assigned the value 3.14159."},
    {"front": "What is the effect of the assignment 'radius = 14' on the value of 'area'?", "back": "The assignment 'radius = 14' has no effect on the value of 'area'."},
]
    # ...

cards_deck3 = [
    {"front": "Why is typing programs directly into the shell inconvenient?", "back": "Typing programs directly into the shell is inconvenient because it lacks features like syntax highlighting, auto-completion, smart indentation, and debugging tools that are available in an integrated development environment (IDE)."},
    {"front": "What is an integrated development environment (IDE)?", "back": "An integrated development environment (IDE) is a software application that provides comprehensive facilities to computer programmers for software development. It typically includes a text editor, a shell, and an integrated debugger."},
    {"front": "What is IDLE?", "back": "IDLE is an integrated development environment (IDE) for Python that comes as part of the standard Python installation package."},
    {"front": "What are some popular Python IDEs?", "back": "Some popular Python IDEs include IDLE, Anaconda, and Canopy."},
    {"front": "What are the common features provided by Python IDEs?", "back": "Python IDEs commonly provide a text editor with syntax highlighting, auto-completion, and smart indentation, a shell with syntax highlighting, and an integrated debugger."},
    {"front": "What is the purpose of the file menu in a Python IDE?", "back": "The file menu in a Python IDE allows you to create new editing windows, open existing Python program files, and save the contents of the current editing window into a file with the .py extension."},
    {"front": "What is the purpose of the edit menu in a Python IDE?", "back": "The edit menu in a Python IDE includes standard text-editing commands (e.g., copy, paste, and find) plus some commands specifically designed to make it easy to edit Python code (e.g., indent region and comment out region)."},
    {"front": "Where can you find more information about IDLE?", "back": "You can find more information about IDLE at http://docs.python.org/library/idle.html/."},
    {"front": "Where can you find more information about Anaconda?", "back": "You can find more information about Anaconda at https://store.continuum.io/cshop/anaconda/."},
    {"front": "Where can you find more information about Canopy?", "back": "You can find more information about Canopy at https://www.enthought.com/products/canopy/."},
]

cards_deck4 = [
    {"front": "What are straight-line programs?", "back": "Straight-line programs are programs that execute one statement after another in the order in which they appear and stop when they run out of statements. They do not have any branching or looping constructs."},
    {"front": "What are branching programs?", "back": "Branching programs are more complex than straight-line programs as they include conditional statements that allow the program to execute different blocks of code depending on the outcome of a test."},
    {"front": "What are the three parts of a conditional statement?", "back": "A conditional statement has three parts: 1) a test that evaluates to True or False, 2) a block of code executed if the test evaluates to True, and 3) an optional block of code executed if the test evaluates to False."},
    {"front": "What does 'elif' stand for in Python?", "back": "'elif' stands for 'else if' in Python and is used for specifying additional conditions in a conditional statement."},
    {"front": "What is a compound Boolean expression?", "back": "A compound Boolean expression is a combination of two or more Boolean expressions joined by logical operators such as 'and' or 'or'."},
    {"front": "What is constant time in the context of program execution?", "back": "A program is said to run in constant time if the maximum running time is bounded by the length of the program, meaning there exists a constant, k, such that the program is guaranteed to take no more than k steps to run, regardless of the input size."},
    {"front": "What are objects of type 'str' used for?", "back": "Objects of type 'str' are used to represent strings of characters."},
    {"front": "How are string literals denoted in Python?", "back": "String literals in Python can be written using either single or double quotes, e.g., 'abc' or \"abc\"."},
    {"front": "What is the purpose of the '+' operator when applied to strings?", "back": "The '+' operator, when applied to strings, is used for concatenation, combining two strings together."},
    {"front": "What is the purpose of the '*' operator when applied to an integer and a string?", "back": "The '*' operator, when applied to an integer and a string, acts as a repetition operator, creating a new string with the original string repeated a specified number of times."},
    {"front": "What is zero-based indexing?", "back": "Zero-based indexing is a system where the first element of a sequence, such as a string or a list, is assigned the index 0, the second element has the index 1, and so on."},
    {"front": "What is slicing in the context of strings?", "back": "Slicing is a technique used to extract substrings of arbitrary length from a string. If 's' is a string, the expression 's[start:end]' denotes the substring of 's' that starts at index 'start' and ends at index 'end-1'."},
]

cards_deck5 = [
    {"front": "What is the 'input' function in Python 3?", "back": "The 'input' function in Python 3 is used to get input directly from a user. It takes a string as an argument, displays it as a prompt in the shell, and waits for the user to type something followed by hitting the enter key. The input is treated as a string and becomes the value returned by the function."},
    {"front": "How does the 'print' function handle multiple arguments?", "back": "When the 'print' function is given multiple arguments, it places a blank space between the values associated with the arguments."},
    {"front": "How is the input from the 'input' function treated?", "back": "The input from the 'input' function is treated as a string, regardless of whether the input is a number or text."},
    {"front": "What are type conversions (type casts)?", "back": "Type conversions (type casts) are used to convert values from one data type to another. In Python, you can use the name of a type to convert values to that type."},
    {"front": "How do you convert a string to an integer in Python?", "back": "To convert a string to an integer in Python, use the 'int()' function, e.g., 'int(\"3\")'."},
    {"front": "What happens when a float is converted to an int in Python?", "back": "When a float is converted to an int in Python, the number is truncated, not rounded. For example, 'int(3.9)' results in the integer '3'."},
    {"front": "What is the '+' operator's behavior with strings?", "back": "The '+' operator is overloaded for strings and is used for concatenation."},
    {"front": "What is the '*' operator's behavior when applied to an int and a str?", "back": "The '*' operator, when applied to an int and a str, becomes a repetition operator. The expression 'n * s', where 'n' is an int and 's' is a str, evaluates to a str with 'n' repeats of 's'."},
    {"front": "What is the result of comparing a string and a number using the '<' operator in Python 3?", "back": "In Python 3, comparing a string and a number using the '<' operator generates an error message, since such expressions don't have an obvious meaning."},
]

cards_deck6 = [
    {"front": "What is ASCII?", "back": "ASCII (American Standard Code for Information Interchange) is a character encoding standard that uses a set of 128 characters, sufficient for representing common characters in English-language text but not for all the world's languages."},
    {"front": "What is Unicode?", "back": "Unicode is a character coding system designed to support the digital processing and display of written texts of all languages. It contains more than 120,000 different characters, covering 129 modern and historic scripts and multiple symbol sets."},
    {"front": "How can you specify the character encoding in a Python program?", "back": "You can specify the character encoding in a Python program by inserting a comment of the form '# -*- coding: encoding name -*-' as the first or second line of your program."},
    {"front": "What is the most frequently used character encoding for World Wide Web pages?", "back": "UTF-8 is the most frequently used character encoding for World Wide Web pages."},
    {"front": "What is the default character encoding in most Python implementations?", "back": "In most Python implementations, the default character encoding is UTF-8."},
    {"front": "Can you use non-English characters in Python strings?", "back": "Yes, you can use non-English characters in Python strings when using Unicode character encoding like UTF-8."},
    {"front": "How can you include non-English characters in a Python program?", "back": "To include non-English characters in a Python program, ensure you are using a Unicode-compatible character encoding like UTF-8. You can then type the characters directly or copy them from a source like a web page and paste them into your program."},
]

cards_deck7 = [
    {"front": "What is iteration in programming?", "back": "Iteration is a process of repeatedly executing a set of statements, also known as looping. It is used when a program needs to perform the same task multiple times."},
    {"front": "What is a while loop in Python?", "back": "A while loop in Python is a control flow statement that allows code to be executed repeatedly as long as a given condition is True. When the condition becomes False, the loop terminates."},
    {"front": "How do you create a while loop in Python?", "back": "In Python, you create a while loop using the 'while' keyword followed by a condition, and then the loop body indented under the while statement."},
    {"front": "What does the 'break' statement do in a loop?", "back": "The 'break' statement in a loop terminates the loop in which it is contained and transfers control to the code immediately following the loop."},
    {"front": "How can you exit a loop without testing the loop condition?", "back": "You can exit a loop without testing the loop condition by using a 'break' statement inside the loop. When the break statement is executed, the loop terminates."},
    {"front": "What happens when a break statement is executed inside a nested loop?", "back": "When a break statement is executed inside a nested loop, it terminates the inner loop and control proceeds to the outer loop."},
]

cards_deck7_extended = [
    {"front": "What is hand-simulation in programming?", "back": "Hand-simulation is a technique to understand a program's behavior by manually executing the code using pencil and paper or a text editor, pretending to be the interpreter."},
    {"front": "How do you square a number using a while loop?", "back": "You can square a number using a while loop by performing repetitive addition. Initialize a variable 'ans' to 0, a variable 'itersLeft' to the value of the number, and add the number to 'ans' while decrementing 'itersLeft' until it reaches 0."},
    {"front": "What happens when a while loop has a negative value in the loop condition?", "back": "When a while loop has a negative value in the loop condition, it may cause an infinite loop if the loop condition does not eventually become False."},
    {"front": "Write a while loop that prints the letter 'X' a specified number of times.", "back": "```python\nnumXs = int(input('How many times should I print the letter X? '))\ntoPrint = ''\nwhile numXs > 0:\n    toPrint += 'X'\n    numXs -= 1\nprint(toPrint)```"},
    {"front": "Write a program that finds the smallest positive integer divisible by both 11 and 12.", "back": "```python\nx = 1\nwhile True:\n    if x % 11 == 0 and x % 12 == 0:\n        break\n    x += 1\nprint(x, 'is divisible by 11 and 12')```"},
]

cards_deck7 += cards_deck7_extended

cards_deck8 = [
    {
        'front': 'What is the algorithmic technique used in the cube root program?',
        'back': 'Exhaustive enumeration'
    },
    {
        'front': 'What is a decrementing function?',
        'back': 'A decrementing function is a function that maps a set of program variables into an integer, is nonnegative when the loop is entered, has a value less than or equal to 0 when the loop terminates, and decreases its value with every iteration of the loop.'
    },
    {
        'front': 'Why is exhaustive enumeration often a practical way to solve a problem?',
        'back': 'Exhaustive enumeration algorithms are often practical because they are typically easy to implement and understand, and in many cases, they run fast enough for all practical purposes.'
    },
    {
        'front': 'How long does it take for a modern computer to execute an instruction?',
        'back': 'On the order of one nanosecond, or one billionth of a second.'
    },
    {
        'front': 'How can you test whether a decrementing function is being decremented in a non-terminating loop?',
        'back': 'Experienced programmers often insert print statements inside the loop to check if the decrementing function is indeed decreasing with each iteration.'
    },
    {
        'front': 'What happens when you run the cube root program with a negative value for x?',
        'back': 'The program will enter an infinite loop, as the value of itersLeft will move farther from 0 rather than closer to it with each iteration.'
    },
    {
        'front': 'What is the decrementing function for the while loop in the cube root program (Figure 3.1)?',
        'back': 'The decrementing function for the while loop in the cube root program is abs(x) - ans**3.'
    }
]

cards_deck9 = [
    {
        'front': 'What is the general form of a for statement in Python?',
        'back': 'for variable in sequence:\n    code block'
    },
    {
        'front': 'What is the built-in function commonly used to generate the sequence of values in a for loop?',
        'back': 'The built-in function "range" is commonly used to generate the sequence of values in a for loop.'
    },
    {
        'front': 'What are the three arguments of the range function, and what do they represent?',
        'back': 'The three arguments of the range function are "start", "stop", and "step". "start" is the first value in the sequence, "stop" is the limit (not included in the sequence), and "step" determines the difference between consecutive values in the sequence.'
    },
    {
        'front': 'If the first argument of range is omitted, what does it default to? What about the last argument (step size)?',
        'back': 'If the first argument of range is omitted, it defaults to 0. If the last argument (step size) is omitted, it defaults to 1.'
    },
    {
        'front': 'Does changing the value of the loop variable inside a for loop affect the number of iterations?',
        'back': 'No, changing the value of the loop variable inside a for loop does not affect the number of iterations. The arguments to the range function are evaluated just before the first iteration of the loop, and not reevaluated for subsequent iterations.'
    },
    {
        'front': 'What does the break statement do in a for loop?',
        'back': 'The break statement in a for loop causes the loop to terminate before it has been run on each element in the sequence over which it is iterating.'
    },
    {
        'front': 'How can you use the for loop and in operator to iterate over characters of a string?',
        'back': 'You can use the for loop and in operator to iterate over characters of a string by using a syntax like "for c in string:", where "c" is the character variable and "string" is the given string.'
    }
]

cards_deck10 = [    {"front": "What is a better problem statement for finding the square root of a nonnegative number?",     
                     "back": "A better problem statement is to find an approximation to the square root that lies within some constant, epsilon, of the actual answer."},    
                     {"front": "What is the issue with using exhaustive enumeration to find the square root of a number between 0 and 1?",     
                      "back": "Exhaustive enumeration only works if the set of values being searched includes the answer. When the number is between 0 and 1, its square root does not lie within the interval between 0 and the number itself."},    
                      {"front": "What is bisection search?",     "back": "Bisection search is an algorithm that divides the search space in half at each step, allowing for a more efficient search process compared to exhaustive enumeration."}]

cards_deck11 = [
    {
        "front": "Why does adding 0.1 ten times in a loop not produce exactly 1.0?",
        "back": "Adding 0.1 ten times doesn't produce exactly 1.0 because floating point numbers are approximations and can't represent some numbers, like 0.1, precisely. Rounding errors accumulate during the loop, resulting in a slightly different value."
    },
    {
        "front": "How many significant digits are available for floating point numbers in most Python implementations?",
        "back": "In most Python implementations, there are 53 bits of precision available for floating point numbers."
    },
    {
        "front": "What is the correct way to compare two floating point values for equality?",
        "back": "Instead of using ==, it's more appropriate to ask whether two floating point values are close enough to each other. For example, use `abs(x-y) < 0.0001` rather than `x == y`."
    }
]

cards_deck12 = [
    {
        "front": "What is Newton's method (also known as Newton-Raphson method)?",
        "back": "Newton's method is an approximation algorithm, usually attributed to Isaac Newton, used to find the real roots of many functions, including polynomials with one variable. The method involves improving an initial guess by calculating guess - p(guess) / p'(guess), where p is the polynomial and p' is its first derivative."
    },
    {
        "front": "What is a polynomial with one variable?",
        "back": "A polynomial with one variable is either 0 or the sum of a finite number of nonzero terms, each consisting of a constant (coefficient) multiplied by the variable raised to a nonnegative integer exponent. The exponent on a variable in a term is called the degree of that term. The degree of a polynomial is the largest degree of any single term."
    },
    {
        "front": "What is the root of a polynomial?",
        "back": "A root of a polynomial p is a solution to the equation p = 0, i.e., an r such that p(r) = 0. In other words, it's a value for the variable that makes the polynomial equal to zero."
    },
    {
        "front": "How does Newton's method use successive approximation?",
        "back": "Newton's method uses successive approximation by iteratively improving the current guess for the root of a polynomial. It calculates the next guess by subtracting the value of the polynomial divided by its first derivative from the current guess: guess - p(guess) / p'(guess)."
    },
    {
        "front": "What is the first derivative of a polynomial?",
        "back": "The first derivative of a polynomial expresses how the value of the polynomial changes with respect to changes in the variable. For any constant k and any coefficient c, the first derivative of the polynomial cx^2 + k is 2cx. For example, the first derivative of x^2 - k is 2x."
    }
]

cards_deck13 = [
    {
        "front": "What does it mean for a programming language to be Turing complete?",
        "back": "A programming language is Turing complete if it can solve any problem that can be solved through computation, using only a finite set of basic mechanisms or instructions. This means that a Turing complete language is theoretically powerful enough to solve any computationally solvable problem."
    },
    {
        "front": "Why is it important to generalize and reuse code?",
        "back": "Generalizing and reusing code helps in making programs more modular, maintainable, and less prone to errors. By reusing code, you avoid duplicating similar chunks of code, which reduces the chances of introducing errors and makes it easier to maintain and update the code."
    },
    {
        "front": "What is a function in Python and why is it important?",
        "back": "A function in Python is a block of reusable code that performs a specific task. Functions help in generalizing and reusing code, making programs more modular and maintainable. They allow you to perform complex computations and tasks without duplicating code, and can be easily reused in different parts of the program or even in other programs."
    },
    {
        "front": "What are the limitations of using a single sequence of instructions in a program?",
        "back": "A single sequence of instructions in a program lacks general utility, as it only works for specific variables and values. Reusing such code requires copying and pasting, possibly editing variable names, and inserting it where needed. This approach is not suitable for complex computations, as it leads to code duplication and increased chances of errors and maintenance difficulties."
    },
    {
        "front": "What is the problem with having multiple chunks of almost identical code in a program?",
        "back": "Having multiple chunks of almost identical code in a program increases the chances of introducing errors, makes the code harder to maintain, and may lead to inconsistencies when fixing errors or updating the code. It is better to generalize and reuse code using functions to avoid these issues."
    }
]

cards_deck14 = [    {        "front": "What is the benefit of being able to define and use custom functions?",        "back": "The ability for programmers to define and use their own functions, as if they were built-in, is a qualitative leap forward in convenience.",    },]

cards_deck15 = [
    {"front": "What is the format of a function definition in Python?", 
     "back": "def name_of_function(list_of_formal_parameters): body_of_function"},
    {"front": "What is the purpose of the 'def' keyword in Python function definitions?", 
     "back": "It tells Python that a function is about to be defined."},
    {"front": "What are the formal parameters of a function?", 
     "back": "The sequence of names within the parentheses following the function name."},
    {"front": "What happens when a function is called in Python?", 
     "back": "1. The expressions that make up the actual parameters are evaluated, and the formal parameters of the function are bound to the resulting values. \n2. The point of execution (the next instruction to be executed) moves from the point of invocation to the first statement in the body of the function. \n3. The code in the body of the function is executed until either a return statement is encountered, in which case the value of the expression following the return becomes the value of the function invocation, or there are no more statements to execute, in which case the function returns the value None. (If no expression follows the return, the value of the invocation is None.) \n4. The value of the invocation is the returned value. \n5. The point of execution is transferred back to the code immediately following the invocation."},
    {"front": "What is the purpose of the 'return' statement in Python function definitions?", 
     "back": "It can be used only within the body of a function and it terminates an invocation of the function. The value of the expression following the return becomes the value of the function invocation."},
    {"front": "What is lambda abstraction in Python?", 
     "back": "Parameters provide something called lambda abstraction, allowing programmers to write code that manipulates not specific objects, but instead whatever objects the caller of the function chooses to use as actual parameters."},
    {"front": "Finger exercise: Write a function isIn that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise.", 
     "back": "def isIn(str1, str2):\n    return str1 in str2 or str2 in str1"},
]

cards_deck16 = [
    {"front": "What is the most common method for binding formal parameters to actual parameters in Python?", 
     "back": "Positional - the first formal parameter is bound to the first actual parameter, the second formal to the second actual, etc."},
    
    {"front": "What is the second way that formal parameters get bound to actual parameters in Python?", 
     "back": "Keyword arguments - formals are bound to actuals using the name of the formal parameter."},
    
    {"front": "What is the function printName used for?", 
     "back": "It assumes that firstName and lastName are strings and that reverse is a Boolean. If reverse == True, it prints lastName, firstName, otherwise it prints firstName lastName."},
    
    {"front": "What are the equivalent invocations of printName?", 
     "back": "- printName('Olga', 'Puchmajerova', False)\n- printName('Olga', 'Puchmajerova', reverse = False)\n- printName('Olga', lastName = 'Puchmajerova', reverse = False)\n- printName(lastName = 'Puchmajerova', firstName = ' Olga', reverse = False)"},
    
    {"front": "Can you follow a keyword argument with a non-keyword argument in Python?", 
     "back": "No, it is not legal to follow a keyword argument with a non-keyword argument."},
    
    {"front": "What are default parameter values and how can they be used?", 
     "back": "Default values allow programmers to call a function with fewer than the specified number of arguments. They are commonly used in conjunction with keyword arguments. For example, def printName(firstName, lastName, reverse = False): ..."},
    
    {"front": "What is the advantage of providing default parameter values in Python?", 
     "back": "It allows for calling a function with fewer than the specified number of arguments and provides some documentation for the perhaps mysterious argument True."},
]


""" decks_and_cards = [
    (deck1, cards_deck1),
    (deck2, cards_deck2),
    (deck3, cards_deck3),
    (deck4, cards_deck4),
    (deck5, cards_deck5),
    (deck6, cards_deck6),
    (deck7, cards_deck7),
    (deck8, cards_deck8),
    (deck9, cards_deck9),
    (deck10, cards_deck10),
    (deck11, cards_deck11),
] """


decks_and_cards = [(globals()[f'deck{i}'], globals()[f'cards_deck{i}']) for i in range(1, 17)]
#Note: range should be 1 plus the max

for deck, cards in decks_and_cards:
    for card in cards:
        add_card_to_deck(deck, card['front'], card['back'])
