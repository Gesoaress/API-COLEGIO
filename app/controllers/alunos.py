import os
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.extensions import db
from app.models import Aluno

bp = Blueprint("alunos", __name__, url_prefix="/alunos")

DOCS_DIR = os.path.join(os.path.dirname(__file__), "../docs")

# --- Criar aluno ---
@bp.post("/")
@swag_from(os.path.join(DOCS_DIR, "alunos_post.yml"))
def criar_aluno():
    dados = request.get_json()

    novo = Aluno(
        nome=dados["nome"],
        email=dados["email"],
        data_nascimento=dados.get("data_nascimento"),
        nota_1=dados.get("nota_1"),
        nota_2=dados.get("nota_2"),
        media_final=dados.get("media_final")
    )

    db.session.add(novo)
    db.session.commit()

    return jsonify(message="Aluno criado com sucesso!", id=novo.id), 201


# --- Listar alunos ---
@bp.get("/")
@swag_from(os.path.join(DOCS_DIR, "alunos_get.yml"))
def listar_alunos():
    alunos = Aluno.query.all()
    lista = [
        {
            "id": a.id,
            "nome": a.nome,
            "email": a.email,
            "data_nascimento": a.data_nascimento,
            "nota_1": a.nota_1,
            "nota_2": a.nota_2,
            "media_final": a.media_final
        }
        for a in alunos
    ]
    return jsonify(lista), 200


# --- Buscar aluno por ID ---
@bp.get("/<int:id>")
@swag_from(os.path.join(DOCS_DIR, "alunos_get_id.yml"))
def obter_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify(message="Aluno não encontrado!"), 404

    return jsonify(
        id=aluno.id,
        nome=aluno.nome,
        email=aluno.email,
        data_nascimento=aluno.data_nascimento,
        nota_1=aluno.nota_1,
        nota_2=aluno.nota_2,
        media_final=aluno.media_final
    ), 200


# --- Atualizar aluno ---
@bp.put("/<int:id>")
@swag_from(os.path.join(DOCS_DIR, "alunos_put.yml"))
def atualizar_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify(message="Aluno não encontrado!"), 404

    dados = request.get_json()
    aluno.nome = dados.get("nome", aluno.nome)
    aluno.email = dados.get("email", aluno.email)
    aluno.data_nascimento = dados.get("data_nascimento", aluno.data_nascimento)
    aluno.nota_1 = dados.get("nota_1", aluno.nota_1)
    aluno.nota_2 = dados.get("nota_2", aluno.nota_2)
    aluno.media_final = dados.get("media_final", aluno.media_final)

    db.session.commit()
    return jsonify(message="Aluno atualizado com sucesso!"), 200


# --- Deletar aluno ---
@bp.delete("/<int:id>")
@swag_from(os.path.join(DOCS_DIR, "alunos_delete.yml"))
def deletar_aluno(id):
    aluno = Aluno.query.get(id)
    if not aluno:
        return jsonify(message="Aluno não encontrado!"), 404

    db.session.delete(aluno)
    db.session.commit()
    return jsonify(message="Aluno deletado com sucesso!"), 200
