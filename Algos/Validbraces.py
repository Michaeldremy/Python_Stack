from stacks import *

def ValidBraces(string):
    # set of opening and closing braces for easy checking
    openings = [ "(", "[", "{" ]
    closings = [ ")", "]", "}" ]

    # dictionary of opening braces and their corresponding closing braces
    valids = {
        "(": ")",
        "{": "}",
        "[": "]" }

    # creating a stack from the previous day's algo
    brace_stack = Stack()

    # Iterate through the string
    for i in string:

        # If a character is an opening brace
        if i in openings:
            # Push the opening brace into the stack
            brace_stack.Push(i)

        # Else if the character is a closing brace
        elif i in closings:
            # Check to see that there is an opening brace in the stack, and then
            # Check to see if the closing brace matches the most recent opening brace in the stack
            if brace_stack.Peek() != None and i == valids[brace_stack.Peek()]:
                # If it matches, remove the opening brace from the top of the stack
                brace_stack.Pop()
            else:
                # If the braces DON'T match, the string is invalid
                return False

    # Check to see that there are no leftover opening braces left in the stack
    if brace_stack.Peek() != None:
        return False
    
    else: 
        return True

print(ValidBraces(")))}"))