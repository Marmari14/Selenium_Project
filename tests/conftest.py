import pytest


@pytest.fixture()
def set_up():
    print("\nЗапуск теста")
    yield
    print("\nТест завершен!")