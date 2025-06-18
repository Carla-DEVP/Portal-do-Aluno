# 🧑‍🎓 Portal do Aluno

Sistema web desenvolvido em Django para gestão acadêmica. O portal permite que alunos acessem informações como dados pessoais, disciplinas, notas, documentos, pagamentos e avisos.

---

## 🚀 Funcionalidades

- 🔐 Login e autenticação
- 🏠 Dashboard com visão geral do aluno
- 💳 Consulta de pagamentos
- 📘 Listagem de disciplinas matriculadas
- 📑 Visualização de documentos
- 📝 Consulta de notas
- 👤 Visualização de dados pessoais
- 📢 Avisos institucionais

---

## 🛠️ Tecnologias

- Python
- Django
- HTML5 + CSS3
- SQLite (banco local)

---

## 🖥️ Como rodar o projeto localmente

### ✔️ Pré-requisitos:

- Python instalado (3.8 ou superior)
- Git instalado (opcional, mas recomendado)

---

### 🔧 Passo a passo:

1. Clone o repositório:

```bash
git clone https://github.com/FernandoFigdev/Portal-do-Aluno.git
```

2. Acesse a pasta do projeto:

```bash
cd nome-do-repositorio
```

3. Crie e ative um ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

4. Instale as dependências:

```bash
pip install -r requirements.txt
```

5. Rode as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crie um superusuário:

```bash
python manage.py createsuperuser
```

7. Inicie o servidor:

```bash
python manage.py runserver
```

8. Acesse no navegador:

```
http://127.0.0.1:8000
```

---

## 🔐 Acesso ao Django Admin:

```
http://127.0.0.1:8000/admin
```

---

## 🗂️ Estrutura de pastas principal:

```
core/            → App principal (views, models, templates, static)
portal_aluno/    → Configurações do projeto Django
manage.py        → Gerenciador Django
requirements.txt → Dependências
README.md        → Documentação do projeto
.gitignore       → Arquivos e pastas ignoradas
```

---

## 📜 Licença

Projeto acadêmico desenvolvido para fins de aprendizado e apresentação.

---

## 👨‍💻 Desenvolvido por:

- **Fernando Figueiredo**
