## 🌐 Postman API Test Suite

This repository showcases API testing using Postman for demo endpoints from `reqres.in`.

### ✅ Included Tests:
- **GET /users?page=2**
  - Status code validation
  - Pagination check (`page = 2`)
  - User count verification (`data.length = 6`)
  - First user's email match

- **POST /users**
  - Status code `201` check
  - Response body contains `id` and `createdAt`

### 📂 Files:
- `API-Test-Suite/amrit_api_collection.json` – Exported Postman collection
- `screenshots/` – Visual proof of passing test results

### 🛠 Tools Used:
- Postman
- JavaScript (Tests tab)
- Git & GitHub for version control

> This suite demonstrates real-world API validation logic and is part of Amrit's QA automation portfolio.
