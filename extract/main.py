import argparse
import movie_page_objects as movie
import datetime #Módulo para usar la hora en que se ejecuta el código
import csv #Módulo para almacenar los resultados en formato .csv

from common import config

def _movie_scrapper(movie_site_id):
    host = config()['movie_site'][movie_site_id]['url']
    print(f'Welcome! \nThe site: {host} is going to be scrap...')

    homepage = movie.HomePage(movie_site_id,host)
    links = homepage.movie_links

    print(links)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    movie_site_choices = list(config()['movie_site'].keys()) 
    parser.add_argument('movie_site',
                        help='The movie store that you want to scrape',
                        type=str,
                        choices=movie_site_choices)
    args = parser.parse_args()
    _movie_scrapper(args.movie_site)