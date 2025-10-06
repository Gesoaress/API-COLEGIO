from app.extensions import db

# --- Professor ---
class Professor(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    materia = db.Column(db.String(100))
    observacoes = db.Column(db.Text)
    email = db.Column(db.String(100), unique=True, nullable=False)

    turmas = db.relationship("Turma", back_populates="professor", cascade="all, delete")

    def __repr__(self):
        return f"<Professor {self.nome}>"


# --- tabela de associação entre Aluno e Turma (caso ainda queira N:N)
matricula_turma = db.Table(
    "matriculas",
    db.Column('aluno_id', db.Integer, db.ForeignKey('alunos.id'), primary_key=True),
    db.Column('turma_id', db.Integer, db.ForeignKey('turmas.id'), primary_key=True)
)


# --- Turma ---
class Turma(db.Model):
    __tablename__ = "turmas"

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    ativo = db.Column(db.Boolean, default=True)

    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    professor = db.relationship("Professor", back_populates="turmas")

    # relacionamento com alunos (One-to-Many)
    alunos = db.relationship("Aluno", back_populates="turma", cascade="all, delete")

    def __repr__(self):
        return f"<Turma {self.descricao}>"


# --- Aluno ---
class Aluno(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=True)  # formato 'YYYY-MM-DD'
    nota_1 = db.Column(db.Float, nullable=True)
    nota_2 = db.Column(db.Float, nullable=True)
    media_final = db.Column(db.Float, nullable=True)

    turmas = db.relationship("Turma", secondary=matricula_turma, back_populates="alunos")

    def __repr__(self):
        return f"<Aluno {self.nome}>"

