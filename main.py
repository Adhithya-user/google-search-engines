from flask import Flask, render_template_string, request, redirect, url_for, session
import os
import random

app = Flask(__name__)
app.secret_key = "cloud_computing_2026_secret"

# ---------------- SETTINGS ---------------- #

CLOUD_FACTS = [
    "90% of the world's data was generated in the last 2 years thanks to Cloud scalability.",
    "Cloud computing is estimated to be 40% more cost-effective for small businesses.",
    "The 'Cloud' is actually composed of millions of miles of undersea fiber optic cables.",
    "By 2026, it is predicted that 95% of digital workloads will be deployed on cloud-native platforms.",
    "The first concept of cloud computing dates back to the 1960s with J.C.R. Licklider's Intergalactic Computer Network."
]

# ✅ THIS WAS MISSING
BACKGROUND_IMAGE = "https://images.unsplash.com/photo-1451187580459-43490279c0fa"

# ---------------- HTML TEMPLATES ---------------- #

LOGIN_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud Access Login</title>
    <style>
        body {
            margin: 0; font-family: 'Segoe UI', sans-serif;
            background: url('{{ bg }}') no-repeat center center fixed;
            background-size: cover;
            height: 100vh; display: flex; align-items: center; justify-content: center;
        }
        .login-card {
            background: rgba(0, 15, 40, 0.9); padding: 40px;
            border-radius: 15px; text-align: center; color: white; width: 320px;
        }
        input {
            width: 90%; padding: 12px; margin: 10px 0;
            border-radius: 5px; border: none;
        }
        .btn {
            background: #00d2ff; color: #001528;
            padding: 12px; border: none;
            border-radius: 25px; cursor: pointer; width: 100%;
        }
        .error { color: #ff4d4d; }
    </style>
</head>
<body>
    <div class="login-card">
        <h2>Cloud Login</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username (admin)" required>
            <input type="password" name="password" placeholder="Password (cloud123)" required>
            <button type="submit" class="btn">Login</button>
        </form>
        {% if error %}<p class="error">{{ error }}</p>{% endif %}
    </div>
</body>
</html>
"""

PORTAL_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud Portal</title>
</head>
<body style="margin:0; font-family:Segoe UI; background:url('{{ bg }}') no-repeat center center fixed; background-size:cover; color:white; text-align:center; padding:50px;">
    <h1>Cloud Computing Portal</h1>
    <p>Your session is secure.</p>

    <h3>Cloud Fact:</h3>
    <p>{{ fact }}</p>

    <br>
    <a href="{{ url_for('portal') }}">Generate New Fact</a> |
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
"""

# ---------------- ROUTES ---------------- #

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'cloud123':
            session['logged_in'] = True
            return redirect(url_for('portal'))
        else:
            error = "Invalid Username or Password!"
    return render_template_string(LOGIN_TEMPLATE, bg=BACKGROUND_IMAGE, error=error)

@app.route('/portal')
def portal():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template_string(PORTAL_TEMPLATE, bg=BACKGROUND_IMAGE, fact=random.choice(CLOUD_FACTS))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
