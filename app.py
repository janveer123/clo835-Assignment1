from flask import Flask
import os

app = Flask(__name__)

# Read BACKGROUND color from environment variable (default = white)
COLOR = os.environ.get("BACKGROUND", "white")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Color App</title>
</head>
<body style="background-color: {color}; text-align: center; padding-top: 50px;">
    <h1 style="color: white;">This is the {color} container!</h1>
</body>
</html>
"""

@app.route("/")
def index():
    return HTML_TEMPLATE.format(color=COLOR)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)