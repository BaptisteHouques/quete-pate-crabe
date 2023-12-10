from flask import Flask, render_template, request, redirect, session
import random
from data import ennemies, characters

app = Flask(__name__)
app.secret_key = "your_secret_key"

def FncAttack(ennemie, character):
    str_character = characters[character]['str']
    ennemies[ennemie]['hp'] -= str_character
    ennemies[ennemie]['hp'] = max(0, ennemies[ennemie]['hp']) # Evite la condition if

    message_ennemie = FncActionEnnemie(ennemie, character) if ennemies[ennemie]['hp'] > 0 else ''
    return f"Vous avez infligé {str_character} points de dégâts à {ennemie}. {message_ennemie}"

def FncDodge():
    return random.choice([True, False]) # Evite la condition if

def FncActionEnnemie(ennemie, character):
    action = random.choice(['Attack', 'Dodge'])

    if action == 'Attack':
        attack_ennemie = random.randint(10, 30)
        characters[character]['hp'] -= attack_ennemie
        characters[character]['hp'] = max(0, characters[character]['hp']) # Evite la condition if
        return f"{ennemie} vous a attaqué et vous a infligé {attack_ennemie} points de dégâts." if characters[character]['hp'] > 0 else "Vous êtes mort ..."

    elif action == 'Dodge':
        return f"{ennemie} a esquivé votre attaque." if FncDodge() else ''




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['character'] = request.form['character']
        return redirect('/fight')
    return render_template('index.html')


@app.route('/fight', methods=['GET', 'POST'])
def fight():
    if 'character' not in session:
        return redirect('/')

    character = session['character']
    if 'ennemie' not in session:
        session['ennemie'] = random.choice(list(ennemies.keys()))

    actual_ennemie = session['ennemie']
    message = ""

    if request.method == 'POST':
        action = request.form['action']

        if action == 'attack':
            message = FncAttack(actual_ennemie, character)
            if ennemies[actual_ennemie]['hp'] <= 0:
                del ennemies[actual_ennemie]
                session.pop('ennemie', None) # Ajoute un défaut pour éviter KeyError

                if not ennemies:
                    return "Félicitations ! Vous avez vaincu tous les adversaires."
                else:
                    return render_template('combatGagne.html', actual_ennemie=actual_ennemie)

        elif action == 'dodge':
            message = "Vous avez esquivé l'attaque!" if FncDodge() else FncActionEnnemie(actual_ennemie, character)

            if characters[character]['hp'] <= 0:
                return "Vous êtes mort ..."

    return render_template('combat.html', character=character, ennemie=actual_ennemie, ennemies=ennemies, characters=characters, message=message)


if __name__ == '__main__':
    app.run(debug=True) # Ajout d'un mode de débogage
