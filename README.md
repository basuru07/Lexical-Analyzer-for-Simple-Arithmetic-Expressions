# Lexer Implementation for Simple Language

This repository contains an implementation of a simple lexer (also known as a lexical analyzer) that tokenizes input strings into various components such as identifiers, numbers, operators, parentheses, and semicolons. The lexer is designed to handle basic mathematical expressions and assignments, and can serve as a foundational tool for building simple interpreters or compilers.

## Purpose
The lexer’s job is to break down a string of code into smaller, manageable parts (tokens), which are then used by parsers or interpreters for further processing. This lexer is capable of handling:
- **Identifiers**: Variable names or function names, typically composed of letters or alphanumeric characters.
- **Numbers**: Integers and floating-point numbers.
- **Operators**: Arithmetic operators such as `+`, `-`, `*`, and `/`.
- **Parentheses**: For grouping expressions or controlling precedence.
- **Semicolons**: To terminate statements in the language.

## Features
- **Tokenization of basic expressions**: Supports arithmetic expressions and simple assignments.
- **Floating-point number support**: Handles both integers and floating-point numbers.
- **Error handling**: Ensures that invalid characters or incorrectly formatted numbers are detected and raises errors.
- **Extendable**: Easy to extend for more complex tokenization needs, such as handling strings, booleans, or keywords.

## Key Components
- **Lexer Class**: The main class that performs the tokenization.
  - **`advance()`**: Moves to the next character in the input string.
  - **`tokenize()`**: Main function to break down the input string into tokens.
  - **`collect_identifier()`**: Collects characters to form an identifier.
  - **`collect_number()`**: Collects characters to form a number, including floating-point numbers.

### Example Usage:
This example demonstrates how to use the `Lexer` class to tokenize a string input:

```python
if __name__ == "__main__":
    input_code = "x = 10 + 20 * (30 / y);"
    lexer = Lexer(input_code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)
```
### Output:
```python
('IDENTIFIER', 'x')
('ASSIGNMENT', '=')
('NUMBER', '10')
('OPERATOR', '+')
('NUMBER', '20')
('OPERATOR', '*')
('PARENTHESIS', '(')
('NUMBER', '30')
('OPERATOR', '/')
('IDENTIFIER', 'y')
('PARENTHESIS', ')')
('SEMICOLON', ';')
```
