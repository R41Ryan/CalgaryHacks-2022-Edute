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
  
  http://127.0.0.1:8000/api/v1/account/**name** (Example: "http://127.0.0.1:8000/api/v1/account/University of Calgary")
  * As a get request, it returns all account objects where the account users are attending **name**.
  * As a delete request, it deletes all account objects where the account users are attending **name**.
  
  http://127.0.0.1:8000/api/v1/account/**name**/$**id** (Example: "http://127.0.0.1:8000/api/v1/account/University of Calgary/$1234")
  * As a get request, it returns the account object attending **name** with an school id of **id**
  * As a put request, it takes in a JSON object input and overwrites the account object attending **name** with an school id of **id**
  * As a delete request, it removes the account object attending **name** with an school id of **id**
 
### driver
 account has the following properties:
 * accountId - a foreign key to the account that it identifies as a driver
 * licenceNum - the driver's driver's licence number
 * driverHistoryFilePath - the path on the server to the document describing the driver's driving history.
 
 http://127.0.0.1:8000/api/v1/driver
 * As a get request, returns all driver objects
 * As a post request, takes in a JSON object input to create a new driver object.
 
 http://127.0.0.1:8000/api/v1/driver/**id** (Example: "http://127.0.0.1:8000/api/v1/driver/103")
 * As a get request, it returns the driver object with an account id of **id**
 * As a put request, it takes in a JSON object input and overwrites the account object an account id of **id**
 * As a delete request, it removes the posting object an with a account id of **id**
 
### posting
 account has the following properties:
 * postingId - A number that uniquely identifies the posting
 * startAddress - the starting address of the driver's ride
 * destination - the address of where the driver's going to
 * startTime - The time the driver is expecting to leave
 * endTime - The time the driver is expected to arrive at the destination
 * driverId - A foreign key to the driver object who is driving for this posting
 * maxPassenger - The maximum number of passengers the driver can accomodate
 * numOfPassenger - The current number of passengers that have booked a seat for this posting
 * status - The status of the posting ("Available, Full, Cancelled, etc.")
 
 http://127.0.0.1:8000/api/v1/posting
 * As a get request, returns all posting objects
 * As a post request, takes in a JSON object input to create a new posting object.
 
 http://127.0.0.1:8000/api/v1/posting/**id** (Example: "http://127.0.0.1:8000/api/v1/posting/103")
 * As a get request, it returns the posting object with an postingId of **id**
 * As a put request, it takes in a JSON object input and overwrites the posting object an postingId of **id**
 * As a delete request, it removes the posting object an with a postingId of **id**
 
### report
 account has the following properties:
 * reportNum - A number that uniquely identifies the report
 * reporterId - the foreign key to the account ID that made the report
 * reportedId - the foreign key to the account ID that the report is made against.
 
 http://127.0.0.1:8000/api/v1/report
 * As a get request, returns all report objects
 * As a post request, takes in a JSON object input to create a new report object.
 
 http://127.0.0.1:8000/api/v1/report/**id** (Example: "http://127.0.0.1:8000/api/v1/report/103")
 * As a get request, it returns the report object with a reportNum of **id**
 * As a put request, it takes in a JSON object input and overwrites the report object a reportNum of **id**
 * As a delete request, it removes the report object an with a reportNum of **id**

### passenger
  passenger refers to PostingPassenger objects and has the following properties:
  * postingId - foreign key referring to the posting
  * idPassenger - foreign key to the account who is a passenger of postingId
  
  http://127.0.0.1:8000/api/v1/passenger
  * As a get request, it returns all the PostingPassegner objects in the database as JSON objects.
  * As a post request, it takes in an input in the form of a JSON object and create a new PostingPassenger object
  
  http://127.0.0.1:8000/api/v1/passenger/**num** (Example: "http://127.0.0.1:8000/api/v1/passenger/12")
  * As a get request, it returns all PostingPassenger objects where the postingId is **name**.
  * As a delete request, it deletes all PostingPassenger objects where the postingId is **name**.
  
  http://127.0.0.1:8000/api/v1/passenger/**num**$**id** (Example: "http://127.0.0.1:8000/api/v1/account/12$1234")
  * As a get request, it returns the PostingPassenger object with postingId **name** and idPassenger **id**
  * As a put request, it takes in a JSON object input and overwrites the PostingPassenger object with postingId **name** and idPassenger **id**
  * As a delete request, it removes the PostingPassenger object with postingId **name** and idPassenger **id**
