from flask import Flask, jsonify
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    @app.route('/health')
    def health_check():
        return jsonify({"status": "healthy"})


    from routes.products import bp as products_bp
    from routes.auth import bp as auth_bp
    from routes.cart import bp as cart_bp

    app.register_blueprint(products_bp, url_prefix='/api/products')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(cart_bp, url_prefix='/api/cart')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
