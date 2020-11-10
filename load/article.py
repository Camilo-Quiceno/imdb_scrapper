from sqlalchemy import Column, String, Integer

from base import Base


class Article(Base):
    __tablename__ = 'articles'

    id = Column(String, primary_key=True)
    movie_title = Column(String)
    movie_director = Column(String)
    movie_sumary = Column(String)
    movie_rating = Column(String)
    movie_gender = Column(String)
    movie_duration = Column(String)
    movie_year = Column(Integer)
    movie_host_uid = Column(String)


    def __init__(self,
                 uid,
                 movie_title,
                 movie_director,
                 movie_sumary,
                 movie_rating,
                 movie_gender,
                 movie_duration,
                 movie_year,
                 movie_host_uid):
                 
        self.id = uid
        self.movie_title = movie_title
        self.movie_director = movie_director
        self.movie_sumary = movie_sumary
        self.movie_rating = movie_rating
        self.movie_gender = movie_gender
        self.movie_duration = movie_duration
        self.movie_year = movie_year
        self.movie_host_uid = movie_host_uid