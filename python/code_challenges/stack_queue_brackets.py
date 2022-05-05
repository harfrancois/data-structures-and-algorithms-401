from data_structures.stack import Stack

# validate function to check if the open string
# has a closing to pare with it
def validate(string_1, string_2):
    if string_1 == '(' and string_2 == ')':
        return True
    elif string_1 == '{' and string_2 == '}':
        return True
    elif string_1 == '[' and string_2 == ']':
        return True
    else:
        return False

def multi_bracket_validation(input_string):
    stack = Stack()
    validation = True
    string_index = 0
    while string_index < len(input_string) and validation:
        bracket = input_string[string_index]
        if bracket in '({[':
            stack.push(bracket)
        else:
            if stack.is_empty():
                validation = False
            else:
                top = stack.pop()
                if not validate(top, bracket):
                    validation = False
        string_index += 1

    if stack.is_empty() and validation:
        return True
    else:
        return False

