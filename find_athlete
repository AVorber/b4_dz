from datetime import datetime

import sqlalchemy as sa

from athlets.connection import Base, connection_db
from athlets.users import User


class Athelete(Base):
    __tablename__ = 'athelete'
    id = sa.Column(sa.Integer, primary_key=True)
    age = sa.Column(sa.Integer)
    birthdate = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.Float)
    weight = sa.Column(sa.Integer)
    name = sa.Column(sa.Text)
    gold_medals = sa.Column(sa.Integer)
    silver_medals = sa.Column(sa.Integer)
    bronze_medals = sa.Column(sa.Integer)
    total_medals = sa.Column(sa.Integer)
    sport = sa.Column(sa.Text)
    country = sa.Column(sa.Text)


def request_user():
    user_id = int(input('Введите id пользователя: '))
    return user_id


def convert_date(date):
    parts = date.split('-')
    date_parts = map(int, parts)
    date = datetime.date(*date_parts)
    return date


def nearest_by_birthdate(user, session):
    athletes = session.query(Athelete).all()
    athlete_id_bd = {}
    for athlete in athletes:
        bd = convert_date(athlete.birthdate)
        athlete_id_bd[athlete.id] = bd

    user_bd = convert_date(user.birthdate)
    min_dist = None
    athlete_id = None

    for id_, bd in athlete_id_bd.items():
        dist = abs(user_bd - bd)
        if not min_dist or dist < min_dist:
            min_dist = dist
            athlete_id = id_

    return athlete_id


def nearest_by_height(user, session):
    athletes_list = session.query(Athelete).all()
    atlhete_id_height = {athlete.id: athlete.height for athlete in athletes_list}

    user_height = user.height
    min_dist = None
    athlete_id = None

    for id_, height in atlhete_id_height.items():
        if height is None:
            continue

        dist = abs(user_height - height)
        if not min_dist or dist < min_dist:
            min_dist = dist
            athlete_id = id_

    return athlete_id


def main():
    session = connection_db()
    user_id = request_user()
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        print('Нет такого пользователя')
    else:
        bd_athlete = nearest_by_birthdate(user, session)
        height_athlete = nearest_by_height(user, session)
        print(f'Ближайший по дате рождения атлет: {bd_athlete}')
        print(f'Ближайший по росту атлет: {height_athlete}')


if __name__ == '__main__':
    main()
