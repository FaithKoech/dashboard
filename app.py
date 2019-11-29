from flask import Flask, render_template
import pygal

app = Flask(__name__)


@app.route('/')
def hello_world():
    x = 1000
    return render_template("My4thwebsite.html",x=x)

@app.route('/About')
def About_page():
    return render_template("About.html")

@app.route('/xyz')
def piechart():
    ratios = [("Gentlement", 5), ("Ladies", 9)]
    pie_chart = pygal.Pie()
    pie_chart.title = 'Browser usage in February 2012 (in %)'
    pie_chart.add(ratios[0][0], ratios[0][1])
    pie_chart.add(ratios[1][0], ratios[1][1])
    # pie_chart.add('Chrome', 36.3)
    # pie_chart.add('Safari', 4.5)
    # pie_chart.add('Opera', 2.3)
    pie_data = pie_chart.render_data_uri()

    graph = pygal.Line()
    graph.title = '% Change Coolness of programming languages over time.'

    graph.Month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    graph.add('Python', [22, 27, 23, 20, 12, 32])
    # graph.add('Java', [15, 45, 76, 80, 91, 95])
    # graph.add('C++', [5, 51, 54, 102, 150, 201])
    # graph.add('All others combined!', [5, 15, 21, 55, 92, 105])
    graph_data = graph.render_data_uri()

    return render_template('dashboard.html', pie_data = pie_data, graph_data = graph_data)




if __name__ == '__main__':
    app.run()
