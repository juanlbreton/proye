import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 65, 275]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie_chart.png')
    plt.close()