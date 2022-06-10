 ----------------------------------------- Initial Set Up Instructions -----------------------------------------
### 1 .Clone the git repo and create an environment 
                    
**Windows**
          
```bash
git clone https://github.com/Dev-Elie/Flask-API-boilerplate.git Flask-API
cd Flask-API
py -3 -m venv venv
```
          
**macOS/Linux**
          
```bash
git clone https://github.com/Dev-Elie/Flask-API-boilerplate.git Flask-API
cd Flask-API
python3 -m venv venv
```

### 2 .Activate the environment
          
**Windows** 

```venv\Scripts\activate```
          
**macOS/Linux**

```. venv/bin/activate```
or
```source venv/bin/activate```

### 3 .Install the requirements

Applies for windows/macOS/Linux

```pip install -r requirements.txt```


### 4. Run the application 


`python wsgi.py`

### 5. Running tests

`pytest -v`
