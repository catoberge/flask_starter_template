from app import app


# Decorators - a decorator modifies the function that follows it
@app.route("/")
@app.route("/index")
def index():
    return "Hei på deg!"
