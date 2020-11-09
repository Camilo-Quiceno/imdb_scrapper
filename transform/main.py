import argparse

import pandas as pd

def main(filename):
    print(' -------Cleaning data------- ')

    df = _read_data(filename)

    df = _clean_lists(df)
    df = _transform_rating(df)
    df = _change_column_order(df)
    df = _filling_empty_spaces(df)
    df = _adding_uid(df)

    _save_data(df,filename)

    return df

def _read_data(filename):
    
    print(f'Reading file {filename} ...')

    return pd.read_csv(filename)


def _clean_lists(df):
    print(' -------Cleaning lists------- ')
    clean_movie_director = (df
                           .apply(lambda row: row['movie_director'], axis=1)
                           .apply(lambda movie_director_string: movie_director_string.strip("["))
                           .apply(lambda movie_director_string: movie_director_string.strip("]"))
                           .apply(lambda movie_director_string: movie_director_string.strip("'"))
                            )
    df['movie_director'] = clean_movie_director

    clean_movie_duration = (df
                           .apply(lambda row: row['movie_duration'], axis=1)
                           .apply(lambda movie_duration_string: movie_duration_string.strip("["))
                           .apply(lambda movie_duration_string: movie_duration_string.strip("]"))
                           .apply(lambda movie_duration_string: movie_duration_string.strip("'"))
                           .apply(lambda movie_duration_string: movie_duration_string.replace("\\n", ''))
                           .apply(lambda movie_duration_string: movie_duration_string.strip(" "))
                            )

    df['movie_duration'] = clean_movie_duration

    clean_movie_gender = (df
                           .apply(lambda row: row['movie_gender'], axis=1)
                           .apply(lambda movie_gender_string: movie_gender_string.strip("["))
                           .apply(lambda movie_gender_string: movie_gender_string.strip("]"))
                           .apply(lambda movie_gender_string: movie_gender_string.replace("'", ''))
                        )   

    df['movie_gender'] = clean_movie_gender

    clean_movie_rating = (df
                           .apply(lambda row: row['movie_rating'], axis=1)
                           .apply(lambda movie_rating_string: movie_rating_string.strip("["))
                           .apply(lambda movie_rating_string: movie_rating_string.strip("]"))
                           .apply(lambda movie_gender_string: movie_gender_string.replace("'", ''))
                           .apply(lambda movie_gender_string: movie_gender_string.replace("'", ''))
                        )   

    df['movie_rating'] = clean_movie_rating


    clean_movie_sumary = (df
                           .apply(lambda row: row['movie_sumary'], axis=1)
                           .apply(lambda movie_sumary_string: movie_sumary_string.strip("["))
                           .apply(lambda movie_sumary_string: movie_sumary_string.strip("]"))
                           .apply(lambda movie_sumary_string: movie_sumary_string.replace("'", ''))
                           .apply(lambda movie_sumary_string: movie_sumary_string.replace('"', ''))
                           .apply(lambda movie_sumary_string: movie_sumary_string.replace("\\n", ''))
                           .apply(lambda movie_sumary_string: movie_sumary_string.strip(" "))
                        )   

    df['movie_sumary'] = clean_movie_sumary

    clean_movie_title = (df
                           .apply(lambda row: row['movie_title'], axis=1)
                           .apply(lambda movie_title_string: movie_title_string.strip("["))
                           .apply(lambda movie_title_string: movie_title_string.strip("]"))
                           .apply(lambda movie_title_string: movie_title_string.replace("'", ''))
                           .apply(lambda movie_sumary_string: movie_sumary_string.replace('\\xa0', ''))
                        )   

    df['movie_title'] = clean_movie_title
    
    clean_movie_year = (df
                           .apply(lambda row: row['movie_year'], axis=1)
                           .apply(lambda movie_year_string: movie_year_string.strip("["))
                           .apply(lambda movie_year_string: movie_year_string.strip("]"))
                           .apply(lambda movie_year_string: movie_year_string.replace("'", ''))
                        )   

    df['movie_year'] = clean_movie_year

    return df


def _transform_rating(df):
    print(' -------Transforming rating------- ')
    float_movie_rating = (df
                           .apply(lambda row: row['movie_rating'], axis=1)
                           .apply(lambda movie_rating_string: float(movie_rating_string) if movie_rating_string else 'NC')
                            )

    df['movie_rating'] = float_movie_rating

    return df


def _change_column_order(df):
    print(' -------Changing column order------- ')
    df = df[['movie_title','movie_director','movie_sumary','movie_rating','movie_gender','movie_duration','movie_year']]
    df.head()

    return df


def _filling_empty_spaces(df):
    print(' -------Filling empty spaces------- ')
    movie_duration_fill = (df
                            .apply(lambda row: row['movie_duration'], axis=1)
                            .apply(lambda movie_duration_string: movie_duration_string if movie_duration_string else 'NC')
                            )

    df['movie_duration'] = movie_duration_fill

    return df

def _adding_uid(df):
    print(' -------Adding uid------- ')
    count_row = df.shape[0]
    
    uid = []

    for i in range(1,count_row + 1):
        uid.append(i)
    
    df['uid'] = uid
 
    return df.set_index('uid') #Le decimos al DataFrame que el nuevo uid será nuestro index

def _save_data(df,filename):
    print(' -------Saving clean data------- ')
    clean_filename = 'clean_{}'.format(filename)
    print('Saving data at location: {}'.format(clean_filename))
    df.to_csv(clean_filename,encoding='utf-8-sig')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument ('filename',
                         help='The path to the dirty data',
                         type=str)
    args = parser.parse_args()

    df = main(args.filename)

    print('Transform is done!')