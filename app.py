from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
  'id':1,
  'title' : 'Data Scientist',
  'Salary' : 'Rs. 12,000,000'
  },
  {
  'id':2,
  'title' : 'Data Analyst',
  'Salary' : 'Rs. 8,000,000'
  },
{
  'id':3,
  'title' : 'Data Engineer',
  'Salary' : 'Rs. 15,000,000'
  }
]

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

@app.route("/")
def hellow_redgerd():
  return render_template('home.html',jobs=JOBS,company_name='Redgerd')

print(__name__)
if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)
  