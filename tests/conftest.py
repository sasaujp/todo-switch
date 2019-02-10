import pytest
from todo_switch import create_app
from todo_switch.config import TestingConfig
from todo_switch.models import db
from sanic.websocket import WebSocketProtocol
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database


@pytest.fixture(scope='session')
def app(request):
    app = create_app()
    return app


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app, protocol=WebSocketProtocol))


@pytest.fixture(scope='session', autouse=True)
def create_db():
    testing_config = TestingConfig()
    db_host = testing_config.DB_HOST
    db_name = testing_config.DB_NAME
    engine = create_engine(f'postgresql://{db_host}/{db_name}')
    if not database_exists(engine.url):
        create_database(engine.url)
    yield
    drop_database(engine.url)
    engine.dispose()


@pytest.fixture()
def cleanup_db():
    testing_config = TestingConfig()
    db_host = testing_config.DB_HOST
    db_name = testing_config.DB_NAME
    engine = create_engine(f'postgresql://{db_host}/{db_name}')
    db.create_all(engine)
    yield engine
    db.drop_all(engine)
