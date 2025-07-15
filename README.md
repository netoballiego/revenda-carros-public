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
```


📁 Estrutura do Projeto:

revenda-carros/
├── carros/               # App principal
├── openai_api/           # Geração de argumentos via OpenAI
├── templates/            # HTML com estrutura moderna
├── static/               # Imagens, CSS, JS
├── .env.example          # Variáveis de ambiente de exemplo
├── requirements.txt
└── manage.py


📸 Demonstração:

<img width="1887" height="923" alt="Captura de tela 2025-07-15 075117" src="https://github.com/user-attachments/assets/94ddc77d-f7e2-452c-9a16-6ab5c5bb63e4" />

<img width="1882" height="918" alt="Captura de tela 2025-07-15 075144" src="https://github.com/user-attachments/assets/962ac5cc-4ebc-4e95-aa5f-8996f36b1545" />






