from flask import Flask, render_template_string
import os

# Flask Application Setup
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Set a secret key for session management

# Route: Main Index
@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Flipit Chicago</title>
            <style>
                body {
                    font-family: 'Helvetica', sans-serif;
                    color: black;
                    background-color: white;
                    text-align: center;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                h1 {
                    font-size: 4em;
                    margin-bottom: 0.5em;
                }
                p {
                    font-size: 1.5em;
                }
                @media only screen and (max-width: 600px) {
                    h1 {
                        font-size: 2.5em;
                    }
                    p {
                        font-size: 1em;
                    }
                }
            </style>
        </head>
        <body>
            <div>
                <h1>FLIPITCHICAGO</h1>
                <p>WHOLESALE AND PRODUCT DEVELOPMENT</p>
                <p>CONTACT FOR INQUIRIES:</p>
                <p>LUKE.KENSIK@GMAIL.COM</p>
            </div>
        </body>
        </html>
        ''')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
