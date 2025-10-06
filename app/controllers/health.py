from flask import Blueprint, jsonify

bp = Blueprint("health", __name__)

@bp.get("/health")
def health_check():
    """
    Health Check
    ---
    tags:
      - Sistema
    responses:
      200:
        description: Retorna o status do servidor
        examples:
          application/json: {"status": "ok"}
    """
    return jsonify(status="ok")
