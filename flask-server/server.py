from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permettre les requêtes CORS pour l'application React
mysql = MySQL()

# Configuration de la base de données
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskreact1_db'
app.config['SECRET_KEY'] = 'fjdkslkdjf qsmeizeoiuez qaputqsmapht sapzeirusksjf'

mysql.init_app(app)

@app.route('/api/sign-up', methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        data = request.get_json()  # Récupérer les données du corps de la requête
        email = data.get('email')
        password1 = data.get('password1')
        password2 = data.get('password2')

        if not email or len(email) < 5:
            return jsonify({'message': 'Email should be greater than 4 characters'}), 400
        elif len(password1) < 7:
            return jsonify({'message': 'Password should be greater than 7 characters'}), 400
        elif password1 != password2:
            return jsonify({'message': 'Passwords don\'t match'}), 400

        cur = mysql.connection.cursor()
        try:
            # Vérifier si l'email existe déjà
            cur.execute("SELECT * FROM users WHERE email = %s", (email,))
            existing_user = cur.fetchone()

            if existing_user:
                return jsonify({'message': 'Email already exists'}), 400

            # Insérer le nouvel utilisateur
            cur.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password1))
            mysql.connection.commit()
            return jsonify({'message': 'Account created!'}), 201
        except Exception as e:
            return jsonify({'message': str(e)}), 500
        finally:
            cur.close()

    # Pour les requêtes GET, vous pouvez retourner le formulaire d'inscription
    return jsonify({'message': 'GET request received. Use POST to sign up.'}), 200



@app.route('/')
def api():
    return "Server is running ..."

if __name__ == '__main__':
    app.run(debug=True)
