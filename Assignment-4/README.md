# Dynamic Web Content 

You are provided with **Dynamicweb.zip** that contains a simple HTTP web server that we have designed for you. It has a simple HTTP registration page (localhost:8080/form) that asks you to enter the first name and email ID to register.

Your task is to write a python script that automates the process of registering. 

The Dynamicweb.zip contains contacts, txt that has the different names and email IDs
that you need to register automatically through your scnpt. 

In the the template folder, you will find an html form whose actions you need to automate through your script. The script should look for error messages if the entry that you are trying to register is already in the system or not. If no error message, your entry gets stored in the rver. The script should save all the responses from the server and count the number of successful and unsuccessful attempts to register. 

1. Please provide a graphical representation of the successful and unsuccessful attempts of registering in a single graph, 
2. Every time you get a response from the server, within it you will also receive the number of elements in the list on the server). Save the number of list elements you receive after every response (in a le local to the directory you run your code from). and plot the changes 

## Requirements 

  1. You will need to install the 1pthw.web- library in order to run the server.
  2. In order to run the server it is necessary to min the python bin/app.py command (from the directory that contains the bin directory) 

You may use requests library if required along with matplotlib. Please keep in mind that every time you restart the server, the server starts fresh
