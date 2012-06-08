# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from frontend.extensions import db

mod = Blueprint('feedback', __name__, url_prefix='/feedback')

@mod.route('/')
def home():
  return render_template('feedback/home.html')