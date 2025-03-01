# Capstone Project: Advanced E-commerce API

- Author: Jaycob Hoffman

- Date: 28 February 2025

# Description

- This advanced e-commerce API is a dynamic, sophisticated, and intuitive API that simulates the multifarious functionalities of professional e-commerce websites. The program is built using Flask with SQLAlchemy, and includes features such as customer account creation, user authentication, the ability to place an order, as well as product and order data. This API is a working representation of the backend for today's intricate e-commerce technologies.

# Features

## Customer Operations

- **Create Customer**: Users can easily create new customers with a name, email, and phone number.
- **Get Customers**: Users can access data about all customers present in the system at the current time.
- **Update Customer**: Users can update customers by providing a new name, email, and/or phone.
- **Delete Customer**: Users can enter the unique ID of the customer they wish to delete to remove them from the system.

## Customer Account Operations

- **Customer Account Login**: Users can log a customer into their account by entering the associated customer's username, password, or role ("user" or "admin").
- **Get Customer Accounts**: Users can view all customer accounts and their associated customers.
- **Update Customer Account**: Users can update customer accounts by providing a new username, password, and/or role.
- **Delete Customer Account**: Users can enter the unique ID ofthe customer account they wish to delete to remove it from the system.

## Order Operations

- **Create Order**: Users can place an order for a product by specifying the product(s)' ID(s), their customer ID, and the date of purchase.
- **Get Order by ID**: Users can access data on individual orders by providing the order ID.

## Product Operations

- **Create Product**: Users can easily create a new product with a name and price.
- **Get Products**: Users can access data about all products present in the system at the current time.
- **Get Product by ID**: Users can access data on individual products by providing the product ID.
- **Update Product**: Users can update products by providing a new name and/or price.
- **Delete Product**: Users can remove products from the system by entering their associated IDs.

## Security and Authentication

All "Customer" and "Customer Account" operations require "admin" roles to access and use. If a user logs in with a role other than "admin" (e.g., "user"), they will not be given in authorization key. If the user possesses the "admin" role, they will be given an authorization key which they can use as a header when making requests to "Customer" and "Customer Account" endpoints. This key will expire after one day.

# More Information

For more detailed info on how to send requests, users can enter "/api/docs" following the port URL shown in the browser (e.g., "http://127.0.0.1:5000").

#

View the Advanced E-commerce API [GitHub Repository](https://github.com/JaycobHoffman1/Capstone-Project-Advanced-E-Commerce-API)