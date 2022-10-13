# Describe the difference between asynchronous programming with synchronous programming.
Asynchronus programming doesn’t block execution of another operation while one or more operations are in progress, whileas synchronus programming operations are performed oen at a time.

# When Implementing Javascript and AJAX, there is an application in the paradigms of Event-Driven Programming. Describe the reasoning for those paradigms and state some examples of its application.
The implementation is used so that the user can have quick and accurate responses based on their actions (events happening). This will lead to better user experience and can help when problems regarding close coordination of microservices, error handling, and retries arise. AJAX also allows 

# Describe the implementation of asynchronous programming in AJAX.
It uses functions which are driven by events happening, and so by such, AJAX allows web pages and applications to dynamically alter database contents without the need to reload the entire page.

# Explain how you would implement the checklist above.
First, I created a view which returns data in JSON form and continued by creating the path. In doing the AJAX GET method to get the list of task, I used the assistant's previous week tutorial solution as a guidance on how to implement it. I haven't succeed in doing the AJAX POST method, and is currently still trying to work on that.
