from sqlalchemy import select

from app.models import User


def test_create_user(session):
    new_user = User(username='alice', password='secret', email='teste@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert user.username == 'alice'


def test_repr_user():
    user = User(username='alice', password='secret', email='teste@test')
    assert repr(user) == 'User(username=alice, email=teste@test)'
