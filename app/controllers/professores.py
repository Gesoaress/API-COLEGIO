import os
from flasgger import swag_from
from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Professor


bp = Blueprint("professores", __name__, url_prefix="/professores")
DOCS_DIR = os.path.join(os.path.dirname(__file__), "../docs")



# --- Criar professor ---
@bp.post("/")
@swag_from(os.path.join(DOCS_DIR, "professores_post.yml"))
def criar_professor():
    dados = request.get_json()

    novo = Professor(
        nome=dados["nome"],
        email=dados["email"],
        idade=dados.get("idade"),
        materia=dados.get("materia"),
        observacoes=dados.get("observacoes")
    )

    db.session.add(novo)
    db.session.commit()

    return jsonify(message="Professor criado com sucesso!", id=novo.id), 201


# --- Listar professores ---
@bp.get("/")
@swag_from(os.path.join(DOCS_DIR, "professores_get.yml"))
def listar_professores():
    """
    Listar todos os professores
    ---
    tags:
      - Professores
    responses:
      200:
        description: Retorna todos os professores cadastrados
    """
    professores = Professor.query.all()
    lista = [
        {
            "id": p.id,
            "nome": p.nome,
            "email": p.email,
            "idade": p.idade,
            "materia": p.materia,
            "observacoes": p.observacoes
        }
        for p in professores
    ]
    return jsonify(lista), 200


# --- Buscar professor por ID ---
@bp.get("/<int:id>")
@swag_from(os.path.join(DOCS_DIR, "professores_get_id.yml"))
def obter_professor(id):
    """
    Buscar professor pelo ID
    ---
    tags:
      - Professores
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do professor
        example: 1
    responses:
      200:
        description: Retorna os dados do professor
      404:
        description: Professor não encontrado
    """
    professor = Professor.query.get(id)
    if not professor:
        return jsonify(message="Professor não encontrado!"), 404

    return jsonify(
        id=professor.id,
        nome=professor.nome,
        email=professor.email,
        idade=professor.idade,
        materia=professor.materia,
        observacoes=professor.observacoes
    ), 200


# --- Atualizar professor ---
@bp.put("/<int:id>")
@swag_from(os.path.join(DOCS_DIR, "professores_put.yml"))
def atualizar_professor(id):
    """
    Atualizar dados de um professor
    ---
    tags:
      - Professores
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID do professor
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nome:
                type: string
              email:
                type: string
              idade:
                type: integer
              materia:
                type: string
              observacoes:
                type: string
    responses:
      200:
        description: Professor atualizado com sucesso
      404:
        description: Professor não encontrado
    """
    professor = Professor.query.get(id)
    if not professor:
        return jsonify(message="Professor não encontrado!"), 404

    dados = request.get_json()
    professor.nome = dados.get("nome", professor.nome)
    professor.email = dados.get("email", professor.email)
    professor.idade = dados.get("idade", professor.idade)
    professor.materia = dados.get("materia", professor.materia)
    professor.observacoes = dados.get("observacoes", professor.observacoes)

    db.session.commit()
    return jsonify(message="Professor atualizado com sucesso!"), 200


# --- Deletar professor ---
@bp.delete("/<int:id>")
@swag_from(os.path.join(DOCS_DIR, "professores_delete.yml"))
def deletar_professor(id):
    """
    Excluir professor
    ---
    tags:
      - Professores
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Professor removido com sucesso
      404:
        description: Professor não encontrado
    """
    professor = Professor.query.get(id)
    if not professor:
        return jsonify(message="Professor não encontrado!"), 404

    db.session.delete(professor)
    db.session.commit()
    return jsonify(message="Professor deletado com sucesso!"), 200
