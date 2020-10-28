# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import chopchop
import countcharacters
import duplicate
import specialsub
import unique


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Type your code here

'''
Practice ProblemQuiz 5
Working with Strings:
    Note:1.When  a  function  returns  true,  it  is  referring  to  a  Boolean
        True  value  not  a  string true. Same for false.
    2.Consideration of punctuation and space is problem specific.
        For punctuation consider comma ( , ), semicolon ( ; ) 0 , colon ( : ), dot ( . ).
        Avoid punctuation means do not consider   punctuation. E.g. by avoiding punctuation
        “let it be, let it be.”, will become ‘let it be let it be’.
    3.[Ignore  cases]  means  the  function  is  case  insensitive. i.e. ‘A’  and ‘a’
        is considered to be same.

1: Write a function named is_specialsub that takes a string (S) and a string (A).
        Then the program checks if the string A appears in the string S or not.
        If the string A is in string  S, the  function  returns  true  else  returns  false.
        If  there  is  any  space  or punctuation in   between  the  characters  either in  S  or  A
        discard them  before matching. [Ignore cases] Function definition: def is_specialsub(S,A):
    Sample Input: print(is_specialsub(‘let it be, let it be, let it be’,’ b     e’))
    Output:True
    Explanation:The space between b and e is discarded and only the order of the characters in the string is important.
    
    Sample Input: print(is_specialsub(‘The cat, sat on the hat’,’  at  sa’)) 
    Output:True
    Explanation:The space and comma between t and s in string S is discarded before matching with A.
'''

print(specialsub.is_specialsub('onomatopoeia', 'mat'))

print(countcharacters.count_chars('onomatopoeia', ['p', 'i', 't']))

print(unique.unique_char('onomatopoeia'))

print(duplicate.contains_duplicate('onomatopoeia'))
print(duplicate.contains_duplicate('what'))

print(chopchop.chop_string('onomatopoeia', 'o'))
