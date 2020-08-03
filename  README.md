#### Get access token:


http://localhost:8000/api/token/

`{"username": "admin", "password": "admin"}`

header: Authorization prefix: Bearer 

#### URLs:

create request: POST http://localhost:8000/api/v1/request

`{"description": "string"}`

get request: GET http://localhost:8000/api/v1/request/{uuid}

change of request: PUT http://localhost:8000/api/v1/request/{uuid}

`{"status": "string"}`

create offer: POST http://localhost:8000/api/v1/offer

`{"request": "string", "description": "string", "price": "string"}`