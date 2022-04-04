[![Python 3.8](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)
<div align = "center">

<h1>Houseprice_Prediction_API_Deployment</h1>
</div>
ImmoElizas's API Machine learning model to predict prices on Belgium's real estate sales.

## Table of contents
[Description](#Description)  
[Installation](#Installation)  
[Usage](#Usage)  
[Output](#Output)  
[How it works](#How-it-works)  
[Examples](#Examples)  
[Authors](#Authors)

## Description
The API return the prediction the price of a propertie in Belgium, based on data scrapped from Immoweb. 
For the predictions our Machine Learning model looks at the relationship between the postal code, the state of the construction, the property subtype (apartment, studio, villa, chalet, ...), and existance of a fireplace, terrace, garden and/or fully equiped kitchen, an estimate of the asking price is made.
 
This API has been deployed with heroku under the url: https://immoanderlecht.herokuapp.com/

## Installation

Clone the repository:
```
git clone https://github.com/Saina2405/Houseprice_Prediction_API_Deployment.git
```

Install the requirements
```
pip install -r requirement.txt
```

## Usage
  
For the predictions, send a `POST` request to https://immoanderlecht.herokuapp.com/predict with the following parameters:
  
  ```json
{
  "data": {
    "area": int,
    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
    "rooms-number": int,
    "zip-code": int,
    "land-area": Optional[int],
    "garden": Optional[bool],
    "garden-area": Optional[int],
    "equipped-kitchen": Optional[bool],
    "full-address": Optional[str],
    "swimming-pool": Optional[bool],
    "furnished": Optional[bool],
    "open-fire": Optional[bool],
    "terrace": Optional[bool],
    "terrace-area": Optional[int],
    "facades-number": Optional[int],
    "building-state": Optional[
      "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
    ]
  }
}
```

Then the result from the API will be:
  ```json
{
      "prediction" : float
}
```
If there is any error on the type of the data, formatting or fields missing. The result willl be:

  ```json
{
      "error" : Optional[str]
}
```
## How it works
1. Processor  
First, the data are cleaned. That means that we drop all the entirely empty rows, string values
are cleaned up, outliers and properties without price and area indication are dropped, duplicates
and columns with the lowest correlation rate are deleted, and some other minor riddances.    

To put everything ready for the rest of the process, the variables that remain are transformed into
features.  

2. Model  
In the second step, the prediction is prepared. Firstly, the price, area, outside space and land
surface are rescaled. This is done in order to apreciate more linealy the relationship between price and area.

Secondly, the database is split and into a train and test dataframe. The first one is used to train the model.  

3. Predictor  
This object is going to be initializated when the app.py is runned. This predictor will load the model which is already trained to make the prediction.  

The data is checked to see if there is any error in the format or/and type, then preprocessed and it columns reformated in order to get a matrix with the required size and pased trough our model to get the prediction.  

4. app.py  
Here is where the `POST` and `GET` requests are processed.   

## Author
Saina Nuersulitan  