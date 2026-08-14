# Restaurant Order Recommendation Procedure

## Overview

This project implements a SQL Server stored procedure for retrieving restaurant food information and recommendations based on a selected menu item.

The procedure accepts a `MenuID` and returns information about the selected food, its prices, frequently ordered foods, and other recommended foods.

## Features

- Retrieves food information using `MenuID`
- Retrieves the original and special prices from the restaurant menu
- Provides multiple frequently ordered food recommendations
- Provides multiple "You May Also Like" recommendations
- Returns the results in JSON format
- Uses database relationships to connect food items with their recommendations
- Uses subqueries to prevent duplicate results when a food has multiple recommendations

## Database Structure

The procedure works with the restaurant menu and recommendation tables.

The recommendation tables allow one food item to have multiple:

- Frequently ordered foods
- You may also like foods

This makes the recommendation system flexible and allows recommendations to be changed in the database without changing the Python application.

## How It Works

1. A `MenuID` is provided to the stored procedure.
2. The procedure identifies the selected food from the restaurant menu.
3. The original and special prices are retrieved.
4. Frequently ordered foods associated with the selected food are retrieved.
5. Additional recommended foods are retrieved.
6. The results are returned as JSON.
7. The JSON response can then be consumed by a Python application.

## Python Integration

The stored procedure is called from Python using `pyodbc`.

Python sends the selected `MenuID` to SQL Server and receives the JSON response.

## Purpose

The goal of this procedure is to provide the backend logic for a restaurant ordering and recommendation system.

It separates the recommendation logic from the application layer, allowing the database to manage food relationships and recommendations efficiently.
