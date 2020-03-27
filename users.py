import sqlalchemy as sa

from athlets.connection import Base, connection_db


class User(Base):
    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)


def request_user():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    gender = input('Ваш пол м/ж: ')
    email = input('Адрес электронной почты: ')
    birthdate = input('Дата рождения: ')
    height = input('Ваш рост: ')
    return User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )


def main():
    session = connection_db()
    user = request_user()
    session.add(user)
    session.commit()


if __name__ == '__main__':
    main()
