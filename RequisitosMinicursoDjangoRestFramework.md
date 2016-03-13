# Requisitos para o minicurso de Django Rest Framework

O notebook do participante deve ter:

* Python 3.4+
* Virtualenv
* Pip

## Criação do ambiente de desenvolvimento

Para o nosso curso, é recomendado que seja criado um ambiente separado que não interfira com os pacotes instalados na máquina. 
Para isto, usaremos o [virtualenv](https://pypi.python.org/pypi/virtualenv/)

```
mkdir curso-linguagil2016
cd curso-linguagil2016 
virtualenv env -p $(which python3)
```

Para ativar este ambiente:

```
source env/bin/activate
```

Note que no shell deve ter aparecido _(env)_ antes do seu prompt normal. Para desativá-lo, faça:

```
deactivate
```

## Instalação dos pacotes básicos

Dentro do ambiente ativado, use o pip para instalar os pacotes básicos para o nosso curso:

```
pip install --upgrade pip==8.1.0
pip install Django==1.9.4 django-extensions==1.6.1 django-filter==0.12.0 djangorestframework==3.3.2
```

Durante o curso, instalaremos outros pacotes.
