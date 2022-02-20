# CalgaryHacks-2022-Group-44
## Project Members
 * Ryan Huynh
 * Shaakira Gadiwan
 * Caroline Basta
 * Daniel Hanick
 * Haseen Kahn

## Libraries used for API
 * Django
 * Django Rest Framework
 * Pillow

## How to run the local server for the API (For Windows)
Ensure Python is installed.
1. Clone the repository
2. Open a command prompt and navigate to where you cloned the repository.
3. Enter the command "env\scripts\activate.bat" to activate the virtual environment
4. Navigate to myproject by entering "cd myproject"
5. Run the server by entering "python manage.py runserver". You will know the server running if there is a prompt where it suggest that pressing CTRL-BREAK will end the server.

## API Documentation
It is recommended to use Postman if you want to see the API in action (https://www.postman.com/)

The general format for the URL to access the API is:
"http://127.0.0.1:8000/api/v1/<commands>"

What goes into <commands> determines the function. There are 5 possible branches for this API, which are:
  * account
  * driver
  * posting
  * report
  * passenger
  
### account
  account has the following properties:
  * accountId - uniquely identifies the account object
  * school - the string identifying the university the account holder is attending
  * idSchool - the account holder's school id
  * phoneNum - the account holder's phone number
  * imagePath - the path on the server to the image depicting the account holder
  
  
  http://127.0.0.1:8000/api/v1/account
  * As a get request, it returns all the account object in the database as JSON objects.
  * As a post request, it takes in an input in the form of a JSON object and create a new account object
  
  http://127.0.0.1:8000/api/v1/account/**name**
  * As a get request, it returns all account objects where the account users are attending **name**.
  * As a delete request, it deletes all account objects where the account users are attending **name**.
  
  http://127.0.0.1:8000/api/v1/account/**name**/$**id**
  * As a get request, it returns the account object attending **name** with an school id of **id**
  * As a put request, it takes in a JSON object input and overwrites the account object attending **name** with an school id of **id**
  * As a delete request, it removes the account object attending **name** with an school id of **id**
  
  
