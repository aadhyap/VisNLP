from flask import Flask,render_template,request
import flask
import json
import word2vec
import pandas as pd

app = Flask(__name__)
data_CBOW = 0
vocabulary = "None"



    




'''def users():

    print("Outputing data to Matrix JSON file")
    with open("matrix.json", "w") as outfile: #handling json file
        #data = json.load(outfile) #reading json file, output list of dictionaries

        d = data_CBOW
   
        json.dump(d, outfile, indent=4)

        #data.append(data_CBOW)

        #response = requests.post(url, data=data.encode())
        return flask.jsonify(d) #sending a valid response, navigate to http://localhost:6969/matrix to see response'''

@app.route("/home")
def home():
   # response.headers['Access-Control-Allow-Origin'] = '*'
    return render_template("cbowNLP.html")

@app.route("/result", methods = ["POST", "GET"])
def result():
    output = request.form.to_dict()
    vocabulary  = output["vocabulary"]
    #should call word2vec send vocabulary
    getoutput()




    return render_template("cbowNLP.html", vocabulary = vocabulary)

@app.route('/matrix', methods=["GET"]) #endpoint folder /...
def getoutput():
        word2vec.start(vocabulary)
        data_CBOW = word2vec.getData()
        print("Outputing data to Matrix JSON file")
        with open("matrix.json", "w") as outfile: #handling json file
            #data = json.load(outfile) #reading json file, output list of dictionaries

            d = data_CBOW
       
            json.dump(d, outfile, indent=4)

            #data.append(data_CBOW)

            #response = requests.post(url, data=data.encode())
            return flask.jsonify(d) #sending a valid response, navigate to http://localhost:6969/matrix to see response

if __name__ == "__main__":
    
    app.run("localhost", 6969)
    #app.run(debug=True)




'''References: 
	- https://tms-dev-blog.com/python-backend-with-javascript-frontend-how-to/

'''