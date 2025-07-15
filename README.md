# 🚘 Revenda Carros • Plataforma Web para Gestão e Venda Inteligente de Veículos

Projeto em desenvolvimento para praticar conceitos de **Django** e **boas práticas de programação web**, com foco em um sistema de revenda de automóveis.

A aplicação permite **cadastrar, listar e buscar veículos** em uma interface simples e responsiva, voltada para fins de estudo e evolução pessoal.

Como diferencial, inclui uma **integração experimental com a OpenAI**, que gera sugestões de **argumentos de venda personalizados** com base nas características do carro — recurso pensado para simular um assistente virtual de apoio à equipe comercial.

---

## ✨ Principais Recursos

✅ Cadastro de veículos com:
- Marca, modelo, ano de fabricação/modelo, valor e imagem.

🔍 Filtro e busca inteligente:
- Pesquise rapidamente por modelo, marca ou ano.

🧠 Integração com OpenAI:
- Geração automática de **argumentos de venda persuasivos** com base nas características do carro.

🔐 Autenticação:
- Cadastro, login e logout para segurança e controle de acesso.

---

## 💡 Casos de Uso

- Estudo prático de desenvolvimento web com Django.
- Simulação de uma plataforma de revenda para aprendizado.
- Testes com integração à OpenAI para gerar textos automáticos.
- Base para projetos futuros com funcionalidades comerciais reais.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Django 4.x**
- **HTML5 + CSS3**
- **OpenAI API**
- **SQLite** → utilizado durante o desenvolvimento local
- **PostgreSQL** → utilizado na aplicação em produção (servidor **EC2 AWS Ubuntu**)
- Deploy realizado manualmente via SSH no EC2 (Nginx)

---

## 🚀 Como rodar o projeto localmente

```bash
# 1. Clone o repositório
git clone https://github.com/netoballiego/revenda-carros-public.git
cd revenda-carros-public

# 2. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/macOS

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o ambiente
cp .env.example .env
# (adicione sua chave OpenAI e configs do Django)

# 5. Aplique migrações e rode o servidor
python manage.py migrate
python manage.py runserver
