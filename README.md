# Computacao-em-nuvem

# AbracadabraKids

Sistema web desenvolvido em **Python com Flask** para o gerenciamento de crianças cadastradas na empresa **AbracadabraKids**, uma empresa voltada para recreação infantil.

O projeto foi desenvolvido como parte do **Projeto Integrado** das disciplinas de **Computação em Nuvem** e **Qualidade de Software**, com o objetivo de demonstrar uma aplicação web funcional, com banco de dados, autenticação de usuários, monitoramento básico e possibilidade de futura implantação em ambiente de nuvem.

---

## Objetivo do Projeto

O objetivo principal do projeto é criar uma aplicação web simples, funcional e organizada, capaz de realizar o gerenciamento de crianças cadastradas no sistema.

A aplicação permite:

- Cadastro de usuários;
- Login e logout;
- Cadastro de crianças;
- Listagem dos registros cadastrados;
- Exclusão de registros;
- Armazenamento das informações em banco de dados;
- Monitoramento básico da aplicação através da rota `/health`.

Além das funcionalidades práticas, o projeto busca demonstrar conceitos importantes de:

- Desenvolvimento web;
- Banco de dados;
- Segurança básica;
- Computação em nuvem;
- Qualidade de software;
- Organização e manutenção de código.

---

## Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Python** — linguagem principal da aplicação;
- **Flask** — framework web utilizado no back-end;
- **Flask-SQLAlchemy** — biblioteca utilizada para integração com banco de dados;
- **SQLite** — banco de dados local utilizado para persistência das informações;
- **HTML5** — estrutura das páginas web;
- **CSS3** — estilização visual das telas;
- **Werkzeug** — biblioteca utilizada para gerar hash das senhas dos usuários.

---

## Estrutura do Projeto

A estrutura de arquivos do projeto está organizada da seguinte forma:

```text
AbracadabraKids/
│
├── app.py
├── requirements.txt
├── README.md
│
├── static/
│   └── style.css
│
└── templates/
    ├── login.html
    ├── register.html
    └── home.html
```

---

## Descrição dos Arquivos

### `app.py`

Arquivo principal da aplicação.

Ele é responsável por:

- Inicializar o Flask;
- Configurar o banco de dados SQLite;
- Criar as tabelas do sistema;
- Definir as rotas da aplicação;
- Controlar login e logout;
- Cadastrar usuários;
- Cadastrar crianças;
- Listar registros;
- Excluir registros;
- Disponibilizar o endpoint de monitoramento `/health`.

---

### `requirements.txt`

Arquivo que contém as bibliotecas necessárias para executar o projeto.

Conteúdo esperado:

```txt
Flask==3.1.0
Flask-SQLAlchemy==3.1.1
Werkzeug==3.1.3
```

---

### `templates/`

Pasta onde ficam as páginas HTML da aplicação.

Arquivos principais:

- `login.html` — tela de login do sistema;
- `register.html` — tela de cadastro de usuário;
- `home.html` — tela principal após o login.

---

### `static/`

Pasta onde ficam os arquivos estáticos do projeto.

Arquivo principal:

- `style.css` — arquivo responsável pela aparência visual do sistema.

---

## Como Executar o Projeto

### 1. Baixar ou clonar o repositório

Caso o projeto esteja no GitHub, clone o repositório:

```bash
git clone LINK_DO_REPOSITORIO
```

Depois acesse a pasta do projeto:

```bash
cd AbracadabraKids
```

Caso esteja utilizando os arquivos manualmente, basta abrir a pasta `AbracadabraKids` no VS Code.

---

### 2. Abrir o projeto no VS Code

Abra o **Visual Studio Code** e selecione:

```text
File > Open Folder
```

Depois escolha a pasta do projeto:

```text
AbracadabraKids
```

---

### 3. Instalar as dependências

No terminal do VS Code, execute:

```bash
python -m pip install -r requirements.txt
```

Caso ocorra algum erro com o arquivo `requirements.txt`, instale as bibliotecas manualmente:

```bash
python -m pip install Flask Flask-SQLAlchemy Werkzeug
```

---

### 4. Executar a aplicação

Ainda no terminal, execute:

```bash
python app.py
```

Se tudo estiver correto, será exibida uma mensagem semelhante a esta:

```text
* Running on http://127.0.0.1:5000
```

---

### 5. Acessar o sistema no navegador

Abra o navegador e acesse:

```text
http://127.0.0.1:5000
```

O sistema irá direcionar automaticamente para a tela de login.

---

## Como Usar o Sistema

### 1. Criar uma conta

Acesse a tela de cadastro:

```text
http://127.0.0.1:5000/register
```

Informe:

- Nome de usuário;
- Senha.

Depois clique em **Cadastrar**.

---

### 2. Fazer login

Após criar a conta, acesse:

```text
http://127.0.0.1:5000/login
```

Informe o usuário e a senha cadastrados.

Depois clique em **Entrar**.

---

### 3. Acessar a tela principal

Após o login, o usuário será redirecionado para a página principal do sistema.

Nessa tela é possível visualizar:

- Quantidade de crianças cadastradas;
- Formulário de cadastro;
- Tabela com os registros cadastrados;
- Informações gerais sobre o sistema.

---

### 4. Cadastrar uma criança

Na tela principal, preencha os campos:

- Nome da criança;
- Idade;
- Responsável.

Depois clique em **Cadastrar**.

O registro será salvo no banco de dados e aparecerá automaticamente na tabela de crianças cadastradas.

---

### 5. Excluir uma criança

Na tabela de crianças cadastradas, clique no botão **Excluir** ao lado do registro desejado.

Após a ação, o sistema remove o registro do banco de dados.

---

### 6. Sair do sistema

Para encerrar a sessão, clique no botão **Sair**.

O usuário será redirecionado para a tela de login.

---

## Endpoint de Monitoramento

O sistema possui um endpoint de verificação chamado **health check**.

Ele pode ser acessado através da rota:

```text
http://127.0.0.1:5000/health
```

Esse endpoint retorna uma resposta em formato JSON informando se a aplicação está online.

Exemplo de resposta:

```json
{
  "status": "online",
  "system": "AbracadabraKids"
}
```

Esse tipo de recurso é bastante utilizado em ambientes de produção e computação em nuvem para verificar a saúde da aplicação.

---

## Banco de Dados

O banco de dados utilizado no projeto é o **SQLite**.

Ele é criado automaticamente na primeira execução da aplicação.

O sistema armazena:

- Usuários cadastrados;
- Crianças cadastradas.

O arquivo do banco é gerado automaticamente com o nome:

```text
database.db
```

---

## Segurança

O sistema utiliza a biblioteca **Werkzeug** para proteger as senhas dos usuários.

As senhas não são armazenadas em texto puro.

Antes de serem salvas no banco de dados, elas são transformadas em **hash**, aumentando a segurança da aplicação.

Essa prática evita que a senha real do usuário fique exposta no banco.

---

## Relação com Computação em Nuvem

Embora o projeto seja executado localmente durante o desenvolvimento, ele foi estruturado pensando em uma futura implantação em ambiente de nuvem.

A aplicação poderia ser hospedada em provedores como:

- AWS;
- Microsoft Azure;
- Google Cloud.

Em um cenário real, o sistema poderia ser implantado em:

- Máquina virtual;
- Serviço PaaS;
- Container Docker;
- Ambiente com CI/CD;
- Banco de dados em nuvem.

A utilização da nuvem permitiria benefícios como:

- Maior disponibilidade;
- Escalabilidade;
- Monitoramento contínuo;
- Facilidade de manutenção;
- Implantação de novas versões com mais segurança.

---

## Relação com Qualidade de Software

Durante o desenvolvimento foram aplicadas práticas básicas de qualidade de software, como:

- Organização dos arquivos do projeto;
- Separação entre interface, estilos e lógica da aplicação;
- Uso de banco de dados para persistência;
- Autenticação de usuários;
- Hash de senhas;
- Endpoint de monitoramento;
- Código simples e de fácil manutenção.

Essas práticas contribuem para tornar o sistema mais confiável, seguro, organizado e preparado para futuras melhorias.

---

## Funcionalidades Implementadas

O sistema possui as seguintes funcionalidades:

- Cadastro de usuários;
- Login de usuários;
- Logout;
- Cadastro de crianças;
- Listagem de crianças cadastradas;
- Exclusão de registros;
- Banco de dados SQLite;
- Interface web estilizada;
- Endpoint de monitoramento `/health`.

---

## Possíveis Melhorias Futuras

O projeto foi desenvolvido em uma versão simplificada, mas pode ser expandido futuramente com novas funcionalidades, como:

- Edição de registros;
- Cadastro de brinquedos;
- Cadastro de monitores;
- Cadastro de eventos;
- Controle financeiro;
- Relatórios;
- Dashboard administrativo;
- Testes automatizados;
- Deploy em nuvem;
- Integração contínua e entrega contínua;
- Banco de dados em nuvem.

---

## Como Parar a Aplicação

Para parar o servidor Flask, volte ao terminal onde o sistema está rodando e pressione:

```bash
CTRL + C
```

---

## Integrantes

- Gustavo Costa Jorge
- Jhones Medeiros Martins
- Thauan Thales Paulista

---

## Considerações Finais

O projeto **AbracadabraKids** demonstra a criação de uma aplicação web funcional utilizando Python, Flask e SQLite.

A solução apresenta autenticação de usuários, persistência de dados, gerenciamento de registros e monitoramento básico da aplicação.

Mesmo sendo uma versão acadêmica e simplificada, o sistema possui estrutura para evoluir e ser implantado futuramente em ambientes de computação em nuvem.
