# UniversalSmsSender

This application is made to use all the online sms services that supply only one API to send a single SMS to a single number. With this application you can import a list of numbers from and excel file and send a text message to all the numbers.

The idea is to create the application with different languages to ensure maximum compatibility with all types of system.

# PySender

Implementation with Python3

USAGE: 
Download or clone the PySender folder, then make a copy of the config.example.py file and rename to config.py.
Then update the file with your settings.
Copy the excel file with the list of numbers (in the first column in the first sheet) inside the PySender folder.
Start the application:
  - Windows: run the startUI.bat 
  - Linux: coming soon...
Input the name of the file excel you want to extract the numbers from and click extract(wait for the result)
Input the message you want to send and click send
For every number the system will try to send the message at maximum three times, then it will move on to the next number
