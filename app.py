from flask import Flask, render_template
from database import load_jobs

app = Flask(__name__)

@app.route("/")
def hello_world():
  jobs = load_jobs()
  return render_template('home.html', job = jobs)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)