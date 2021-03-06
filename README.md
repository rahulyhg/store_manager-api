## Store Manager [![Build Status](https://travis-ci.org/missvicki/store_manager-api.svg?branch=heroku)](https://travis-ci.org/missvicki/store_manager-api) [![Coverage Status](https://coveralls.io/repos/github/missvicki/store_manager-api/badge.svg?branch=heroku)](https://coveralls.io/github/missvicki/store_manager-api?branch=heroku) [![Maintainability](https://api.codeclimate.com/v1/badges/a68f287f8f7b9bf13c07/maintainability)](https://codeclimate.com/github/missvicki/store_manager-api/maintainability)

Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.    

## Getting Started

For installation of this project:  `$ git clone 'https://github.com/missvicki/store_manager-api.git`

## Prerequisites

* Create a Virtual Environment e.g.: `$ virtualenv storemanager`
* Activate the environment: 
    * For Windows: `$c:/ .\storemanager\Scripts\activate`
    * For Linux and Mac: `$ source storemanager/bin/activate`
* Install project dependencies e.g. flask: `$ pip install -r requirements.txt`

## Features

* Admin: 
    * can create a product
    * can get all products
    * can get a specific product 
    * can delete a product
    * can modify a single product

    * can get all sale orders
    * can get a single sale made by attendant

    * can create new users
    * can login
    * can view all users
    * can delete users


* Attendant:
    * can login

    * can create a sale order of a product

    * can get all products 
    * can get a specific product
    * can create a product


## Heroku Endpoints

| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| POST |[/api/v1/auth/signup](https://store-manager-api-.herokuapp.com/api/v1/auth/signup)|Create a New User|
| POST |[/api/v1/auth/login](https://store-manager-api-.herokuapp.com/api/v1/auth/login)|Login|
| POST | [/api/v1/products](https://store-manager-api-.herokuapp.com/api/v1/products) | Creates a product |
| POST | [/api/v1/sales](https://store-manager-api-.herokuapp.com/api/v1/sales) | Creates a sales order |
| GET | [/api/v1/products](https://store-manager-api-.herokuapp.com/api/v1/products) | Fetches all products|
| GET | [/api/v1/products/product_id](https://store-manager-api-.herokuapp.com/api/v1/products/1) | Fetches a single product |
| GET | [/api/v1/sales](https://store-manager-api-.herokuapp.com/api/v1/sales) | Fetches all sales |
| GET | [/api/v1/users](https://store-manager-api-.herokuapp.com/api/v1/users) | Fetches all users |
| DELETE | [/api/v1/products/product_id](https://store-manager-api-.herokuapp.com/api/v1/products/1) | Deletes a product |
| DELETE | [/api/v1/users/user_id](https://store-manager-api-.herokuapp.com/api/v1/users/1) | Deletes a single user |
| PUT | [/api/v1/products/product_id](https://store-manager-api-.herokuapp.com/api/v1/products/1) | Modifies a single product |

## Testing the app

`$nosetests --with-cov --cov  tests/`
  
## Language

**Python**: 3.6.5

## Run the app

`$ python run.py`

## Authors

* **Victor Nomwesigwa**

## Acknowledgments

* Thank you to Andela for the opportunity of giving me this challenge
* My fellow Andela bootcampers, thank you for the help rendered to me when I was stranded





