# Rick and Morty Character Scraper

This project contains a Python script that queries the **Rick and Morty API** and filters characters based on the following criteria:

- ✅ Species: Human  
- ✅ Status: Alive  
- ✅ Origin: contains the word "Earth"

The results are saved to a **CSV file** with the following information for each character:

- Name  
- Location  
- Image URL

---

## 🚀 How to Run the Script

### 1. Clone the Repository

```bash
git clone https://github.com/LiavHackmon/rick-and-morty-filter.git
cd rick-and-morty-filter

Make sure Python 3 is installed, then install the required package

Run the Script - This will generate a file called rick_and_morty_characters.csv.

This script uses the Rick and Morty API.

## Bonus: Dockerized REST API Service

This project now includes a Dockerized Flask REST API service that provides endpoints to fetch the filtered Rick and Morty character data as JSON.

### REST API Endpoints

- **GET /**  
  Returns a simple homepage with navigation buttons to the other endpoints.

- **GET /characters**  
  Returns a webpage displaying alive human characters from Earth with images and locations.

- **GET /healthcheck**  
  Returns a simple health check status page.

### How to Build the Docker Image

Make sure you have Docker installed.  
Run this command in the directory containing the `Dockerfile` and `app.py`:

```bash
docker build -t rick-and-morty-api .

docker run -p 5000:5000 rick-and-morty-api
