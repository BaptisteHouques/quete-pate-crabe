from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"

characters = {
    'boxeur': {'vie': 100, 'force': 30},
    'voleur': {'vie': 80, 'force': 40},
    'gros': {'vie': 120, 'force': 20}
}

adversaires = {
    'Sally': {'vie': 100},
    'Patric': {'vie': 120},
    'Carlos': {'vie': 80}
}

def attaquer(adversaire, personnage):
    force_personnage = characters[personnage]['force']
    adversaires[adversaire]['vie'] -= force_personnage
    adversaires[adversaire]['vie'] = max(0, adversaires[adversaire]['vie']) # Evite la condition if

    message_adversaire = action_adversaire(adversaire, personnage) if adversaires[adversaire]['vie'] > 0 else ''
    return f"Vous avez infligé {force_personnage} points de dégâts à {adversaire}. {message_adversaire}"

def esquiver():
    return random.choice([True, False]) # Evite la condition if

def action_adversaire(adversaire, personnage):
    action = random.choice(['attaquer', 'esquiver'])

    if action == 'attaquer':
        attaque_adversaire = random.randint(10, 30)
        characters[personnage]['vie'] -= attaque_adversaire
        characters[personnage]['vie'] = max(0, characters[personnage]['vie']) # Evite la condition if
        return f"{adversaire} vous a attaqué et vous a infligé {attaque_adversaire} points de dégâts." if characters[personnage]['vie'] > 0 else "Vous êtes mort ..."

    elif action == 'esquiver':
        return f"{adversaire} a esquivé votre attaque." if esquiver() else ''

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['personnage'] = request.form['personnage']
        return redirect('/combat')
    return render_template('index.html')

@app.route('/combat', methods=['GET', 'POST'])
def combat():
    if 'personnage' not in session:
        return redirect('/')

    personnage = session['personnage']
    if 'adversaire' not in session:
        session['adversaire'] = random.choice(list(adversaires.keys()))

    adversaire_actuel = session['adversaire']
    message = ""

    if request.method == 'POST':
        action = request.form['action']

        if action == 'attaquer':
            message = attaquer(adversaire_actuel, personnage)
            if adversaires[adversaire_actuel]['vie'] <= 0:
                del adversaires[adversaire_actuel]
                session.pop('adversaire', None) # Ajoute un défaut pour éviter KeyError

                if not adversaires:
                    return "Félicitations ! Vous avez vaincu tous les adversaires."
                else:
                    return f"Vous avez vaincu {adversaire_actuel} ! Choisissez un nouvel adversaire."

        elif action == 'esquiver':
            message = "Vous avez esquivé l'attaque!" if esquiver() else action_adversaire(adversaire_actuel, personnage)

            if characters[personnage]['vie'] <= 0:
                return "Vous êtes mort ..."

    return render_template('combat.html', personnage=personnage, adversaire=adversaire_actuel, adversaires=adversaires, characters=characters, message=message)

if __name__ == '__main__':
    app.run(debug=True) # Ajout d'un mode de débogage
