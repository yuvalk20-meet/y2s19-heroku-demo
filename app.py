from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/icecream', methods=['GET', 'POST'])
def home_page():
    if request.method == 'GET':
    	return render_template("index.html") 
    else:
    	flavor = request.form['flavor']
    	return render_template("icecreammaker.html", flavor = flavor)
       

if __name__ == '__main__':
   app.run(debug = True)
