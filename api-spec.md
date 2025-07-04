# API 명세서 (v1)

## 인증 API

### 회원가입
- Endpoint: POST /api/v1/auth/register
- Request Body:
  ```json
  {
    "email": "string",
    "password": "string",
    "name": "string"
  }
  ```
- Response: 201 Created
  ```json
  {
    "id": "number",
    "email": "string",
    "name": "string",
    "created_at": "datetime"
  }
  ```

### 로그인
- Endpoint: POST /api/v1/auth/login
- Request Body:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- Response: 200 OK
  ```json
  {
    "access_token": "string",
    "token_type": "Bearer"
  }
  ```

## 자산 관리 API

### 자산 업로드
- Endpoint: POST /api/v1/assets
- Header: Authorization: Bearer {token}
- Request Body (multipart/form-data):
  ```json
  {
    "file": "binary",
    "name": "string",
    "description": "string",
    "tags": ["string"],
    "folder_id": "number (optional)"
  }
  ```
- Response: 201 Created
  ```json
  {
    "id": "number",
    "name": "string",
    "description": "string",
    "folder_id": "number",
    "mime_type": "string",
    "size": "number",
    "file_url": "string",
    "created_at": "datetime",
    "updated_at": "datetime",
    "tags": [
      {
        "id": "number",
        "name": "string",
        "created_at": "datetime"
      }
    ]
  }
  ```

### 자산 목록 조회
- Endpoint: GET /api/v1/assets
- Header: Authorization: Bearer {token}
- Query Parameters:
  - folder_id: number (optional)
  - tag: string (optional)
- Response: 200 OK
  ```json
  [
    {
      "id": "number",
      "name": "string",
      "description": "string",
      "folder_id": "number",
      "mime_type": "string",
      "size": "number",
      "file_url": "string",
      "created_at": "datetime",
      "updated_at": "datetime",
      "tags": [
        {
          "id": "number",
          "name": "string",
          "created_at": "datetime"
        }
      ]
    }
  ]
  ```

### 폴더 생성
- Endpoint: POST /api/v1/folders
- Header: Authorization: Bearer {token}
- Request Body:
  ```json
  {
    "name": "string",
    "parent_id": "number (optional)"
  }
  ```
- Response: 201 Created
  ```json
  {
    "id": "number",
    "name": "string",
    "parent_id": "number",
    "user_id": "number",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ``` 