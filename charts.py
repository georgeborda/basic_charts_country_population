import matplotlib.pyplot as plt  # Importar matplotlib

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)      # Crear grafica de barras con los labels y values
    plt.savefig(f'./imgs/{name}.png')      # Guarda la gráfica
    plt.close()                 # Cierra la gráfica


def generate_pie_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)     # Para los piecharts es necesario indicar explicitamente los labels
    ax.axis('equal')
    plt.savefig(f'./imgs/{name}.png')
    plt.close()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
