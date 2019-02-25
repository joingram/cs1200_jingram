"""
CSCI 1200
Lab Exercise 6.1

DICTIONARIES (CONT.)

In this lab we will continue practicing how do use dictionaries.
Do all work in Geany IDE and follow instructions provided 
in this code file.

Learning Outcomes
=================
In this lab you will learn how to:
- declare a dictionary
- add different types of values to a dictionary
- accessing dictionary values using keys and loops
- accessing dictionary values in a nested dictionary
- testing if keys exists in a dictionary
- removing key value pairs


Evaluation
==========
20 pts. - submitted filename 6_1.py
20 pts. - 6_1.py executes without error
20 pts. - Part 1 meets requirements
20 pts. - Part 2 meets requirements
20 pts. - Part 3 meets requirements

Submission
==========
As before, submit your work on D2L or using git.
Earn 5 pts. extra credit by submitting using git by due date.

"""


#=======================================================================
# PART 1
#-----------------------------------------------------------------------
# In this part you will practice declaring a dictionary and
# adding different values to it
#-----------------------------------------------------------------------

# 1. Create a dictionary called `my_university`. This 
#    dictionary should initially be empty.




# 2. Add new key-value pair to my_university dictionary. 
#    The key is `name` and the value is `Augusta University`





# 3. Add new key-value pair to my_university dictionary.
#    The key is `founding_year` and the value is 1828 (integer)





# 4. Add new key-value pair to my_university dictionary.
#    The key is `president` and the value is `Brooks Keel`





# 5. Add new key-value pair to my_university dictionary.
#    The key is `campuses` and the value is a list with following
#    values: summerville, riverfront, health sciences, forest hills





# 6. Add new key-value pair to my_university dictionary.
#    The key is `course_codes` and the value is a dictionary with 
#    following key-value pairs:
#    "BIOL" : "Biology"
#    "CSCI" : "Computer Science"
#    "MATH" : "Mathematics"
#    "PHYS" : "Physics"
#    "ENGL" : "English"
#    "POLS" : "Political Science"
#    "HIST" : "History"
#    "HUMN" : "Humanities"
#    You can add more key-value pairs if you want.







#=======================================================================
# PART 2
#-----------------------------------------------------------------------
# In this part you will practice how to access values from the 
# `my_university` dictionary you created in part 1.
#
# When you are asked to access values from my_university, make sure
# you are using the proper syntax for accessing values, example:  
# print(some_dict[key]) or  print(some_dict.values())  (CORRECT) 
#
# Using string literals such as print("some text") is incorrect.
#-----------------------------------------------------------------------


# 1. Print following text using values from `my_university`.
#
#    "I'm a student at {name}. The university was founded
#     in {founding_year}. The current president is {president}."
#
#    Replace the words in braces { } with appropriate values from
#    the dictionary you created in part 1.






# 2. Print the following text using values from `my_university`.
#
#    "The university has 4 campuses:"
#    "- {campus}"  
#
#    Print the names of ALL campuses.
#    If you want, you can try to print them in alphabetical order.






# 3. Print the following text using values from `my_university`.
#
#    "I have taken courses in:"
#    "- {value of course_code}
#
#    Print ONLY names of subjects you have taken or are currently
#    taking, for example "Computer Science" and/or "History".







#=======================================================================
# PART 3
#-----------------------------------------------------------------------
# In this part you will practice removing and modifying dictionary 
# values.
#-----------------------------------------------------------------------


#  1. Remove key-value pair `course_codes` from `my_university`.
#     Use del keyword.




#  2. Remove key-value pair `president` from `my_university`.
#     Use a different keyword other than del. 




#  3. Remove key-value pair `campuses` from `my_university`.
#     Choose any appropriate keyword. 




#  4. Test that `my_university` no longer contains the key `campuses`.
#     Hint: write a conditional statement and print the truth value





#  5. At this point `my_university` should only contain 2 keys:
#     `name` and `founding_year`.  Let's practice changing these 
#     values to some new values. 
#     Change `name` to 'Harvard University'
#     Change `founding_year` to 1636





#  6. Print `my_university` to verify that the values have changed.





#  7. Lastly remove all remaining key-value pairs from `my_university`.
#     Hint: There is a special command that removes all key-value
#     pairs from a python dictionary, it starts with c.


 


#=======================================================================
# That's it for today!
# End of Lab Exercise 6.1
#=======================================================================
