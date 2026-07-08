CREATE TABLE cargo (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    permisao1 BOOLEAN NOT NULL,
    permisao2 BOOLEAN NOT NULL,
    permisao3 BOOLEAN NOT NULL,
    permisao4 BOOLEAN NOT NULL,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE cargo ADD CONSTRAINT cargo_nome_unique UNIQUE (nome);

CREATE TABLE responsavel (
    id BIGSERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NULL,
    email VARCHAR(150) NULL,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE responsavel ADD CONSTRAINT responsavel_telefone_unique UNIQUE (telefone);
ALTER TABLE responsavel ADD CONSTRAINT responsavel_email_unique UNIQUE (email);

CREATE TABLE equipe (
    id SERIAL PRIMARY KEY,
    id_cargo INTEGER NOT NULL, -- Corrigido para INTEGER para bater com cargo.id
    nome_completo VARCHAR(100) NOT NULL,
    telefone VARCHAR(20) NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE aluno (
    id SERIAL PRIMARY KEY,
    id_equipe INTEGER NOT NULL,
    id_responsavel BIGINT NOT NULL, -- Corrigido para BIGINT para bater com responsavel.id
    nome_completo VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    telefone VARCHAR(20) NULL,
    email VARCHAR(150) NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE curso (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(120) NOT NULL,
    descricao TEXT NULL,
    carga_horaria INTEGER NOT NULL, -- Em horas
    publico_alvo VARCHAR(200) NULL,
    pre_requisito VARCHAR(200) NULL,
    visivel_site BOOLEAN NOT NULL, -- Exibe na página pública
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE turma (
    id SERIAL PRIMARY KEY,
    id_curso INTEGER NOT NULL,
    nome_turma VARCHAR(80) NOT NULL, -- Ex: INFO-2026-MANHA
    limite_alunos INTEGER NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE professor_turma (
    id SERIAL PRIMARY KEY,
    id_equipe INTEGER NOT NULL,
    id_turma INTEGER NOT NULL,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE professor_turma ADD CONSTRAINT professor_turma_id_equipe_id_turma_unique UNIQUE (id_equipe, id_turma);

CREATE TABLE horario (
    id BIGSERIAL PRIMARY KEY,
    id_turma INTEGER NOT NULL,
    id_professor INTEGER NOT NULL,
    dia_semana VARCHAR(3) CHECK (dia_semana IN ('SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB')) NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fim TIME NOT NULL,
    sala VARCHAR(60) NULL,
    publicado BOOLEAN NOT NULL, -- Visível no portal do aluno
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE comunicado (
    id SERIAL PRIMARY KEY,
    id_autor INTEGER NOT NULL,
    titulo VARCHAR(200) NOT NULL,
    mensagem TEXT NOT NULL,
    destinatario VARCHAR(10) CHECK (destinatario IN ('TODOS', 'TURMA', 'PERFIL')) NOT NULL DEFAULT 'TODOS',
    id_turma INTEGER NULL, -- Preenchido quando destinatario = TURMA
    publicar_em TIMESTAMP NULL, -- Agendamento de publicação automática
    publicado BOOLEAN NOT NULL,
    visivel_site BOOLEAN NOT NULL, -- Exibe na seção de novidades do site
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE leitura_comunicado (
    id SERIAL PRIMARY KEY,
    id_comunicado INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    lido_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE leitura_comunicado ADD CONSTRAINT leitura_comunicado_id_comunicado_id_usuario_unique UNIQUE (id_comunicado, id_usuario);

CREATE TABLE log_auditoria (
    id SERIAL PRIMARY KEY,
    id_equipe INTEGER NULL, -- NULL quando ação é do sistema
    acao VARCHAR(100) NOT NULL, -- Ex: LOGIN, EDIT_ALUNO, DEL_FREQ
    tabela_afetada VARCHAR(80) NULL,
    dados_anteriores TEXT NULL, -- JSON com estado anterior
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE configuracao_site (
    id SERIAL PRIMARY KEY,
    chave VARCHAR(100) NOT NULL, -- Ex: TEXTO_SOBRE, WHATSAPP, LINK_MAPS
    valor TEXT NULL,
    atualizado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_por INTEGER NULL
);
ALTER TABLE configuracao_site ADD CONSTRAINT configuracao_site_chave_unique UNIQUE (chave);

CREATE TABLE matricula (
    id SERIAL PRIMARY KEY,
    id_aluno INTEGER NOT NULL,
    id_turma INTEGER NOT NULL,
    data_inicio DATE NOT NULL,
    data_saida DATE NOT NULL,
    status VARCHAR(15) CHECK (status IN ('ATIVO', 'CONCLUÍDO', 'CANCELADO')) NOT NULL,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE matricula ADD CONSTRAINT matricula_id_aluno_id_turma_unique UNIQUE (id_aluno, id_turma);

CREATE TABLE frequencia (
    id BIGSERIAL PRIMARY KEY,
    id_horario BIGINT NOT NULL,
    id_aluno INTEGER NOT NULL,
    data_aula DATE NOT NULL,
    status VARCHAR(15) CHECK (status IN ('PRESENTE', 'AUSENTE', 'JUSTIFICADO')) NOT NULL,
    justificativa TEXT NULL,
    registrado_por INTEGER NOT NULL,
    criado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- CHAVES ESTRANGEIRAS (FOREIGN KEYS)
ALTER TABLE frequencia ADD CONSTRAINT frequencia_registrado_por_foreign FOREIGN KEY (registrado_por) REFERENCES equipe(id);
ALTER TABLE matricula ADD CONSTRAINT matricula_id_turma_foreign FOREIGN KEY (id_turma) REFERENCES turma(id);
ALTER TABLE horario ADD CONSTRAINT horario_id_turma_foreign FOREIGN KEY (id_turma) REFERENCES turma(id);
ALTER TABLE configuracao_site ADD CONSTRAINT configuracao_site_atualizado_por_foreign FOREIGN KEY (atualizado_por) REFERENCES equipe(id);
ALTER TABLE comunicado ADD CONSTRAINT comunicado_id_autor_foreign FOREIGN KEY (id_autor) REFERENCES equipe(id);
ALTER TABLE matricula ADD CONSTRAINT matricula_id_aluno_foreign FOREIGN KEY (id_aluno) REFERENCES aluno(id);
ALTER TABLE horario ADD CONSTRAINT horario_id_professor_foreign FOREIGN KEY (id_professor) REFERENCES equipe(id);
ALTER TABLE professor_turma ADD CONSTRAINT professor_turma_id_equipe_foreign FOREIGN KEY (id_equipe) REFERENCES equipe(id);
ALTER TABLE aluno ADD CONSTRAINT aluno_id_equipe_foreign FOREIGN KEY (id_equipe) REFERENCES equipe(id);
ALTER TABLE professor_turma ADD CONSTRAINT professor_turma_id_turma_foreign FOREIGN KEY (id_turma) REFERENCES turma(id);
ALTER TABLE log_auditoria ADD CONSTRAINT log_auditoria_id_equipe_foreign FOREIGN KEY (id_equipe) REFERENCES equipe(id);
ALTER TABLE leitura_comunicado ADD CONSTRAINT leitura_comunicado_id_comunicado_foreign FOREIGN KEY (id_comunicado) REFERENCES comunicado(id);
ALTER TABLE aluno ADD CONSTRAINT aluno_id_responsavel_foreign FOREIGN KEY (id_responsavel) REFERENCES responsavel(id);
ALTER TABLE frequencia ADD CONSTRAINT frequencia_id_aluno_foreign FOREIGN KEY (id_aluno) REFERENCES aluno(id);
ALTER TABLE turma ADD CONSTRAINT turma_id_curso_foreign FOREIGN KEY (id_curso) REFERENCES curso(id);
ALTER TABLE equipe ADD CONSTRAINT equipe_id_cargo_foreign FOREIGN KEY (id_cargo) REFERENCES cargo(id);
ALTER TABLE frequencia ADD CONSTRAINT frequencia_id_horario_foreign FOREIGN KEY (id_horario) REFERENCES horario(id);