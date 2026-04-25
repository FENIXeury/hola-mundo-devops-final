from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Proyecto DevOps</title>

        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0f172a, #1e40af);
                color: white;
            }

            .card {
                text-align: center;
                padding: 40px;
                border-radius: 20px;
                background: rgba(255, 255, 255, 0.12);
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            }

            h1 {
                font-size: 45px;
                margin-bottom: 10px;
            }

            p {
                font-size: 20px;
                color: #dbeafe;
            }

            .badge {
                margin-top: 20px;
                display: inline-block;
                padding: 10px 20px;
                border-radius: 30px;
                background: #22c55e;
                color: #052e16;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>🚀 Hola Mundo DevOps CI/CD</h1>
            <p>Aplicación web desplegada con GitHub Actions, Docker Hub y Render</p>
            <div class="badge">Proyecto Final DevOps</div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
