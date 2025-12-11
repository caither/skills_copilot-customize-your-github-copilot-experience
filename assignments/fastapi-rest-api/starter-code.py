from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Task API",
    description="A simple Task management API built with FastAPI",
    version="1.0.0"
)

# TODO: Define Pydantic models for data validation
# Create Task and TaskUpdate models with appropriate fields and validation


# Sample in-memory database (replace with real database in production)
tasks_db = {}
next_task_id = 1


# Task 1: Basic API Setup and Endpoints
# ======================================

@app.get("/")
async def root():
    """Root endpoint that returns API information."""
    return {
        "message": "Welcome to Task API",
        "version": "1.0.0",
        "endpoints": {
            "tasks": "/tasks",
            "docs": "/docs"
        }
    }


@app.get("/tasks")
async def get_all_tasks():
    """
    TODO: Get all tasks
    - Return all tasks from the database
    - Handle empty database gracefully
    """
    pass


@app.get("/tasks/{task_id}")
async def get_task(task_id: int):
    """
    TODO: Get a specific task by ID
    - Retrieve task by ID
    - Return 404 if task not found
    """
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_task(task):
    """
    TODO: Create a new task
    - Validate input using Pydantic model
    - Generate unique ID
    - Store in database
    - Return created task with ID
    """
    pass


@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task):
    """
    TODO: Update an existing task
    - Find task by ID
    - Update fields
    - Return updated task or 404 if not found
    """
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    """
    TODO: Delete a task by ID
    - Find and remove task
    - Return 204 No Content on success
    - Return 404 if task not found
    """
    pass


# Task 2: Data Validation with Pydantic
# ======================================
# TODO: Implement Pydantic models above for:
# - Task (with id, title, description, completed status, created_at)
# - TaskUpdate (for PATCH/PUT operations)
# - Include field validation:
#   - Title: required, min 1 character, max 100
#   - Description: optional, max 500
#   - Status: boolean with default False


# Task 3: Advanced Features
# ==========================

@app.get("/tasks/search")
async def search_tasks(
    skip: int = 0,
    limit: int = 10,
    completed: Optional[bool] = None
):
    """
    TODO: Implement search with filtering and pagination
    - Filter by completion status
    - Support pagination with skip and limit
    - Return filtered results
    """
    pass


# TODO: Add more advanced features:
# - Custom status codes based on conditions
# - Logging for API requests
# - Detailed error responses with example format
# - Request/response examples in docstrings


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
