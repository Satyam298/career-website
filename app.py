from flask import Flask, render_template, jsonify, request, url_for, redirect
from database import load_jobs, load_job_id, add_application_to_db

app = Flask(__name__)

@app.route("/")
def list_job():
  jobs = load_jobs()
  return render_template('home.html', job = jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_id(id)
  if not job:
    return "Not Found", 404
  return render_template('jobinfo.html', job=job)

@app.route('/job/<id>/apply', methods=['post'])
def submit_application(id):
    data = request.form
  
    job = load_job_id(id)
    add_application_to_db(id,data)
    # return redirect(url_for('list_job'))
    return '''<script>
       alert("Application Submitted");
       window.location.href = '{}';
    </script>'''.format(url_for('list_job'))
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)  