from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Turma, Professor
import os
from flasgger import swag_from


bp = Blueprint("turmas", __name__, url_prefix="/turmas")
DOCS_DIR = os.path.join(os.path.dirname(__file__), "../docs")



# --- Criar turma ---
@bp.post("/")
@swag_from(os.path.join(DOCS_DIR, "turmas_post.yml"))
def criar_turma():
    """
    Criar nova turma
    ---
    tags:
      - Turmas
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nome:
                type: string
                example: "Turma A"
              turno:
                type: string
                example: "Manhã"
              professor_id:
                type: integer
                example: 1
    responses:
      201:
        description: Turma criada com sucesso
        examples:
          application/json: {"message": "Turma criada com sucesso!", "id": 1}
      404:
        description: Professor não encontrado
    """
    dados = request.get_json()

    # verifica se o professor informado existe
    professor = Professor.query.get(dados.get("professor_id"))
    if not professor:
        return jsonify(message="Professor não encontrado!"), 404

    nova = Turma(
        nome=dados["nome"],
        turno=dados["turno"],
        professor_id=professor.id
    )

    db.session.add(nova)
    db.session.commit()

    return jsonify(message="Turma criada com sucesso!", id=nova.id), 201


# --- Listar todas as turmas ---
@bp.get("/")
@swag_from(os.path.join(DOCS_DIR, "turmas_get.yml"))
def listar_turmas():
    """
    Listar todas as turmas
    ---
    tags:
      - Turmas
    responses:
      200:
        description: Retorna todas as turmas com o nome do professor responsável
        examples:
          application/json:
            [
              {
                "id": 1,
                "nome": "Turma A",
                "turno": "Manhã",
                "professor": "Marina Souza"
              }
            ]
    """
    turmas = Turma.query.all()
    lista = [
        {
            "id": t.id,
            "nome": t.nome,
            "turno": t.turno,
            "professor": t.professor.nome
        }
        for t in turmas
    ]
    return jsonify(lista), 200


# --- Buscar turma por ID ---
@bp.get("/<int:id>")
@swag_from(os.path.join(DOCS_DIR, "turmas_get_id.yml"))
def obter_turma(id):
    """
    Buscar turma pelo ID
    ---
    tags:
      - Turmas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da turma
        example: 1
    responses:
      200:
        description: Retorna os dados da turma
        examples:
          application/json:
            {"id": 1, "nome": "Turma A", "turno": "Manhã", "professor": "Marina Souza"}
      404:
        description: Turma não encontrada
    """
    turma = Turma.query.get(id)
    if not turma:
        return jsonify(message="Turma não encontrada!"), 404

    return jsonify(
        id=turma.id,
        nome=turma.nome,
        turno=turma.turno,
        professor=turma.professor.nome
    ), 200


# --- Atualizar turma ---
@bp.put("/<int:id>")
@swag_from(os.path.join(DOCS_DIR, "turmas_put.yml"))
def atualizar_turma(id):
    """
    Atualizar turma existente
    ---
    tags:
      - Turmas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da turma
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              nome:
                type: string
                example: "Turma B"
              turno:
                type: string
                example: "Tarde"
              professor_id:
                type: integer
                example: 2
    responses:
      200:
        description: Turma atualizada com sucesso
      404:
        description: Turma ou professor não encontrados
    """
    turma = Turma.query.get(id)
    if not turma:
        return jsonify(message="Turma não encontrada!"), 404

    dados = request.get_json()
    turma.nome = dados.get("nome", turma.nome)
    turma.turno = dados.get("turno", turma.turno)

    if "professor_id" in dados:
        professor = Professor.query.get(dados["professor_id"])
        if not professor:
            return jsonify(message="Professor não encontrado!"), 404
        turma.professor_id = professor.id

    db.session.commit()
    return jsonify(message="Turma atualizada com sucesso!"), 200


# --- Deletar turma ---
@bp.delete("/<int:id>")
@swag_from(os.path.join(DOCS_DIR, "turmas_delete.yml"))
def deletar_turma(id):
    """
    Deletar turma
    ---
    tags:
      - Turmas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID da turma
        example: 1
    responses:
      200:
        description: Turma deletada com sucesso
      404:
        description: Turma não encontrada
    """
    turma = Turma.query.get(id)
    if not turma:
        return jsonify(message="Turma não encontrada!"), 404

    db.session.delete(turma)
    db.session.commit()
    return jsonify(message="Turma deletada com sucesso!"), 200
