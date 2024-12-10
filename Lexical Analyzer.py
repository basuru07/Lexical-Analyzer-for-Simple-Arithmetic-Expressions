class Lexer:
    """
    A simple lexer to tokenize input strings into identifiers, numbers,
    operators, parentheses, and semicolons.
    """

    def __init__(self, input_string):
        self.input_string = input_string
        self.tokens = []
        self.current_char = None
        self.position = -1
        self.advance()

    def advance(self):
        """Move to the next character in the input string."""
        self.position += 1
        if self.position < len(self.input_string):
            self.current_char = self.input_string[self.position]
        else:
            self.current_char = None

    def tokenize(self):
        """
        Break the input string into a list of tokens.
        Returns:
            list: A list of (type, value) tuples representing tokens.
        """
        while self.current_char is not None:
            if self.current_char.isspace():
                self.advance()
            elif self.current_char.isalpha():
                self.tokens.append(('IDENTIFIER', self.collect_identifier()))
            elif self.current_char.isdigit():
                self.tokens.append(('NUMBER', self.collect_number()))
            elif self.current_char == '=':
                self.tokens.append(('ASSIGNMENT', self.current_char))
                self.advance()
            elif self.current_char in "+-*/":
                self.tokens.append(('OPERATOR', self.current_char))
                self.advance()
            elif self.current_char in "()":
                self.tokens.append(('PARENTHESIS', self.current_char))
                self.advance()
            elif self.current_char == ';':
                self.tokens.append(('SEMICOLON', self.current_char))
                self.advance()
            else:
                raise ValueError(f"Unknown character: {self.current_char}")
        return self.tokens

    def collect_identifier(self):
        """
        Collect an identifier token.
        Returns:
            str: The identifier string.
        """
        identifier = ""
        while self.current_char is not None and self.current_char.isalnum():
            identifier += self.current_char
            self.advance()
        return identifier

    def collect_number(self):
        """
        Collect a number token, including floating-point numbers.
        Returns:
            str: The number string.
        """
        number = ""
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            if self.current_char == '.' and '.' in number:
                raise ValueError(f"Invalid number format: {number}.")
            number += self.current_char
            self.advance()
        return number


# Example Usage
if __name__ == "__main__":
    input_code = "(a + b) * c;"
    lexer = Lexer(input_code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)
