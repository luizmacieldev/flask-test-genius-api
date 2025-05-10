# flask-test-genius-api

Steps:

   1 - After cloning the project, navigate to the "flask-test-genius-api" folder and install the dependencies listed in the requirements.txt file using the command:
        pip install -r requirements.txt


    2 -2 - Add your AWS credentials by running the command: aws configure
    and providing the following parameters:
            "AWS ACCESS KEY id",
            "AWS SECRET ACCESS KEY",
            "Default Region Name"

    3 - Run the create_table.py script with the command:
        python create_table.py

    
    4 - Start the application by running:
        python app.py
        


Running Tests: <br/>
To perform tests, use the following URL format:
http://127.0.0.1:5000/genius/<artist_name>

Test examples: <br/>

http://127.0.0.1:5000/genius/metallica

http://127.0.0.1:5000/genius/nirvana

http://127.0.0.1:5000/genius/nirvana?cache=False

http://127.0.0.1:5000/genius/aerosmith

http://127.0.0.1:5000/genius/eminem

http://127.0.0.1:5000/genius/eminem?cache=False

To view data in Redis, use redis-cli with the following commands:
KEYS * – View all artists saved in Redis

GET "artist_name" – Check the saved information of a specific artist

TTL "artist_name" – Check the expiration time (in seconds) of the record





