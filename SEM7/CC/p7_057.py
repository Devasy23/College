import lexer
import parser

lexer = lexer.lexer
parser = parser.parser

input_string = """
if (x == y) {
    // code block
} else {
    // code block
}

while (x < 10) {
    // code block
}
"""

lexer.input(input_string)
result = parser.parse(input_string)

if result is not None:
    print("Parsing successful!")
else:
    print("Parsing failed.")
