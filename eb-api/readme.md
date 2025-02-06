para usar o EB abrir terminal
source ~/.ebcli-virtual-env/bin/activate

para criar a aplicação no aws
eb init -p python-3.12 api-flask --region us-east-1

para criar o ambbiente
eb create flask-env-dev

para atualizar
eb deploy {nome do ambiente}

para terminar o ambiente
eb terminate flask {ambiente}
