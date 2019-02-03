# Key Value Store
This an assignment for Software Development curse Database.

The project is written in python with a flask api facade.

## Features 

- Key-value store database
- Write data to a database file
- Read data from the database file
- Offsets stored in momory for faster reading
- Ability to generate the offsets if program is launched with an existing database

## How to run 
Clone the project
`git clone https://github.com/Alfen321/KeyValueStore.git`

### Run in docker
1. Run docker container
`bash docker_run`
or
`docker run -it --rm -p 5000:5000 -v /$(pwd)://app:rw alfen321/simpledb:latest`

1. Access facade page on `localhost:5000`

### Run on local python
1. Install required python libraries:
`pip3 install -r requirements`
1. Run the program:
`python3 main.py`