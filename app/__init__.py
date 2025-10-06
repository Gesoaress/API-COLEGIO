from flask import Flask
from flasgger import Swagger, LazyJSONEncoder
from .extensions import db


def create_app():
    app = Flask(__name__)

    # --- Configurações do banco ---
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.json_encoder = LazyJSONEncoder

    # --- Configuração do Swagger ---
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API Colégio",
            "description": "Documentação da API do Sistema Escolar (Professores, Turmas e Alunos)",
            "version": "1.0.0"
        },
        "basePath": "/",
        "schemes": ["http"],
    }

    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec_1",
                "route": "/apispec_1.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/apidocs/",
        "parse": True,           # ativa o parser YAML
        "enable_validate": True  # força validação e exibição dos schemas
    }

    # --- Inicializa o banco ---
    db.init_app(app)

    # --- Cria o Swagger (depois de init_app) ---
    Swagger(app, template=swagger_template, config=swagger_config)

    # --- Importa e registra os blueprints ---
    from .controllers.health import bp as health_bp
    from .controllers.professores import bp as professores_bp
    from .controllers.turmas import bp as turmas_bp
    from .controllers.alunos import bp as alunos_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(professores_bp)
    app.register_blueprint(turmas_bp)
    app.register_blueprint(alunos_bp)

    return app
