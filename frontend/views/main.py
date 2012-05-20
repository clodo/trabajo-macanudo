from flask import Blueprint, render_template

mod = Blueprint('main', __name__)

@mod.route('/')
def home():
  return render_template('main/home.html')