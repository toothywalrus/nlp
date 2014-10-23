import matplotlib.pyplot as plt
import scipy as sp

legend = []

def error(f, x, y):
    return sp.sum((f(x)-y)**2)

def get_data():
    data = sp.genfromtxt("input/web_traffic.tsv", delimiter="\t")

    x = data[:, 0]
    y = data[:, 1]

    x = x[~sp.isnan(y)]
    y = y[~sp.isnan(y)]

    return (x, y,)

def prepare_plot(x, y):
    plt.scatter(x, y)
    plt.title("Web traffic over the last month")
    plt.xlabel("Time")
    plt.ylabel("Hits/hour")
    plt.xticks([w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])
    plt.autoscale(tight=True)
    plt.grid()

def add_func(x, y, degree):
    fp = sp.polyfit(x, y, degree)
    f = sp.poly1d(fp)
    fx = sp.linspace(0, x[-1], 1000)
    plt.plot(fx, f(fx), linewidth=4)
    legend.append("d=%i" % f.order)

x, y = get_data()
prepare_plot(x, y)

# for d in range(100, 101):
#     add_func(x, y, d)

inflection = 3.5 * 7 * 24
xa = x[:inflection]
ya = y[:inflection]
xb = x[inflection:]
yb = y[inflection:]

# fa = sp.poly1d(sp.polyfit(xa, ya, 1))
# fb = sp.poly1d(sp.polyfit(xb, yb, 1))

add_func(xa, ya, 1)
add_func(xb, yb, 1)

plt.legend(legend, loc="upper left")
plt.show()