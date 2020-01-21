#LRUCache
Coding assessment for an interview

Assumptions:

1. The assignment asked for the signature of capability to remove a key, value pair from the cache to be 
'del' since that is a key word in python. I assumed that changing the signature to 'delete' is OK.

2. I assumed that the key can be of any type and any value. Even negative and None. 

3. There was no mention of what needs to be returned to the user in case of Error specifically for get().
    Since the key can be anything (assumption 2) I assumed returning None would be acceptable.
    This can be switched to throwing an exception or any other value if needed.

4. I realize this is a lot of code for something that can be accomplished via collections and python3 functools packages.
    but since this is a take home assessment I assumed we are not allowed to use any of the convenience offered by those packages.


How to run the code:
1. If you dont have python3 installed install by following instructions here: https://www.python.org/downloads/
2. Clone the git repo.
3. The main.py file allows for quick initialization and calling of appropriate functions. Modify that file to what you desire to test.
4. In your terminal navigate to the git repo and run comand
    python main.py