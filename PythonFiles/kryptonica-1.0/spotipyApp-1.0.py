#!/usr/bin/python3 
# Importing the 'cgi' module 
import cgi
import cgitb 

from scripts import Cas

# Using the inbuilt methods 

cgitb.enable()
html_ = Cas()

opening = html_.createOpening('Kryptonica')
print(opening)

form = cgi.FieldStorage() 
if form.getvalue("name"): 
	name = form.getvalue("name") 
	print("<h1>Hello " +name+"! Thanks for using my script!</h1><br />") 
if form.getvalue("happy"): 
	print("<p> Yayy! I'm happy too! </p>") 
if form.getvalue("sad"): 
	print("<p> Oh no! Why are you sad? </p>") 

# Using HTML input and forms method 
print("<form method='post' action='spotipyApp-1.0.py'><p>Name: <input type='text' name='name' /></p>") 
print("<input type='checkbox' name='happy' /> Happy") 
print("<input type='checkbox' name='sad' /> Sad") 
print("<input type='submit' value='Submit' />") 
print("</form") 
print("</body></html>") 
