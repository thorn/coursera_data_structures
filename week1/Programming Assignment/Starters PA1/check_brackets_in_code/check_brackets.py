# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read().strip()
    result = "Success"

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            bracket = Bracket(next, i)
            opening_brackets_stack.append(bracket)

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                result = str(i + 1)
                break;

            last_bracket = opening_brackets_stack.pop()
            if not last_bracket.Match(next):
                result = str(i + 1)
                break

    if len(opening_brackets_stack) > 0 and result == "Success":
        result = opening_brackets_stack.pop().position + 1
    # Printing answer, write your code here
    print(result)
