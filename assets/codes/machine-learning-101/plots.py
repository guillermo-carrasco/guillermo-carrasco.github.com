import matplotlib.pyplot as plt
import numpy as np

# Create data points
x = np.array([0, 1, 2, 3.5, 4, 4.5, 5.1, 7.3, 8, 8.4, 9, 10])
y = np.array([0, 1.1, 2.3, 3, 4, 5.3, 6, 7, 8.4, 9.2, 9.7, 10])

def scatter_labels():
    """ Write titles and labels for the scatter plot
    """
    plt.title('Hours studied and grade obtained')
    plt.xlabel('Hours studied')
    plt.ylabel('Grade')
    plt.xlabel('Hours')
    plt.xlim((0, 10))
    plt.ylim((0, 10))

def show_data_points():
    scatter_labels()
    plt.scatter(x, y)
    plt.show()

def show_datapoints_with_lines():
    scatter_labels()
    # Datapoints
    plt.scatter(x, y, marker='x', c='b')
    # Overfitting
    plt.annotate('Overfitting',
                 ha='center',
                 va='center',
                 xytext = (5, 7),
                 xy = (6, 6.5),
                 arrowprops = {
                    'facecolor' : 'red',
                    'edgecolor': 'red',
                    'arrowstyle': '->'
                 })
    plt.plot(x, y, c='r')
    # Underfitting
    plt.annotate('Too optimistic',
                 ha='center',
                 va='center',
                 xytext = (1.5, 8),
                 xy = (3, 6),
                 arrowprops = {
                    'facecolor' : 'magenta',
                    'edgecolor': 'magenta',
                    'arrowstyle': '->'
                 })
    plt.plot(range(11), [p*2 for p in range(11)], c='m')
    # Pesimistic
    plt.annotate('Too pesimistic',
                 ha='center',
                 va='center',
                 xytext = (8, 3),
                 xy = (8, 5.6),
                 arrowprops = {
                    'facecolor' : 'cyan',
                    'edgecolor': 'cyan',
                    'arrowstyle': '->'
                 })
    plt.plot(range(11), [p*0.7 for p in range(11)], c='c')
    # Better
    plt.annotate('Good enough',
                 ha='center',
                 va='center',
                 xytext = (6, 2),
                 xy = (6, 6),
                 arrowprops = {
                    'facecolor' : 'green',
                    'edgecolor': 'green',
                    'arrowstyle': '->'
                 })
    plt.plot(range(11), range(11), c='g')
    plt.show()

def draw_clusters():
    c1_x = np.random.normal(1, 1, 500)
    c1_y = np.random.normal(8, 1, 500)
    plt.scatter(c1_x, c1_y)
    c2_x = np.random.normal(5, 1, 500)
    c2_y = np.random.normal(6, 1, 500)
    plt.scatter(c2_x, c2_y)
    c3_x = np.random.normal(5, 1, 500)
    c3_y = np.random.normal(10, 1, 500)
    plt.scatter(c3_x, c3_y)
    plt.show()
