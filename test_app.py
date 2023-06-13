import pytest
import sqlite3
from app import get_user_by_id

def test_get_user_by_id(mocker):
    # Substitui a função connect do módulo sqlite3 para retornar um objeto mock
    mock_conn = mocker.patch('sqlite3.connect', return_value=mocker.Mock())
    
    # Define a resposta para a chamada fetchone do cursor
    mock_conn.return_value.cursor.return_value.fetchone.return_value = ('1', 'John Doe')

    user = get_user_by_id(1)

    # Verifica se a função connect foi chamada com o nome correto do banco de dados
    sqlite3.connect.assert_called_with('users.db')

    # Verifica se o cursor executou a consulta SQL correta
    mock_conn.return_value.cursor.return_value.execute.assert_called_with('SELECT * FROM users WHERE id=1')

    # Verifica se a função retornou os dados corretos
    assert user == ('1', 'John Doe')

