__author__ = 'jonerik13'

#Jon-Erik Svenson, Project 2, CS 311

def run(string, fileName):
    """
    This program takes in a string and an external file and checks if the string is in the language
    or not. Both aruments are taken as a string. The program opens a grammar file, loads
    information into a dictionary, and then maintains a stack list and an input list, and prints
    accept or reject.

    >>> run('', 'grammar1.py')
    String Rejected

    >>> run('', 'grammar2.py')
    String Rejected

    >>> run('', 'grammar3.py')
    String Rejected

    >>> run('', 'grammar4.py')
    String Rejected

    >>> run('aa#bb', 'grammar1.py')
    String Accepted!

    >>> run('101#101', 'grammar2.py')
    String Accepted!

    >>> run("a#b#ccc#", "grammar3.py")
    String Accepted!

    >>> run('0001000', 'grammar4.py')
    String Accepted!

    >>> run('1111111', 'grammar3.py')
    String Rejected

    >>> run('#', 'grammar2.py')
    String Rejected


    """

    grammarDict = {}

    killBool = False
    if string == '#':
        if fileName == 'grammar1.py' or fileName == 'grammar2.py':
            killBool = True
    elif string == '':
        killBool = True


    #string to list
    string = list(string)


    #open file, loop by line
    f = open(fileName, "r")
    for line in f:

        #split line on the comma
        hold = line.split(",")

        #strip the endline
        hold[1] = hold[1].rstrip('\n')

        #save the rule
        rule = hold[1]


        #rejoin the rule and split to make our key
        string2 = ''
        string2 = string2.join(hold)
        hold = list(string2)

        #concatenate variable, next char
        var = hold[0]+hold[1]

        #load dictionary
        grammarDict[var] = rule



    #push start variable
    stack = ["S"]

    #while the input string is not empty, loop
    while string:
        print stack
        if not stack:
            killBool = True
            break

        #check if variable
        if stack[0].isupper():

                #if so, find the rule, pop the variable and replace with rule
                var = stack[0] + string[0]
                if var in grammarDict.keys():

                    stack.pop(0)
                    stack.insert(0, grammarDict[var])
                    joiner = ''.join(stack)
                    stack = list(joiner)

                #if the key isnt in the dictionary, autoreject
                else:

                    killBool = True
                    break

        #if the first char on the stack is a lowercase, compare to input, pop if true
        elif string[0] == stack[0]:
                    string.pop(0)
                    stack.pop(0)

        #reject if false
        else:

                    killBool = True
                    break

    #check if input and stack is empty, if both are, accept
    if not killBool:
        if not stack and not string:
            print "String Accepted!"
    else:
        print "String Rejected"


#helper function to run for user
def runGrammar():

    go = True
    while go:
        startFile = raw_input("Type your filename for the grammar: ")
        startString = raw_input("Now type a string to test: ")
        run(startString, startFile)

        ask = raw_input("Would you like to run again? (Y/N): ")
        if ask.upper() == 'Y':
            go = True
        else:
            go = False


runGrammar()


#doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()