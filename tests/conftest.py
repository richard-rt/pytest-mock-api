import pytest


@pytest.fixture
def posts_fixture():
    posts = [
        {'userId': 1, 'id': 1, 'title': 'Titulo teste 1', 'body': 'Conteudo do blog 1'},
        {'userId': 2, 'id': 2, 'title': 'Titulo teste 2', 'body': 'Teste de conteudo do blog 2'}
    ]
    return posts


@pytest.fixture
def first_post_fixture(posts_fixture):
    return posts_fixture[0]
