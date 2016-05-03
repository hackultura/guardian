# Guardian

Sistema de registro de visitantes para controle interno da Secretaria de Cultura do DF.

# Requisitos minimos

 - Python 3.5
 - PostgreSQL
 - Autoenv
 - Virtualenv

# Instalação

1 - Faça o checkout do projeto:

```bash
git clone 
```

2 - Cria um ambiente virtual:

```bash
$ cd guardian
$ virtualenv venv
```

3 - Ative o ambiente virtual e instale as dependências:

```bash
$ source venv/bin/activate
(guardian)$ pip install -r requirements.txt
```

4 - Cria o banco de dados no PostgreSQL:

```bash
$ psql -U postgres
$ Password: ******
postgres=# CREATE DATABASE guardian;
```

5 - Faça as configurações do seu banco de dados, exportando uma variável de ambiente com o nome `DATABASE_URL` ou use o [autoenv](https://github.com/kennethreitz/autoenv) para fazer automaticamente isso
acessando o arquivo `.env` na raiz do seu projeto. Ele pode ser baseado no `env.template`:

```bash
(guardian)$ export DATABASE_URL="postgres://user:password@localhost/guardian"
```

```bash
(guardian)$ mv env.template .env
(guardian)$ autoenv_init
```

Para mais informações de como instalar e usar o autoenv, acesse [aqui](https://github.com/kennethreitz/autoenv).

6 - Rode as migrações do projeto:

```bash
(guardian)$ python manage.py migrate
```

7 - Levante o servidor local
```bash
(guardian)$ python manage.py runserver
```

Licença: GPLv2
