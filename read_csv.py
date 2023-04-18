import csv

def read_csv(path):     # path es la ruta del archivo
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')   # delimiter es para seleccionar cual es el delimitador entre datos, en este caso los datos son delimitados por una coma ','
        # En reader quedan grabados todos los datos del archivo, reader es un iterable
        header = next(reader)   # La primera línea del dataset será el header
        data = []       # Lista donde se grabarán todos los datos en forma de diccionario

        for row in reader:
            iterable = zip(header, row)     # Combinar el header con la fila
            country_dict = {key:value for key, value in iterable}       # dictionary comprehension para pasar las tuplas de iterable a la llave y el valor en un diccionario
            data.append(country_dict)

        return data

if __name__ == '__main__':
    data = read_csv('./data.csv')
    print(data[0])
    '''
    {'Rank': '36', 'CCA3': 'AFG', 'Country/Territory': 'Afghanistan', 'Capital': 'Kabul', 'Continent': 'Asia', '2022 Population': '41128771', '2020 Population': '38972230', '2015 Population': '33753499', '2010 Population': '28189672', '2000 Population': '19542982', '1990 Population': '10694796', '1980 Population': '12486631', '1970 Population': '10752971', 'Area (kmÂ²)': '652230', 'Density (per kmÂ²)': '63.0587', 'Growth Rate': '1.0257', 'World Population Percentage': '0.52'}
    '''