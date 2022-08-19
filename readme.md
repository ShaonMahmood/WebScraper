A simple scarping system build with Python
=================

**Tested on MacOS(m1)**

Simple Ebay Scraper build with python, scrapy and mongodb 

## Prerequisites

 - Must have docker and docker compose installed on your computer. 
 - For docker engine see, https://docs.docker.com/engine/install
 - For docker compose see, https://docs.docker.com/compose/install
 - Need Mongodb compass to view the scraped data. see, https://www.mongodb.com/try/download/compass


## Project Specifications

Build a simple and efficient scraping system that accepts the URL of a specific website and scrapes a list
of items with price. The system should also be able to scrap data if there are paginations. The result
must be stored in the MongoDB database collection. Data imported from multiple web pages should
match the standard database columns and structure. It would be best if you kept the web page URL so it
could be configured and updated. The application should return the status after finishing or any issue
with the process. Assume that your app will run on a very low configuration machine.

## Project Requirements

 - Programming Language: Python 3.x.
 - Preferred Database: MongoDB.
 - Project should be packed and built on Docker.
 - Preferred if maintain OOP.
 - Preferred if maintain common security concern.
 - Maximum execution time of each scraping should not exceed 30s.
 - Should be able to handle large data.
 - Should handle all the errors

## Installation

Clone the repo using mac/linux terminal:

    git clone https://github.com/ShaonMahmood/WebScraper
    cd WebScraper

If You Have zip file, unzip it first and then chnage the directory, i used ubuntu's unzip:

    unzip WebScraper-main.zip
    cd WebScraper-main/

make a copy of env.example file to a file named .env. You can configure the url and serch item here. then run the following in terminal.

```sh
docker-compose up -d --build
```

The app container is up and running. you should see the logs in the terminal. The product is loaded as expected. You can verify it by inspecting the database using mongodb-compass at http://localhost:27017


## Uninstall/ Clean up Containers
Full clean up

```sh
docker-compose down -v
docker-compose rm -fs
docker system prune 

```

## Improvement

* Should have included proper Test Cases
* App Structure could be improved
* Could have more simpler solution but i select scarpy for its robustness, concurrent support and ease of use.