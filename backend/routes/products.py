from flask import Blueprint, jsonify

bp = Blueprint('products', __name__)

@bp.route('/', methods=['GET'])
def get_products():
    return jsonify({"products": []})
