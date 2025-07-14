from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def get_characters():
    characters = []
    page = 1
    while True:
        response = requests.get(f"https://rickandmortyapi.com/api/character?page={page}")
        data = response.json()
        for character in data['results']:
            if (
                character['species'] == 'Human' and
                character['status'] == 'Alive' and
                'Earth' in character['origin']['name']
            ):
                characters.append({
                    'Name': character['name'],
                    'Location': character['location']['name'],
                    'Image': character['image']
                })
        if not data['info']['next']:
            break
        page += 1
    return characters

@app.route('/rickmorty/') # This route is correct
def home():
    return """
    <html>
    <head>
        <title>Rick and Morty API</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background: #f9f9f9; }
            button {
                padding: 15px 25px;
                font-size: 18px;
                margin: 10px;
                cursor: pointer;
                border-radius: 5px;
                border: none;
                background-color: #007BFF;
                color: white;
                transition: background-color 0.3s ease;
            }
            button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to the Rick and Morty API Service</h1>
        <!-- FIX: Update internal links to include /rickmorty/ prefix -->
        <button onclick="window.location.href='/rickmorty/characters'">View Characters</button>
        <button onclick="window.location.href='/rickmorty/healthcheck'">Health Check</button>
    </body>
    </html>
    """

@app.route('/rickmorty/characters') # This route is correct
def characters_endpoint():
    characters = get_characters()

    html = """
    <html>
    <head>
        <title>Rick and Morty Characters</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; background: #f9f9f9; }
            h1 { text-align: center; }
            .container { display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; }
            .card {
                background: white;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                width: 220px;
                padding: 15px;
                text-align: center;
                transition: transform 0.2s;
            }
            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 8px 15px rgba(0,0,0,0.2);
            }
            .card img {
                width: 150px;
                border-radius: 8px;
                margin-bottom: 10px;
            }
            .card h3 {
                margin: 10px 0 5px;
                font-size: 20px;
                color: #333;
            }
            .card p {
                margin: 5px 0;
                color: #555;
                font-size: 16px;
            }
            .back-btn {
                display: block;
                margin: 30px auto;
                padding: 12px 25px;
                font-size: 16px;
                border: none;
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                width: 180px;
                text-align: center;
                transition: background-color 0.3s ease;
            }
            .back-btn:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h1>Alive Human Characters from Earth</h1>
        <div class="container">
    """

    for c in characters:
        html += f"""
        <div class="card">
            <img src="{c['Image']}" alt="Image of {c['Name']}">
            <h3>{c['Name']}</h3>
            <p>Location: {c['Location']}</p>
        </div>
        """

    html += """
        </div>
        <!-- FIX: Update internal link to include /rickmorty/ prefix -->
        <a href="/rickmorty/" class="back-btn">Back to Home</a>
    </body>
    </html>
    """
    return html

@app.route('/rickmorty/healthcheck') # This route is correct
def healthcheck():
    return """
    <html>
      <body style="font-family: Arial, sans-serif; text-align:center; margin-top:50px; background:#f9f9f9;">
        <h2>Health Check Status</h2>
        <p>Status: <strong>OK</strong></p>
        <!-- FIX: Update internal link to include /rickmorty/ prefix -->
        <button onclick="location.href='/rickmorty/'" style="padding:12px 25px; font-size:16px; border:none; border-radius:5px; background:#007BFF; color:#fff; cursor:pointer;">Back to Home</button>
      </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


