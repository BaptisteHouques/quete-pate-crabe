# game/controllers/character_controller.py
from flask import Blueprint, render_template, request
from models import Character

character_controller = Blueprint('character_controller', __name__)

@character_controller.route('/choose_character', methods=['POST'])
def choose_character():
    character_name = request.form.get('character_name')
    character = Character.get_by_name(character_name)
    return render_template('character.html', character=character)
