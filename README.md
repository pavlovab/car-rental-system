# Car Rental System

## Overview

The Car Rental System is a RESTful web service built using Python and Flask, designed to manage the rental of vehicles. This system allows users to manage cars, branches, customers, and rental transactions efficiently.

## Features

- **Car Management**: Add, update, delete, and view cars in the system.
- **Branch Management**: Manage rental branches where cars are available.
- **Customer Management**: Register and manage customers.
- **Rental Management**: Create, update, and view rental transactions, linking customers to the cars they rent.
- **Error Handling**: Graceful error handling for various operations, including validation and integrity checks.

## Technologies Used

- **Python**: Programming language used to build the application.
- **Flask**: A lightweight WSGI web application framework.
- **SQLAlchemy**: ORM for database interactions.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/car-rental-system.git
   cd car-rental-system

2. **Create a virtual environment**:

   ```bash
   python -m venv venv

3. **Activate the virtual environment**:

- On macOS/Linux:

   ```bash
   source venv/bin/activate

- On Windows:

   ```bash
   .\venv\Scripts\activate

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   
5. **Run the application**:

   ```bash
   python app.py


# Car Rental System API Documentation

## Car API Endpoints

### GET /api/cars
- **Description**: Retrieves a list of all cars in the system.
- **Request**: None
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (Example Data):
    ```json
    [
      {
        "id": 1,
        "make": "Toyota",
        "model": "Camry",
        "year": 2020,
        "rental_rate": 50.0,
        "availability": true,
        "branch_id": 2,
        "rentals": []
      },
      {
        "id": 2,
        "make": "Honda",
        "model": "Civic",
        "year": 2021,
        "rental_rate": 55.0,
        "availability": true,
        "branch_id": 3,
        "rentals": []
      }
    ]
    ```

---

### GET /api/cars/<int:car_id>
- **Description**: Retrieves details of a specific car by its ID.
- **Request**: None
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (Example Data):
    ```json
    {
      "id": 1,
      "make": "Toyota",
      "model": "Camry",
      "year": 2020,
      "rental_rate": 50.0,
      "availability": true,
      "branch_id": 2,
      "rentals": []
    }
    ```
  - **Status Code**: `404 Not Found` (if the car with the given ID does not exist)
  - **Body** (Example Data):
    ```json
    {
      "error": "Not Found"
    }
    ```

---

### POST /api/cars
- **Description**: Creates a new car in the system.
- **Request Body** (Example Data):
  - **Content-Type**: `application/json`
  - **Body**:
    ```json
    {
      "make": "Toyota",       // (required) String
      "model": "Camry",      // (required) String
      "year": 2020,          // (required) Integer
      "rental_rate": 50.0,   // (required) Float
      "branch_id": 2         // (required) Integer
    }
    ```
- **Response**:
  - **Status Code**: `201 Created`
  - **Body** (Example Data):
    ```json
    {
      "id": 1,
      "make": "Toyota",
      "model": "Camry",
      "year": 2020,
      "rental_rate": 50.0,
      "availability": true,
      "branch_id": 2,
      "rentals": []
    }
    ```
  - **Status Code**: `400 Bad Request` (if any required field is missing or if the branch ID is invalid)
  - **Body** (Example Data):
    ```json
    {
      "error": "Invalid branch_id field, specified branch does not exist."
    }
    ```

---

### PUT /api/cars/<int:car_id>
- **Description**: Updates details of a specific car.
- **Request Body** (Example Data):
  - **Content-Type**: `application/json`
  - **Body**:
    ```json
    {
      "make": "Toyota",       // (optional) String
      "model": "Corolla",     // (optional) String
      "year": 2021,           // (optional) Integer
      "rental_rate": 45.0,    // (optional) Float
      "availability": false,   // (optional) Boolean
      "branch_id": 2          // (optional) Integer
    }
    ```
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (Example Data):
    ```json
    {
      "id": 1,
      "make": "Toyota",
      "model": "Corolla",
      "year": 2021,
      "rental_rate": 45.0,
      "availability": false,
      "branch_id": 2,
      "rentals": []
    }
    ```
  - **Status Code**: `400 Bad Request` (if the branch ID is invalid)
  - **Body** (Example Data):
    ```json
    {
      "error": "Invalid branch_id field, specified branch does not exist."
    }
    ```

---

### DELETE /api/cars/<int:car_id>
- **Description**: Deletes a specific car from the system.
- **Request**: None
- **Response**:
  - **Status Code**: `204 No Content`
  - **Body**: None
  - **Status Code**: `400 Bad Request` (if the car is still associated with a rental)
  - **Body** (Example Data):
    ```json
    {
      "error": "Car removal failed. Car is probably still associated with a rental."
    }
    ```
  - **Status Code**: `404 Not Found` (if the car with the given ID does not exist)
  - **Body** (Example Data):
    ```json
    {
      "error": "Not Found"
    }
    ```

---

## Customer API Endpoints

### GET /api/customers
- **Description**: Retrieves a list of all customers in the system.
- **Request**: None
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (Example Data):
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "phone": "123-456-7890",
        "rentals": [
           {
               "id": 1,
               "car_id": 2,
               "customer_id": 1,
               "start_date": "2024-10-15",
               "end_date": "2024-10-20"
           }
    ]
      },
      {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane@example.com",
        "phone": "098-765-4321",
        "rentals": []  // This customer has no rentals
      }
    ]
    ```

---

### GET /api/customers/<int:customer_id>
- **Description**: Retrieves details of a specific customer by their ID.
- **Request**: None
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (Example Data):
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "123-456-7890",
      "rentals": []
    }
    ```
  - **Status Code**: `404 Not Found` (if the customer with the given ID does not exist)
  - **Body** (Example Data):
    ```json
    {
      "error": "Not Found"
    }
    ```

---

### POST /api/customers
- **Description**: Creates a new customer in the system.
- **Request Body** (Example Data):
  - **Content-Type**: `application/json`
  - **Body**:
    ```json
    {
      "name": "John Doe",       // (required) String
      "email": "john@example.com", // (required) String
      "phone": "123-456-7890"   // (required) String
    }
    ```
- **Response**:
  - **Status Code**: `201 Created`
  - **Body** (Example Data):
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "123-456-7890",
      "rentals": []
    }
    ```
  - **Status Code**: `400 Bad Request` (if any required field is missing)
  - **Body** (Example Data):
    ```json
    {
      "error": "Missing required field."
    }
    ```

---

### PUT /api/customers/<int:customer_id>
- **Description**: Updates details of a specific customer.
- **Request Body** (Example Data):
  - **Content-Type**: `application/json`
  - **Body**:
    ```json
    {
      "name": "John Smith",     // (optional) String
      "email": "johnsmith@example.com", // (optional) String
      "phone": "123-456-7891"   // (optional) String
    }
    ```
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (Example Data):
    ```json
    {
      "id": 1,
      "name": "John Smith",
      "email": "johnsmith@example.com",
      "phone": "123-456-7891",
      "rentals": []
    }
    ```

---

### DELETE /api/customers/<int:customer_id>
- **Description**: Deletes a specific customer from the system.
- **Request**: None
- **Response**:
  - **Status Code**: `204 No Content`
  - **Body**: None
  - **Status Code**: `400 Bad Request` (if the customer is still associated with a rental)
  - **Body** (Example Data):
    ```json
    {
      "error": "Customer removal failed. Customer is still probably associated with a rental."
    }
    ```
  - **Status Code**: `404 Not Found` (if the customer with the given ID does not exist)
  - **Body** (Example Data):
    ```json
    {
      "error": "Not Found"
    }
    ```

---

## Rental API Endpoints

### GET /api/rentals
- **Description**: Retrieves a list of all rentals in the system.
- **Request**: None
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (Example Data):
    ```json
    [
      {
        "id": 1,
        "car_id": 1,
        "customer_id": 1,
        "start_date": "2024-10-20",
        "end_date": "2024-10-27"
      },
      {
        "id": 2,
        "car_id": 2,
        "customer_id": 2,
        "start_date": "2024-10-21",
        "end_date": "2024-10-28"
      }
    ]
    ```

---

### GET /api/rentals/<int:rental_id>
- **Description**: Retrieves details of a specific rental by its ID.
- **Request**: None
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (Example Data):
    ```json
    {
      "id": 1,
      "car_id": 1,
      "customer_id": 1,
      "start_date": "2024-10-20",
      "end_date": "2024-10-27"
    }
    ```
  - **Status Code**: `404 Not Found` (if the rental with the given ID does not exist)
  - **Body** (Example Data):
    ```json
    {
      "error": "Not Found"
    }
    ```

---

### POST /api/rentals
- **Description**: Creates a new rental in the system.
- **Request Body** (Example Data):
  - **Content-Type**: `application/json`
  - **Body**:
    ```json
    {
      "car_id": 1,                // (required) Integer
      "customer_id": 1,           // (required) Integer
      "start_date": "2024-10-20", // (required) String (format: YYYY-MM-DD)
      "end_date": "2024-10-27"    // (required) String (format: YYYY-MM-DD)
    }
    ```
- **Response**:
  - **Status Code**: `201 Created`
  - **Body** (Example Data):
    ```json
    {
      "id": 1,
      "car_id": 1,
      "customer_id": 1,
      "start_date": "2024-10-20",
      "end_date": "2024-10-27"
    }
    ```
  - **Status Code**: `400 Bad Request` (if any required field is missing or invalid)
  - **Body** (Example Data):
    ```json
    {
      "error": "Rental creation failed. Check if IDs for Car and Customer are valid."
    }
    ```

---

### PUT /api/rentals/<int:rental_id>
- **Description**: Updates details of a specific rental.
- **Request Body** (Example Data):
  - **Content-Type**: `application/json`
  - **Body**:
    ```json
    {
      "start_date": "2024-10-21", // (optional) String (format: YYYY-MM-DD)
      "end_date": "2024-10-28"     // (optional) String (format: YYYY-MM-DD)
    }
    ```
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (Example Data):
    ```json
    {
      "id": 1,
      "car_id": 1,
      "customer_id": 1,
      "start_date": "2024-10-21",
      "end_date": "2024-10-28"
    }
    ```

---

### DELETE /api/rentals/<int:rental_id>
- **Description**: Deletes a specific rental from the system.
- **Request**: None
- **Response**:
  - **Status Code**: `204 No Content`
  - **Body**: None
  - **Status Code**: `404 Not Found` (if the rental with the given ID does not exist)
  - **Body** (Example Data):
    ```json
    {
      "error": "Not Found"
    }
    ```

---

## Branch API Endpoints

### GET /api/branches
- **Description**: Retrieves a list of all branches in the system.
- **Request**: None
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (Example Data):
    ```json
    [
      {
        "id": 1,
        "name": "Downtown Branch",
        "location": "123 Main St",
        "cars": []  // Cars associated with this branch
      },
      {
        "id": 2,
        "name": "Uptown Branch",
        "location": "456 Elm St",
        "cars": []  // Cars associated with this branch
      }
    ]
    ```

---

### GET /api/branches/<int:branch_id>
- **Description**: Retrieves details of a specific branch by its ID.
- **Request**: None
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (Example Data):
    ```json
    {
      "id": 1,
      "name": "Downtown Branch",
      "location": "123 Main St",
      "cars": []  // Cars associated with this branch
    }
    ```
  - **Status Code**: `404 Not Found` (if the branch with the given ID does not exist)
  - **Body** (Example Data):
    ```json
    {
      "error": "Not Found"
    }
    ```

---

### POST /api/branches
- **Description**: Creates a new branch in the system.
- **Request Body** (Example Data):
  - **Content-Type**: `application/json`
  - **Body**:
    ```json
    {
      "name": "Downtown Branch",  // (required) String
      "location": "123 Main St"    // (required) String
    }
    ```
- **Response**:
  - **Status Code**: `201 Created`
  - **Body** (Example Data):
    ```json
    {
      "id": 1,
      "name": "Downtown Branch",
      "location": "123 Main St",
      "cars": []  // Cars associated with this branch
    }
    ```
  - **Status Code**: `400 Bad Request` (if any required field is missing)
  - **Body** (Example Data):
    ```json
    {
      "error": "Missing required field."
    }
    ```

---

### PUT /api/branches/<int:branch_id>
- **Description**: Updates details of a specific branch.
- **Request Body** (Example Data):
  - **Content-Type**: `application/json`
  - **Body**:
    ```json
    {
      "name": "New Branch Name",     // (optional) String
      "location": "789 Oak St"        // (optional) String
    }
    ```
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (Example Data):
    ```json
    {
      "id": 1,
      "name": "New Branch Name",
      "location": "789 Oak St",
      "cars": []  // Cars associated with this branch
    }
    ```

---

### DELETE /api/branches/<int:branch_id>
- **Description**: Deletes a specific branch from the system.
- **Request**: None
- **Response**:
  - **Status Code**: `204 No Content`
  - **Body**: None
  - **Status Code**: `400 Bad Request` (if there are associated cars with the branch)
  - **Body** (Example Data):
    ```json
    {
      "error": "Can not delete branch, associated cars still exist."
    }
    ```
  - **Status Code**: `404 Not Found` (if the branch with the given ID does not exist)
  - **Body** (Example Data):
    ```json
    {
      "error": "Not Found"
    }
    ```
