import os


class Config:
    DB_HOST = 'todo-switch@127.0.0.1:5432'
    DB_NAME = 'todo-switch'


class TestingConfig:
    DB_HOST = 'todo-switch@127.0.0.1:5432'
    DB_NAME = 'todo-switch-testing'


def get_configuration():
    if os.getenv('testing'):
        return TestingConfig()
    return Config()
