# Flask API Documentation
This is a simple Flask API for managing documents and generating recommended similar documents.

API Endpoints
This Flask API application provides several endpoints to interact with a collection of documents stored in memory.

Retrieving all documents:
Endpoint: GET /documents
Description: Returns a list of all documents in the collection
Response: JSON object containing a list of documents

Creating a new document:
Endpoint: POST /documents
Description: Creates a new document in the collection
Request body: JSON object containing document title, author, and content
Response: JSON object containing the newly created document

Retrieving a specific document:
Endpoint: GET /documents/int:document_id
Description: Returns a specific document by ID
Parameters: document_id (integer)
Response: JSON object containing the specified document or an error message if not found

Updating a specific document:
Endpoint: PUT /documents/int:document_id
Description: Updates a specific document by ID
Parameters: document_id (integer)
Request body: JSON object containing the updated document fields
Response: JSON object containing the updated document or an error message if not found

Deleting a specific document:
Endpoint: DELETE /documents/int:document_id
Description: Deletes a specific document by ID
Parameters: document_id (integer)
Response: Empty response with HTTP status code 204 if the document is successfully deleted or an error message if not found

Generating recommended similar documents:
Endpoint: POST /recommendations
Description: Generates a list of recommended similar documents based on a given document
Request body: JSON object containing the document for which to generate recommendations
Response: JSON object containing a list of recommended documents

Retrieving previously generated recommended similar documents:
Endpoint: GET /recommendations
Description: Retrieves a list of recommended similar documents previously generated
Response: JSON object containing a list of recommended documents

To run the application, navigate to the project directory in a terminal window and execute the command "python app.py". The application will run on http://localhost:5000/ by default.

Note: This application does not include authentication or authorization features and is intended for demonstration purposes only.
