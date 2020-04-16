# Handling

## Processamento de Imagens

### Pacotes e Modulos

- [Pillow](https://pillow.readthedocs.io/en/stable)


## Preparando ambiente virtual

> Python version: 3.8.2

 ```bash
# O segundo venv indica o nome para o seu ambiente
$ python3 -m venv venv
```

 ```bash
# Navegar ate o script para ativar o ambiente
$ cd venv/scripts

# Ativar o ambiente
$ activate

# Desativar o ambiente
$ deactivate
``` 

## Pacotes e Modulos

```bash
# Instalar modulos
$ pip install Pillow
``` 

```bash
# Lista modulos instalados
$ pip freeze
``` 

```bash
# Cria arquivo com os modulos instalados
$ pip freeze > requirements.txt
``` 

```bash
# Instalar pacotes apartir do arquivo criado
$ pip install -r requirements.txt
``` 

```bash
# Remover modulos
$ pip uninstall Pillow
``` 

