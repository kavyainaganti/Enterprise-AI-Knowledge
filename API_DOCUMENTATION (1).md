# Enterprise AI Knowledge System
## REST API Documentation

**Version:** 1.0  
**Backend Framework:** FastAPI  
**Frontend:** JavaScript / Vite  
**Large Language Model:** Google Gemini  
**Embedding Model:** BGE-M3  
**Vector Database:** Qdrant  

> **Implementation note:** This document is a detailed API documentation draft based on the project's stated technology stack. The endpoint paths, request schemas, and response examples below are proposed conventions, not verified descriptions of the current backend. Confirm them against the actual FastAPI route definitions and Pydantic schemas before publishing as the final API reference.

---

## 1. Introduction

The Enterprise AI Knowledge System is an AI-powered knowledge management application. It allows users to upload documents, process their content, search the knowledge base using natural language, and ask questions about stored documents.

The backend exposes REST APIs that connect the frontend with document-processing services, the embedding model, vector database, and large language model.

### Main functionalities

- Upload and manage documents.
- Extract text from supported document formats.
- Generate vector embeddings using BGE-M3.
- Store and retrieve document embeddings using Qdrant.
- Perform semantic searches.
- Generate contextual answers using Google Gemini.
- Return answers and, where supported, source references to the frontend.

## 2. System Architecture

```text
             FRONTEND
          JavaScript / Vite
                 |
                 | HTTP Requests
                 v
          FASTAPI BACKEND
                 |
        +--------+---------+
        |                  |
        v                  v
 DOCUMENT PROCESSING    QUESTION PROCESSING
        |                  |
        v                  v
 Text Extraction       Query Processing
        |                  |
        v                  v
 BGE-M3 EMBEDDINGS     BGE-M3 EMBEDDINGS
        |                  |
        v                  v
        +------ QDRANT ----+
                 |
                 v
          CONTEXT RETRIEVAL
                 |
                 v
          GOOGLE GEMINI
                 |
                 v
          GENERATED ANSWER
                 |
                 v
              FRONTEND
```

## 3. Base URL

For local development, the default FastAPI address is:

`http://localhost:8000`

The actual API base URL may differ depending on deployment configuration.

## 4. API Request Standards

### 4.1 HTTP methods

| Method | Purpose |
|---|---|
| GET | Retrieve information |
| POST | Upload data or submit a request |
| PUT | Replace an existing resource |
| PATCH | Partially update a resource |
| DELETE | Delete a resource |

### 4.2 Content types

For JSON requests:

`Content-Type: application/json`

For document uploads:

`Content-Type: multipart/form-data`

### 4.3 Example response envelope

A successful JSON response may use a structure such as:

```json
{
  "success": true,
  "message": "Request completed successfully",
  "data": {}
}
```

The actual response structure depends on the backend implementation.

---

# 5. API Endpoint Documentation

The following endpoints form a suggested API contract. Confirm the actual paths and fields in the FastAPI route files before treating them as implemented.

## 5.1 Health Check API

**Endpoint:** `GET /health`

**Purpose:** Checks whether the backend application is running.

### Example request

```http
GET /health
```

### Example response

```json
{
  "status": "healthy",
  "message": "Enterprise AI Knowledge System is running"
}
```

### Possible status codes

- `200 OK` – Backend is running.
- `500 Internal Server Error` – Unexpected server error.

## 5.2 Document Upload API

**Endpoint:** `POST /documents/upload`

**Purpose:** Allows users to upload documents for processing and knowledge extraction.

**Request type:** `multipart/form-data`

### Form data

| Parameter | Type | Required | Description |
|---|---|---|---|
| file | File | Yes | Document to upload |

**Supported file types:** Confirm the formats enabled in the document-processing code. Common formats include PDF, DOCX, PPTX, and TXT.

### Example request

```http
POST /documents/upload
Content-Type: multipart/form-data
```

Form field: `file` — select the document to upload.

### Example response

```json
{
  "success": true,
  "message": "Document uploaded successfully",
  "data": {
    "document_id": "doc_001",
    "filename": "company_policy.pdf",
    "status": "processing"
  }
}
```

### Suggested processing workflow

1. Receive the uploaded document.
2. Validate its file type and size.
3. Extract text from the document.
4. Divide extracted text into smaller chunks.
5. Generate embeddings using BGE-M3.
6. Store vectors and associated metadata in Qdrant.
7. Make the document available for retrieval.

### Possible status codes

- `200 OK` – Upload successful.
- `400 Bad Request` – Invalid upload request.
- `413 Payload Too Large` – File exceeds configured size limit.
- `415 Unsupported Media Type` – Unsupported file type.
- `500 Internal Server Error` – Processing or server error.

## 5.3 Retrieve All Documents API

**Endpoint:** `GET /documents`

**Purpose:** Retrieves the list of documents available in the knowledge system.

### Example request

```http
GET /documents
```

### Example response

```json
{
  "success": true,
  "documents": [
    {
      "document_id": "doc_001",
      "filename": "company_policy.pdf",
      "status": "completed"
    },
    {
      "document_id": "doc_002",
      "filename": "employee_handbook.docx",
      "status": "completed"
    }
  ]
}
```

### Possible status codes

- `200 OK` – Documents retrieved successfully.
- `500 Internal Server Error` – Unable to retrieve documents.

## 5.4 Retrieve a Specific Document API

**Endpoint:** `GET /documents/{document_id}`

**Purpose:** Retrieves details about a particular document.

### Path parameters

| Parameter | Type | Description |
|---|---|---|
| document_id | String | Unique document identifier |

### Example request

```http
GET /documents/doc_001
```

### Example response

```json
{
  "success": true,
  "document": {
    "document_id": "doc_001",
    "filename": "company_policy.pdf",
    "status": "completed"
  }
}
```

### Possible status codes

- `200 OK` – Document found.
- `404 Not Found` – Document does not exist.
- `500 Internal Server Error` – Server error.

## 5.5 Delete Document API

**Endpoint:** `DELETE /documents/{document_id}`

**Purpose:** Deletes a selected document from the knowledge system.

### Example request

```http
DELETE /documents/doc_001
```

### Example response

```json
{
  "success": true,
  "message": "Document deleted successfully"
}
```

The deletion process should remove the document's associated vectors from Qdrant and its metadata from the document registry, where applicable.

### Possible status codes

- `200 OK` – Document deleted.
- `404 Not Found` – Document not found.
- `500 Internal Server Error` – Deletion failed.

## 5.6 AI Question Answering API

**Endpoint:** `POST /chat`

**Purpose:** Allows users to ask questions about documents stored in the Enterprise Knowledge System.

This is the main Retrieval-Augmented Generation (RAG) operation.

### Example request body

```json
{
  "question": "What is the company's leave policy?"
}
```

### Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| question | String | Yes | User's natural-language question |

### Processing workflow

1. Receive the user's question.
2. Generate a query embedding using BGE-M3.
3. Search for relevant document vectors in Qdrant.
4. Retrieve the most relevant text chunks.
5. Send the question and retrieved context to Google Gemini.
6. Generate an answer based on the retrieved information.
7. Return the answer and, if implemented, its source references.

### Example response

```json
{
  "success": true,
  "question": "What is the company's leave policy?",
  "answer": "Employees are entitled to annual leave according to the company policy.",
  "sources": [
    {
      "filename": "company_policy.pdf",
      "page": 5
    }
  ]
}
```

The source information is illustrative. Actual citations depend on the metadata stored and returned by the backend.

### Possible status codes

- `200 OK` – Answer generated successfully.
- `400 Bad Request` – Invalid question.
- `404 Not Found` – No relevant information found, if handled this way.
- `500 Internal Server Error` – AI or backend processing failure.
- `503 Service Unavailable` – Required external service unavailable.

## 5.7 Semantic Search API

**Endpoint:** `POST /search`

**Purpose:** Finds relevant document content based on the meaning of a user's query.

### Example request

```json
{
  "query": "Employee attendance rules",
  "top_k": 5
}
```

### Request parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| query | String | Yes | Search query |
| top_k | Integer | No | Maximum number of results to retrieve |

### Example response

```json
{
  "success": true,
  "results": [
    {
      "document_id": "doc_001",
      "filename": "company_policy.pdf",
      "content": "Employees must follow the attendance policy...",
      "score": 0.89
    }
  ]
}
```

The similarity score and result fields depend on the retrieval implementation.

### Possible status codes

- `200 OK` – Search completed.
- `400 Bad Request` – Invalid search query.
- `500 Internal Server Error` – Search service failure.

---

# 6. AI Technology Integration

## 6.1 Google Gemini

Google Gemini is used as the Large Language Model (LLM) for generating natural-language responses.

**Responsibilities:**

- Understand user questions.
- Process retrieved document context.
- Generate contextual answers.
- Provide responses in a readable format.

## 6.2 BGE-M3 Embedding Model

BGE-M3 converts text into numerical vector representations.

**Responsibilities:**

- Generate embeddings for document chunks.
- Generate embeddings for user queries.
- Support semantic similarity-based retrieval.

## 6.3 Qdrant Vector Database

Qdrant stores and retrieves vector representations of document content.

**Responsibilities:**

- Store document embeddings.
- Store associated metadata.
- Perform similarity searches.
- Return relevant document chunks for question answering.

---

# 7. Error Handling

The API should return appropriate HTTP status codes and meaningful error messages.

| Status Code | Meaning | Description |
|---|---|---|
| 200 | OK | Request successful |
| 201 | Created | Resource created |
| 400 | Bad Request | Invalid request |
| 401 | Unauthorized | Authentication required |
| 403 | Forbidden | Permission denied |
| 404 | Not Found | Resource not found |
| 413 | Payload Too Large | Uploaded file too large |
| 415 | Unsupported Media Type | Unsupported file type |
| 422 | Validation Error | Request data validation failed |
| 500 | Internal Server Error | Unexpected server error |
| 503 | Service Unavailable | Required service unavailable |

### Example error response

```json
{
  "detail": "Invalid request. Please provide a valid question."
}
```

---

# 8. API Testing

FastAPI automatically generates interactive API documentation using OpenAPI.

After starting the backend, open:

**Swagger UI:** `http://localhost:8000/docs`

**ReDoc:** `http://localhost:8000/redoc`

These interfaces allow developers to:

- View available API endpoints.
- Inspect request parameters.
- View response schemas.
- Execute API requests.
- Test endpoints without using the frontend.

---

# 9. Security Considerations

The API should follow these security practices:

1. Store API keys in environment variables.
2. Never expose Gemini API credentials in frontend code.
3. Validate uploaded document types and sizes.
4. Restrict access to sensitive documents where required.
5. Validate incoming API requests.
6. Configure CORS to allow only trusted frontend origins.
7. Avoid logging sensitive document contents or credentials.
8. Use HTTPS in production.
9. Implement authentication and authorization if required by the application.

---

# 10. Conclusion

The Enterprise AI Knowledge System API provides the communication layer between the frontend and the AI-powered backend.

FastAPI handles incoming requests, BGE-M3 generates embeddings, Qdrant performs vector retrieval, and Google Gemini generates contextual answers.

Together, these components support an intelligent document-based knowledge retrieval and question-answering system.

---

## Documentation Verification Checklist

Before publishing this document as the final API reference:

- [ ] Confirm every endpoint path against the FastAPI route definitions.
- [ ] Confirm request fields and required parameters.
- [ ] Confirm response schemas and HTTP status codes.
- [ ] Confirm supported document formats and upload limits.
- [ ] Confirm whether document listing, retrieval, and deletion are implemented.
- [ ] Confirm whether semantic search is exposed as a separate endpoint.
- [ ] Confirm authentication and authorization behavior.
- [ ] Test the documented endpoints through Swagger UI.

**Final note:** This document is a proposed API reference, not a verified record of the current implementation. Update it using the actual backend routes and schemas before presenting it as an implemented API specification.
