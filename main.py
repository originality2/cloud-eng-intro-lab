from flask import Flask
from flask import render_template
import os 
from flask import send_from_directory 
import operator
app = Flask(__name__)


def reset_results():
    return {"Jermaine":0, "Brett":0, "Mel":0, "Murray":0}

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/<direction>')
def play(direction):
    global question
    global total_qs
    global results
    global mapping
    if direction != "start":
        question += 1
        results[direction] += 1
    if question <= total_qs:
        my_file = open("./templates/content/" + str(question) + ".txt", "r")
        lines = my_file.readlines()
        heading = ""
        choices = []
        image_path = "static/images/buzzfeedarrow.png"

        for line in lines:
            line = line.strip("\n")
            line = line.split(",")
            print(line)
            if line[0] == "heading":
                heading = line[1]
            elif line[0] == "choice":
                tmp = [line[1], line[2]]
                choices.append(tmp)
            elif line[0] == "image":
                image_path = line[1]

        return render_template('play.py', heading=heading, 
        image_path=image_path, choices=choices)
    else:
        result = max(results.iteritems(), key=operator.itemgetter(1))[0]
        my_file = open("./templates/content/" + str(result) + ".txt", "r")
        lines = my_file.readlines()
        heading = ""
        result = ""
        image_path = "static/images/buzzfeedarrow.png"

        for line in lines:
            line = line.strip("\n")
            line = line.split(",")
            if line[0] == "heading":
                heading = line[1]
            elif line[0] == "result":
                result = line[1]
            elif line[0] == "image":
                image_path = line[1]
        results = reset_results()
        question = 1
        return render_template('end.py', heading=heading, 
        image_path=image_path, result=result)

question = 1
total_qs = 4
results = reset_results()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')