import subprocess
import datetime 


def main():
    print("Welcome to the pipeline")

    movies_host_uids = ['imdb','reelgood']
    now = datetime.datetime.now().strftime("%Y_%m_%d")

    for movie_host_uid in movies_host_uids:
        
        csv_name = f'{movie_host_uid}_{now}_movies_info.csv'

        #Extract
        subprocess.run(['python','main.py',movie_host_uid],cwd='.\extract')
        subprocess.run(['copy',r'.\extract\*.csv',r'.\transform\*.csv'],shell=True)
        subprocess.run(['del',r'.\extract\*.csv'],shell=True)
        
        #Transform
        subprocess.run(['python','main.py',csv_name],cwd='./transform')
        subprocess.run(['copy',r'.\transform\*.csv',r'.\load\*.csv'],shell=True)
        subprocess.run(['del',r'.\transform\*.csv'],shell=True)
    
        #Load
        subprocess.run(['python','main.py',f'clean_{csv_name}'],cwd='./load')
        subprocess.run(['del',r'.\load\*.csv'],shell=True)

        print(f'Scrapper finish with {movie_host_uid} scrapping!')


if __name__ == "__main__":
    
    main()
    print('DONE!')