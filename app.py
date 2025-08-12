from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, BIS209!</h1><p>Welcome to your Azure test app.</p>"

@app.route("/echo", methods=["GET", "POST"])
def echo():
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        # This is intentionally insecure for testing (no sanitisation)
        return render_template_string("<h2>You said: {{ user_input }}</h2>", user_input=user_input)
    return '''
        <form method="post">
            Say something: <input type="text" name="user_input">
            <input type="submit" value="Echo">
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

