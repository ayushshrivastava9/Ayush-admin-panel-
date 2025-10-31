from flask import Flask, render_template_string

# Flask application object banaya
app = Flask(__name__)

# --- HTML Content (Jo web page par dikhega) ---
# Ismein saara HTML aur CSS shamil hai
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ROBIN WEB - ALL OPTION</title>
    <style>
        /* CSS styling for the dark theme and neon glow */
        body {
            background-color: #000;
            color: #fff;
            font-family: 'Consolas', 'Courier New', monospace;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            min-height: 100vh;
        }

        .container {
            width: 90%;
            max-width: 420px;
            padding: 20px 0;
            box-sizing: border-box;
            text-align: center;
        }

        .header {
            margin-bottom: 30px;
        }
        .title {
            color: #ffb6c1;
            font-size: 28px;
            margin-bottom: 0px;
            text-shadow: 0 0 10px #ff69b4, 0 0 20px #ff69b4; /* Pink Neon Glow */
        }
        .subtitle {
            color: #fff;
            font-size: 18px;
            margin-top: 0px;
            font-weight: normal;
        }

        .option-button {
            display: block;
            width: 100%;
            padding: 15px 10px;
            margin-bottom: 15px;
            background-color: #00ffff; /* Bright Cyan */
            color: #000;
            text-decoration: none;
            border: none;
            border-radius: 8px;
            font-size: 14px;
            font-weight: bold;
            text-transform: uppercase;
            box-shadow: 0 0 15px #00ffff, 0 0 30px #00ffff; /* Strong Cyan Neon Glow */
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            letter-spacing: 1px;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .option-button:hover {
            background-color: #00eeee;
            box-shadow: 0 0 20px #00eeee, 0 0 40px #00eeee;
            transform: translateY(-2px);
        }

        .footer {
            color: #444;
            font-size: 10px;
            margin-top: 30px;
            padding-bottom: 10px;
        }
    </style>
</head>
<body>

    <div class="container">
        <header class="header">
            <h1 class="title">💖 ROBIN WEB 💖</h1>
            <h2 class="subtitle">(ALL OPTION)</h2>
        </header>

        <div class="options-list">
            <a href="/convo-server" class="option-button"><- 1 - CONVO SERVER -></a>
            <a href="/backup-convo" class="option-button"><- 2 - BACKUP CONVO -></a>
            <a href="/post-server" class="option-button"><- 3 - POST SERVER -></a>
            <a href="/backup-post" class="option-button"><- 4 - BACKUP POST SERVER -></a>
            <a href="/token-check" class="option-button"><- 5 - TOKENS CHECK VALIDITY -></a>
            <a href="/fetch-uid" class="option-button"><- 6 - FETCH ALL UID WITH TOKEN -></a>
            <a href="/fetch-page-tokens" class="option-button"><- 7 - FETCH PAGE TOKENS -></a>
            <a href="/group-locker" class="option-button"><- 8 - GROUP NAME LOCKER -></a>
            <a href="/youtube-dl" class="option-button"><- 9 - YOUTUBE DOWNLOADER -></a>
            <a href="/instagram-dl" class="option-button"><- 10 - INSTAGRAM DOWNLOADER -></a>
            <a href="/facebook-dl" class="option-button"><- 11 - FACEBOOK DOWNLOADER -></a>
            <a href="/cookie-to-json" class="option-button"><- 12 - COOKIE TO JSON -></a>
        </div>

        <footer class="footer">
            © 2022 MADE BY :- LEGEND ROBIN
        </footer>
    </div>

</body>
</html>
"""
# --- End of HTML Content ---

# Root URL ('/') par HTML_CONTENT load karega
@app.route('/')
def home():
    """Main page load karega."""
    return render_template_string(HTML_CONTENT)

# Ek example route (jaise ki button 1 click karne par)
@app.route('/convo-server')
def convo_server():
    """Button click hone par Python ka logic yahan chalta."""
    # Agar aapko CONVO SERVER ka koi kaam karna hai (jaise koi API call, ya file process), 
    # toh woh code is function ke andar aayega.
    return "<h1>CONVO SERVER Activated!</h1><p>Ab aap yahan apna zaroori Python code chala sakte hain.</p>"

# Aap is tarah har button ke liye naye @app.route functions bana sakte hain.
# Example: @app.route('/youtube-dl')

# Application ko run karne ke liye
if __name__ == '__main__':
    # Debug mode ON hai aur port 5000 par run hoga (0.0.0.0 for deployment)
    app.run(debug=True, host='0.0.0.0', port=5000)