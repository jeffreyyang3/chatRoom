# Chat room 

This is my submission for MobLab's technical assessment.

## Installation

I used Docker to start a Redis server, with the command

**docker run -p 6379:6379 -d redis:2.8**

I also tried to avoid installation and dependency issues by using virtualenv and a requirements.txt.

From the chatRoom directory, virtualenv can be run with 

**source env/bin/activate**

It may also be necessary to run 

**pip3 install -r requirements.txt**

After that, the app should be ready to run with
**python3 manage.py runserver**

accessible through a web browser at 
**http://localhost:8000/**

Open a tab/window for each client at that URL.
There may still be installation issues, as I could only test this 
on one other computer.  If there are any that
you can't figure out, I can try my best to fix it, or give a live demo.
I can be contacted through email, or more quickly at 626-818-2618.


## Overview
This is a Django application with Vue.js handling front end
interactivity. It also uses a Django library called Channels to
make WebSocket handling easier. 

With this application, one can create or join a chatroom.
In the chatroom, one person can be the instructor, and the
rest of the members are students.  The students have the choice of being anonymous to each other, or having their names be visible to each other.  However, the instructor can always see all students' names, even if they are anonymous to each other.   

Each participant in the chatroom opens a WebSocket, used to exchange JSON encoded data with the server.
The server handles the appropriate message forwarding and the functionality for anonymity.
Data is parsed and displayed on the front end with Vue.js.

## Issues/Potential Issues

 - Since the assignment did not ask me to handle situations 
with more than one instructor, I didn't write in functionality for that. When there is more than one instructor,
instructors won't receive messages correctly.

 - Due to the way the instructor's message channel is broadcasted to 
the chat room, there's a very small possibility, especially with slow connections) that the instructor might miss a message. 

 - If the instructor leaves and joins again, or a different instructor enters after, the chat may not work correctly.
 - As far as I can tell, there isn't an issue now , but a bad room name input could cause 404 or WebSocket connection failure.

 - If JS is disabled, or Vue doesn't load, nothing will work.

## Thoughts

This was my first time having to write actual back end functionality instead of  letting a framework abstract everything away.  Thus, I found it extra challenging to work with Django on an interactive web application of this nature. 

 Most of the functionality for this application was done with client-side JS because I didn't know how to get Django to do what I wanted. But I ended up liking the front end more than I thought I would. It was a pleasure to work with Vue, and I also enjoyed styling the chatroom.

If I were to do this project or something similar again, I would try to have the back end handle more of the logic. My reliance on client-side JS for functionality necessitated unintuitive workarounds like having the instructor constantly send invisible messages to the group. Also, in many other real world use cases, that reliance could be unsafe.

Overall, I really enjoyed working on this project. It was an awesome learning experience. 







