**API Documentation**

SMS Transactions API

# Project Information

| **Project name** | _MoMo SMS Analyzer Formative Assessment_ |
| --- | --- |
| **Last updated** | _29<sup>th</sup> September 2026_ |
| --- | --- |
| **Team** | _Team 4 Cohort 1_ |
| --- | --- |

# Endpoint Summary

| **Method** | **Path** | **Description** | **Documented by** |
| --- | --- | --- | --- |
| GET | /transactions | Lists all SMS transactions | Joshua Gunnogere Mulongo |
| --- | --- | --- | --- |
| GET | /transactions/{id} | Returns a single transaction | _Didier Abizera_ |
| --- | --- | --- | --- |
| POST | /transactions | Adds a new transaction | _Josue Rene Nsengiyumva_ |
| --- | --- | --- | --- |
| PUT | /transactions/{id} | Updates an existing transaction | _Josue Rene Nsengiyumva_ |
| --- | --- | --- | --- |
| DELETE | /transactions/{id} | Deletes a transaction | _\[Name\]_ |
| --- | --- | --- | --- |

## Common Error Formats

_Error formats shared by most endpoints, so each section can stay short._

{

"error": "Invalid JSON"

}

or

{

“error": "Transaction not found"

}

Or

{

"error": "Authentication required"

}

Or

{

"Error": "Invalid Transaction ID”

}

# 1\. GET /transactions

| **Documented by** | _Joshua Gunnogere Mulongo_ |
| --- | --- |
| **Date** | _29/09/2026_ |
| --- | --- |

## 1.1 Endpoint & Method

| **Method** | GET |
| --- | --- |
| **URL** | /transactions |
| --- | --- |
| **Description** | _Lists all SMS transactions currently loaded from the parsed dataset._ |
| --- | --- |
| **Authentication** | _Basic Auth required. Send as an Authorization: Basic &lt;base64-encoded username:password&gt; header._ |
| --- | --- |

## 1.2 Request Parameters

<div class="joplin-table-wrapper"><table><thead><tr><th><p><strong>Name</strong></p></th><th><p><strong>Location</strong></p></th><th><p><strong>Type</strong></p></th><th><p><strong>Required</strong></p></th><th><p><strong>Description</strong></p></th></tr><tr><th><p><em>None</em></p></th><th><p>-</p></th><th><p>-</p></th><th><ul><li></li></ul></th><th><p>This endpoint takes no parameters</p></th></tr></thead></table></div>

_Add or remove rows as needed. Write "None" if the endpoint takes no parameters._

## 1.3 Request Example

curl -u admin:momo2026 http://localhost:8000/transactions

## 1.4 Response Example

_Show a real successful response: status code, then the body._

**Success – 200 OK**

\[

{

"protocol": "0",

"address": "M-Money",

"date": "1715351458724",

"body": "You have received 2000 RWF from Jane Smith...",

"id": 1

},

{

"protocol": "0",

"address": "M-Money",

"date": "1715351523000",

"body": "You have paid 12500 RWF to...",

"id": 2

}

\]

## 1.5 Error Codes

| **Status code** | **Meaning** | **When it happens** | **Example response** |
| --- | --- | --- | --- |
| 401 | Unauthorized | _Missing or incorrect username/password_ | _{"error": "Authentication required"}_ |
| --- | --- | --- | --- |

_Only list the codes your implementation really returns._

## 1.6 Notes

_Optional: edge cases, limitations, known issues, or tips for other developers._

Returns the full list of transactions as currently loaded in memory from dsa/sms_records.json; the list is not paginated, so all records are returned in a single response.

# 2\. GET /transactions/{id}

| **Documented by** | _Didier Abizera_ |
| --- | --- |
| **Date** | 29/09/2026 |
| --- | --- |

## 2.1 Endpoint & Method

| **Method** | GET |
| --- | --- |
| **URL** | /transactions/{id} |
| --- | --- |
| **Description** | _Retrieves a single transaction by its ID, using linear search to scan the transaction list for a match_ |
| --- | --- |
| **Authentication** | _Basic Auth required. Send as an Authorization: Basic &lt;base64-encoded username:password&gt; header_ |
| --- | --- |

## 2.2 Request Parameters

| **Name** | **Location** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| id  | Path | integer | Yes | _The unique ID of the transaction to retrieve_ |
| --- | --- | --- | --- | --- |

_Add or remove rows as needed. Write "None" if the endpoint takes no parameters._

## 2.3 Request Example

curl -u admin:momo2026 http://localhost:8000/transactions/1

## 2.4 Response Example

_Show a real successful response: status code, then the body._

**Success – 200 OK**

{

"protocol": "0",

"address": "M-Money",

"date": "1715351458724",

"type": "1",

"body": "You have received 2000 RWF from Jane Smith (\*\*\*\*\*\*\*\*\*013) on your mobile money account at 2024-05-10 16:30:51. Message from sender: . Your new balance:2000 RWF. Financial Transaction Id: 76662021700.",

"service_center": "+250788110381",

"readable_date": "10 May 2024 4:30:58 PM",

"id": 1

}

## 2.5 Error Codes

| **Status code** | **Meaning** | **When it happens** | **Example response** |
| --- | --- | --- | --- |
| 404 | Not Found | No transaction exists with the given ID | _https://claude.ai/chat/bf134e74-7b2a-4254-b708-5f80e66056d2#:~:text=%7B%22error%22%3A%20%22Transaction%20not%20found%22%7D_ |
| --- | --- | --- | --- |
| 401 | Unauthorized | _Missing or incorrect username/password_ | _{"error": "Authentication required"}_ |
| --- | --- | --- | --- |
| 400 | Bad Request | _The ID in the URL isn't a valid number_ | _{"error": "Invalid transaction ID"}_ |
| --- | --- | --- | --- |
| _\[code\]_ | _\[meaning\]_ | _\[when\]_ | _\[example\]_ |
| --- | --- | --- | --- |

_Only list the codes your implementation really returns._

## 2.6 Notes

_Optional: edge cases, limitations, known issues, or tips for other developers._

The GET /transactions/{id} endpoint uses linear search (checking each transaction one by one) rather than the dictionary lookup used in DELETE /transactions/{id}. This is intentional, matching the assignment's DSA requirement to implement and later compare both search methods.

# 3\. POST /transactions

| **Documented by** | _Josue Rene Nsengiyumva_ |
| --- | --- |
| **Date** | _29<sup>th</sup> September 2026_ |
| --- | --- |

## 3.1 Endpoint & Method

| **Method** | POST |
| --- | --- |
| **URL** | /transactions |
| --- | --- |
| **Description** | Adds a new SMS transaction. The server reads a JSON object from the request body, assigns it a new numeric ID, stores it, and returns the created record. |
| --- | --- |
| **Authentication** | Authentication is required. HTTP Basic Auth: send an Authorization header with base64(username: password). Requests without valid credentials receive 401. |
| --- | --- |

## 3.2 Request Parameters

| **Name** | **Location** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| Authorization | Header | string | Yes | Basic &lt;base64(username:password)&gt; |
| --- | --- | --- | --- | --- |
| Content-Type | Header | string | Recommended | application/json not enforced, but the body is always parsed as JSON. |
| --- | --- | --- | --- | --- |
| Content-Type | Header | integer | Yes | Size of the body in bytes. Added automatically by curl and Postman. If missing, the body is empty and the request fails with 400. |
| --- | --- | --- | --- | --- |
| Transaction fields | Body | JSON Object | Yes | Any valid JSON object. Use the same fields as the records in sms_records.json. |
| --- | --- | --- | --- | --- |
| id  | Body | integer | No  | Ignored. The server always assigns the id itself. |
| --- | --- | --- | --- | --- |

## 3.3 Request Example

curl -X POST http://localhost:8000/transactions \\

\-u username:password \\

\-H "Content-Type: application/json" \\

\-d '{"type": "received", "amount": 5000, "sender": "Jane Doe", "date": "2026-09-01 10:30:00"}'

## 3.4 Response Example

_Show a real successful response: status code, then the body._

**Success – 201 Created**

{

"type": "received",

"amount": 5000,

"sender": "Jane Doe",

"date": "2026-09-01 10:30:00",

"id": 101

}

## 3.5 Error Codes

| **Status code** | **Meaning** | **When it happens** | **Example response** |
| --- | --- | --- | --- |
| 400 | Bad Request | The body is empty or is not valid JSON. | { "error": "Invalid JSON" } |
| --- | --- | --- | --- |
| 401 | Unauthorized | Credentials are missing or wrong. The response includes a WWW-Authenticate: Basic header. | No body |
| --- | --- | --- | --- |
| 404 | Not Found | The URL is not exactly /transactions (for example, a typo, or /transactions/5). | No body |
| --- | --- | --- | --- |

## 3.6 Notes

• The new id is the current number of records + 1. Any id sent in the body is overwritten.

• Transactions are kept in memory only. They are not written back to sms_records.json, so they disappear when the server restarts.

# 4\. PUT /transactions/{id}

| **Documented by** | _Josue Rene Nsengiyumva_ |
| --- | --- |
| **Date** | _29<sup>th</sup> September 2026_ |
| --- | --- |

## 4.1 Endpoint & Method

| **Method** | PUT |
| --- | --- |
| **URL** | /transactions/{id} |
| --- | --- |
| **Description** | Updates an existing SMS transaction. The fields sent in the JSON body are merged into the stored record, and the full updated record is returned. |
| --- | --- |
| **Authentication** | Required. HTTP Basic Auth: send an Authorization header with base64(username:password). Requests without valid credentials receive 401. |
| --- | --- |

## 4.2 Request Parameters

| **Name** | **Location** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| id  | Path | integer | Yes | ID of the transaction to update, for example /transactions/1. Must be a whole number. |
| --- | --- | --- | --- | --- |
| Authorization | Header | string | Yes | Basic &lt;base64(username:password)&gt; |
| --- | --- | --- | --- | --- |
| Content-Type | Header | string | Recommended | application/json. Not enforced, but the body is always parsed as JSON. |
| --- | --- | --- | --- | --- |
| Content-Length | Header | integer | Yes | Size of the body in bytes. Added automatically by curl and Postman. If missing, the body is empty and the request fails with 400. |
| --- | --- | --- | --- | --- |
| (fields to update) | Body | JSON object | Yes | Only the fields you send are changed. Fields you leave out keep their current values. Fields are not validated. |
| --- | --- | --- | --- | --- |
| id  | Body | integer | No  | Ignored. The id always stays the one in the URL. |
| --- | --- | --- | --- | --- |

## 4.3 Request Example

curl -X PUT http://localhost:8000/transactions/1 \\

\-u username:password \\

\-H "Content-Type: application/json" \\

\-d '{"amount": 7500}'

## 4.4 Response Example

_Show a real successful response: status code, then the body._

**Success – 200 OK**

{

"type": "received",

"amount": 7500,

"sender": "Jane Doe",

"date": "2026-09-01 10:30:00",

"id": 1

}

## 4.5 Error Codes

| **Status code** | **Meaning** | **When it happens** | **Example response** |
| --- | --- | --- | --- |
| 400 | Bad Request | The body is empty or is not valid JSON. | { "error": "Invalid JSON" } |
| --- | --- | --- | --- |
| 401 | Unauthorized | Credentials are missing or wrong. The response includes a WWW-Authenticate: Basic header. | No body |
| --- | --- | --- | --- |
| 404 | Not Found | No transaction exists with the given id. | { "error": "Transaction not found" } |
| --- | --- | --- | --- |
| 404 | Not Found | The URL does not start with /transactions/ (for example PUT /transactions with no id). | No body |
| --- | --- | --- | --- |

## 4.6 Notes

• This is a partial update: the body is merged into the existing record. Fields you do not send are kept, and new fields are added.

• The id cannot be changed. Any id in the body is overwritten with the id from the URL.

# 5\. DELETE /transactions/{id}

| **Documented by** | _Josue Rene Nsengiyumva_ |
| --- | --- |
| **Date** | _29<sup>th</sup> September 2026_ |
| --- | --- |

## 5.1 Endpoint & Method

| **Method** | DELETE |
| --- | --- |
| **URL** | /transactions/{id} |
| --- | --- |
| **Description** | Deletes one SMS transaction by its id. On success, it returns the deleted record along with a confirmation message. |
| --- | --- |
| **Authentication** | Required. HTTP Basic Auth: send an Authorization header with base64(username:password). Requests without valid credentials receive 401 |
| --- | --- |

## 5.2 Request Parameters

| **Name** | **Location** | **Type** | **Required** | **Description** |
| --- | --- | --- | --- | --- |
| id  | Path | integer | Yes | ID of the transaction to delete, for example /transactions/1. Must be a whole number. |
| --- | --- | --- | --- | --- |
| Authorization | Header | string | Yes | _Basic &lt;base64(username:password)&gt;_ |
| --- | --- | --- | --- | --- |
| (body) | Body | none | No  | _This endpoint takes no request body._ |
| --- | --- | --- | --- | --- |

## 5.3 Request Example

curl -X DELETE http://localhost:8000/transactions/1 \\

\-u username:password

## 5.4 Response Example

_Show a real successful response: status code, then the body._

**Success – 200 OK**

{

"message": "Transaction deleted successfully",

"transaction": {

"type": "received",

"amount": 5000,

"sender": "Jane Doe",

"date": "2026-09-01 10:30:00",

"id": 1

}

}

## 5.5 Error Codes

| **Status code** | **Meaning** | **When it happens** | **Example response** |
| --- | --- | --- | --- |
| 400 | Bad Request | The last part of the URL is not a whole number (for example /transactions/abc, or /transactions with no id). | { "error": "Invalid transaction ID" } |
| --- | --- | --- | --- |
| 401 | Unauthorized | Credentials are missing or wrong. The response includes a WWW-Authenticate: Basic header. | { "error": "Authentication required" } |
| --- | --- | --- | --- |
| 404 | Not Found | No transaction exists with the given id, for example because it was already deleted. | { "error": "Transaction not found" } |
| --- | --- | --- | --- |
| 400 | Bad Request | The last part of the URL is not a whole number (for example /transactions/abc, or /transactions with no id). | { "error": "Invalid transaction ID" } |
| --- | --- | --- | --- |

## 5.6 Notes

• Success returns 200 with the deleted record in the body, not 204 No Content.

• The deletion is kept in memory only. sms_records.json is not changed, so the record comes back when the server restarts.

• Other ids are not renumbered, so deleting a record leaves a gap. Sending the same DELETE a second time returns 404.