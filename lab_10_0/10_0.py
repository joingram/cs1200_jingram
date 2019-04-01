"""
CSCI 1200
Lab Exercise 10.0

FILES AND EXCEPTIONS

In this lab you will learn how to read and write text files and how
to handle exceptions. Do all work in Geany IDE and follow instructions 
provided in this code file.

Learning Outcomes
=================
In this lab you will learn how to:
- Read a file
- Write a file
- Write a try-catch block
- Handle FileNotFoundError

Evaluation
==========
20 pts. - submitted filename 10_0.py
20 pts. - 10_0.py executes without error
60 pts. - Program meets requiments

Submission
==========
As before, submit your work on D2L or using git. Submit all files.
If you are using D2L please zip your submission files.
Earn 5 pts. extra credit by submitting using git by due date.

"""

#=======================================================================
# ASSIGNMENT INSTRUCTIONS
#-----------------------------------------------------------------------
#
# Using your computer's file system allows you to make more interesting 
# programs by creating programs that can do some work, stop, and resume 
# processing from the same place later. In today's lab we will practice
# reading from and writing to files. We will build a simple chatbot
# that tells funny jokes, and record the total number of times the bot 
# has told jokes. 
#
#-----------------------------------------------------------------------
# PART 1
#-----------------------------------------------------------------------
#
# First let's perform all imports and initialize all variables
#
# 1. import BotHelper class from module called `bot_functions`. 
#    This class contains some predefined helper funtions you will use 
#    during this lab. You do no need to instantiate this class.
# 
# 2. Type a command to open a file `funny.txt` for reading.
#
# 3. funny.txt contains some plain text jokes. In order to use it, 
#    we need to parse the text. After you have opened the file for
#    reading, pass the file object to parse_jokes function which is 
#    already defined for you in BotHelper, as follows:  
#    jokes = BotHelper.parse_jokes(file_obj)
#
# 4. Type a command to try open file `counter.txt` for reading. Assign 
#    contents to an integer variable called counter. 
#    Note: this file may not exist yet. In that case initialize counter
#    variable with value 0. If file does exist, make sure to convert 
#    file contents to integers using int() function. 
#
#-----------------------------------------------------------------------







#-----------------------------------------------------------------------
# PART 2
#-----------------------------------------------------------------------
# Next let's write an simple chatbot. This bot is not very smart but 
# what is lacks in intelligence it will make up by being funny.
#
# 4. Choose a name for your bot, then print a greeting to the user.
#    Something like `Hi My name is ..... I'm a funny chatbot.". 
#    Ask the user what their name is. You may respond in some way
#    if you want to, for example: 'Nice to meet you (name)'.
#
# 5. Declare a while loop that will run indefinitely (until user quits).
#    Steps 6., 7., and 8. should be defined inside this while loop:
#
#    6. Ask if the user wants to hear a joke. Instead of writing 
#    a hardcoded string prompt, use BotHelper as follows:   
#    user_response = input(BotHelper.want_a_joke())
#    This function takes one optional argument: user's name
#
#    7. If the user responds with "no", "not now" or "nope", print
#    something to the user, like "OK bye" or "maybe next time", then 
#    break the while loop. When checking the response, ignore letter 
#    case and white spaces, i.e. "NO  " should be treated same as "no".
#
#    8. Else increment counter variable by 1. Then run following
#    command, where `jokes` is the text you read from file in part 1:
#    BotHelper.tell_joke(jokes)
#   
#
# 9. Outside the while loop, write the value of counter variable
#    to a file called `counter.txt`. You must overwrite any previous 
#    contents of the file.  This will be the end of the program.
#
# 10. Every time you run the program and the bot tells jokes the
#     counter value will increment. You should run the program a few 
#     times and observe the value in counter.txt increment after every
#     program execution. 
#-----------------------------------------------------------------------







#=======================================================================
# That's it for today!
# End of Lab Exercise 10.0
#=======================================================================
