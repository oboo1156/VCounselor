# How to  access the website on your local machine using terminal:

**Creating and activating virtual environment:**
1. `python -m venv venv`
2. `venv\Scripts\activate` (on Windows) | `source/venv/bin/activate` (on Mac)

**Creating a place to save installed packages. Also installing the packages:**
3. `pip freeze > requirements.txt`
4. `pip install -r requirements.txt`

**Accessing the website on your local machine:**
5. `python manage.py runserver`
Then you click on the link that follows ie [localhost](http://127.0.0.1:8000/)


---

## nb: this project has the libraries and requirements already installed on the virtual environment(venv) -
## so just activate it(step 2). Then go ahead and access the website following step5.**