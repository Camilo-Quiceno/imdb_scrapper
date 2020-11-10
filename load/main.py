import argparse

import pandas as pd

from article import Article
from base import Base, engine, Session

def main(filename):

    Base.metadata.create_all(engine) #Genera schema en nuestra base de datos
    session = Session() 
    articles = _read_data(filename)

    for index, row in articles.iterrows(): #Iterrows nos permite genrar un loop adentro de cada una nuestras filas de nuestro DataFrame
        print('Loading article uid {} into DB'.format(row['uid']))
        article = Article(row['uid'],
                          row['movie_title'],
                          row['movie_director'],
                          row['movie_sumary'],
                          row['movie_rating'],
                          row['movie_gender'],
                          row['movie_duration'],
                          row['movie_year'],
                          row['movie_host_uid'])

        session.add(article) #Ingresa nuestro articulo a la base de datos

    session.commit()
    session.close()


def _read_data(filename):
    print(f'Reading file {filename} ...')
    return pd.read_csv(filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument ('filename',
                         help='The path to the clean data',
                         type=str)

    args = parser.parse_args()

    main(args.filename)

    print('The project is loaded!')