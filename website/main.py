from website import create_app # website(name of folder) becomes a python package because we have __init__.py in that folder. That's why we can import the function create_app

app = create_app()

if __name__ == '__main__': # only run this file if we have it, NOT imported. You only want to run the web server if you have the '__main__' file.
    app.run(debug=True) # anytime we make change to our python code, it will rerun the web server. **Turn this off when running the app in production**
    