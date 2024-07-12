# JSON Web Token

## Installation and requirements
Requires:
- Python 3

### How to install
```
cd CyberSecurity/JWT
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python server.py
```

These commands will create a Python virtual environment, install the project's dependencies, and launch the website on localhost:8000

To test the application and JWTs:

Navigate to the home page
- http://localhost:8000/

Acquire a JWT token as a cookie for normal user permissions
- http://localhost:8000/login?user=any_username

Try to visit the page that requires admin permissions
- http://localhost:8000/secretpage

Try to change permission to admin (user=admin)
- http://localhost:8000/login?user=admin

Try again
- http://localhost:8000/secretpage

During the experiment, there will be some text that will help you to identify if everything goes as planned.


