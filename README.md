Secure API Project (Flask)

## Overview
This project demonstrates how insecure API design can expose sensitive data, and how basic security measures can be implemented to mitigate these risks.
The project starts with a deliberately vulnerable API, then applies fixes such as authentication and password hashing.

This is an educational project that demonstrates why API security matters. Two versions of the same API:
Vulnerable → No authentication, exposed sensitive data
Secured → API key protection, environment variables, proper error handling
The result? Anyone with network access can steal your data in Version 1. Version 2 locks them out


## Technologies Used
- Python
- Flask
- PowerShell / cURL (for testing)
- Werkzeug (for password hashing)



Phase 1: Vulnerable API

Problem
The API exposed sensitive data through a public endpoint:


- No authentication required
- Anyone could access sensitive information

Example Attack
http://127.0.0.1:3000/data


Result: Sensitive data returned

Phase 2: Securing the API

API Key Authentication
- Stored API key in environment variable
- Required `X-API-Key` header for access

### Code Vulnerability
@app.route('/data')
def get_data():
    # NO AUTHENTICATION
    return jsonify(sensitive_data)  # names, emails, password hashes

### Vulnerability Fix
API_KEY = os.getenv("API_KEY", "mySecretKey")

def is_authorized():
    return request.headers.get("X-API-Key") == API_KEY

@app.route('/data')
def get_data():
    if not is_authorized():
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(sensitive_data)
