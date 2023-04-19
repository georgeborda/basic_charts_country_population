import utils
import read_csv
import charts


def main():
    data = read_csv.read_csv('./data.csv')      # Get the data in a list of dictionaries
    country = input('Type country => ')     # Select the country
    result = utils.population_by_country(data, country) # Get the dictionary of the chosen country

    # generate bar chart with a country data
    if len(result) > 0:     # if found the country
        country = result[0]     
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels,values)     

    # generate pie chart of some countries 
    column = 'World Population Percentage'  
    continent = 'South America'
    labels, values = utils.population_by_year(data, column, continent)
    charts.generate_pie_chart(continent, labels, values)


if __name__ == '__main__':
    main()