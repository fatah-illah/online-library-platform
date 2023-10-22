
---
# Online Library API

## Overview
This is a FastAPI based API for an online library system. It allows operations such as reading, creating, updating, and deleting books in the library database.

## Prerequisites
- Python 3.8+
- FastAPI
- mysql-connector-python

## Setup
1. Install the required dependencies:
```bash
pip install fastapi[all] mysql-connector-python
```

2. Clone this repository and navigate to its directory.

3. To run the server, use the following command:
```bash
uvicorn main:app --reload
```

4. Open your browser or an API testing tool like Postman and access the endpoints.

## Testing with Swagger UI
FastAPI comes with an integrated Swagger UI for testing and documentation. After starting the server:

1. Open your web browser and navigate to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. You will see an interactive API documentation where you can:
    - View all available endpoints.
    - Test the API operations directly from the browser.
    - View request and response models.
3. Click on an endpoint to expand its operations, and you can test each operation by clicking "Try it out".

## Endpoints
1. `GET /books/` - Retrieve all books
2. `GET /books/{book_id}` - Retrieve a specific book by its ID
3. `POST /books/` - Create a new book
4. `PUT /books/{book_id}` - Update a specific book by its ID
5. `DELETE /books/{book_id}` - Delete a book by its ID

## Testing
In addition to Swagger, refer to the `test_main.http` file for testing the endpoints using an API client.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

---
