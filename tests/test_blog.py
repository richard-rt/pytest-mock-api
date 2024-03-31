from unittest.mock import patch
from blog.blog import Blog
from tests.conftest import posts_fixture, first_post_fixture

@patch('blog.blog.requests.get')
def test_posts(mock_get):
    # Definindo o retorno simulado da chamada à API
    mock_get.return_value.json.return_value = posts_fixture

    blog = Blog()
    posts = blog.posts()

    # Verificando se o método retornou os posts corretamente
    assert posts == posts_fixture

@patch('blog.blog.requests.get')
def test_post_by_user_id(mock_get):
    # Definindo o retorno simulado da chamada à API
    mock_get.return_value.json.return_value = first_post_fixture  # Usando apenas o primeiro post para este teste

    blog = Blog()
    post = blog.post_by_user_id("1")

    # Verificando se o método retornou o post corretamente
    assert post == first_post_fixture