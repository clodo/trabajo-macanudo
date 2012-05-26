# -*- coding: utf-8 -*-

from flask import Blueprint, jsonify, request
from frontend.models import Tag
from frontend.extensions import db

mod = Blueprint('ajax', __name__, url_prefix='/ajax')

@mod.route('/tags')
def tags():
  term = request.args.get('term', '')

  if term == '':
    return '[]'

  tags = Tag.query.filter(Tag.name.like(term+'%')).all()

  #return jsonify(tags=[tag.name for tag in tags])
  return '[' + ",".join('"'+tag.name+'"' for tag in tags) + ']'