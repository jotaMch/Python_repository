from flask import Blueprint, render_template, request
from database.client import CLIENTES

client_route = Blueprint('client', __name__)

@client_route.route('/')
def list_clients():
    return render_template('list_clients.html', clients = CLIENTES)


@client_route.route('/', methods=['POST'])
def insert_client():
    """inserir cliente"""
    data = request.json
    novo_usuario = {
        "id": len(CLIENTES) + 1,
        "name": data('name'),
        "email": data('email'),
    }
    CLIENTES.append(novo_usuario)
    return {"client": novo_usuario}


@client_route.route('/new')
def form_client():
    """ formulário para cadastrar cliente """
    return render_template('form_client.html')


@client_route.route('/<int:client_id>')
def details_client(client_id):
    """ exibir detalhes do cliente """
    return render_template('details_client.html')


@client_route.route('/<int:client_id>/edit')
def form_edit_client(client_id):
    """ formulário para editar um cliente """
    return render_template('form_edit_client.html')


@client_route.route('/<int:client_id>/update', methods=['PUT'])
def update_client(client_id):
    """ atualizar informações do cliente """
    pass


@client_route.route('/<int:client_id>/delete', methods=['PUT'])
def delete_client(client_id):
    """ deletar informações do cliente """
    pass
