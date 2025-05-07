# Predicting Area of Countries using Decision Trees

This project is a simple example of using data from a website (https://www.scrapethissite.com/pages/simple/) and storing it in a MySQL database. Then, a decision tree model is trained to predict the area of countries based on their population.

## Features:
- Scraping data from a website using `BeautifulSoup`
- Storing data in a MySQL database
- Using a Decision Tree Classifier (`DecisionTreeClassifier`) to predict the area of countries

## Process Overview:

### 1. Scraping Data from the Website

Initially, this project fetches data from a specific website and extracts country name, capital, population, and area. The scraped data is then stored in a MySQL database.

### 2. Storing Data in a MySQL Database

The project uses a MySQL database to store the scraped data. The data is inserted into a table named `takhmin` in the database.

### 3. Training the Prediction Model

After the data is stored in the database, it reads the data and uses it to train a decision tree model. The model is trained to predict the area of countries based on their population.

### 4. Predicting the Area of a Country

Once the model is trained, you can use it to predict the area of a new country based on its population.

## Installation and Setup:

### Prerequisites:
Before running the project, make sure you have the following libraries installed:
- `requests`
- `beautifulsoup4`
- `mysql-connector-python`
- `scikit-learn`

You can install all the dependencies by running the following command:

```bash
pip install -r requirements.txt
