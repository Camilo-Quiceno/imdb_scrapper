import argparse
import movie_page_objects as movie
import datetime #Módulo para usar la hora en que se ejecuta el código
import csv #Módulo para almacenar los resultados en formato .csv

from common import config

def _movie_scrapper(movie_site_id):
    
    host = config()['movie_site'][movie_site_id]['url']

    print(f'Welcome! \nThe site: {movie_site_id} is going to be scraped...')
    
    homepage = movie.HomePage(movie_site_id,host)
    links = homepage.movie_links
    
    print(f'You are going to scrap: {len(links)} links')

    movies = []
    movie_number = 1

    for link in links:

        url = config()['movie_site'][movie_site_id]['url_base'] + link

        movie_page = movie.MoviePage(movie_site_id,url)
        movies.append(movie_page)
        print(f'Movie {movie_page.movie_title[0]} fetched! {movie_number} of {len(links)}')
        movie_number += 1

    _save_movies(movie_site_id,movies)


def _save_movies(movie_site_id,movies_info):
    now = datetime.datetime.now().strftime('%Y_%m_%d') #Se toma el momento en que se ejecuta el programa
    out_file_name = '{}_{}_movies_info.csv'.format(movie_site_id,now) #Se le da nombre al archivo teniendo en cuenta la hora y el sitio

    csv_headears = list(filter(lambda property: not property.startswith('_'), dir(movies_info[0])))

    #Se escribe sobre el archivo creado.
    with open(out_file_name, mode='w+',encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(csv_headears)

        for movies_info in movies_info:
            row = [str(getattr(movies_info, prop)) for prop in csv_headears]
            writer.writerow(row)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    movie_site_choices = list(config()['movie_site'].keys()) 
    parser.add_argument('movie_site',
                        help='The movie store that you want to scrape',
                        type=str,
                        choices=movie_site_choices)
    args = parser.parse_args()
    _movie_scrapper(args.movie_site)