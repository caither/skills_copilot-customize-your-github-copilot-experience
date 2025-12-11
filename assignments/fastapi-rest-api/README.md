# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. Master HTTP methods, request/response handling, data validation, and API best practices while creating practical web services.

## 📝 Tasks

### 🛠️ Basic API Setup and Endpoints

#### Description
Create a basic FastAPI application with multiple endpoints. Set up the project structure and implement GET, POST, PUT, and DELETE operations for a simple resource.

#### Requirements
Completed program should:

- Initialize a FastAPI application with proper project structure
- Implement GET endpoint to retrieve all items and individual items by ID
- Implement POST endpoint to create new items with request body validation
- Implement PUT endpoint to update existing items
- Implement DELETE endpoint to remove items
- Use proper HTTP status codes (200, 201, 400, 404, etc.)
- Include basic error handling and meaningful error messages

### 🛠️ Data Validation with Pydantic

#### Description
Enhance API endpoints with robust data validation using Pydantic models. Ensure input data is validated automatically and API responses are properly typed.

#### Requirements
Completed program should:

- Define Pydantic models for request and response data structures
- Implement field validation with constraints (required fields, min/max values, email format, etc.)
- Provide automatic documentation of expected data formats
- Handle validation errors gracefully with descriptive messages
- Use type hints throughout the codebase
- Return properly typed responses with consistent structure

### 🛠️ Advanced Features and Documentation

#### Description
Add advanced features to the API including filtering, pagination, query parameters, and auto-generated interactive documentation.

#### Requirements
Completed program should:

- Implement query parameters for filtering and pagination
- Add path parameters and parameter validation
- Generate automatic API documentation (Swagger UI and ReDoc)
- Implement custom responses and status codes based on business logic
- Add request/response examples in API documentation
- Include proper logging for debugging and monitoring
- Handle edge cases and implement graceful error responses
