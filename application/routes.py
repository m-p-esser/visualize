"""Routes."""
from flask import render_template
from flask import current_app as app
from .models import Diagrams

@app.route('/')
def index():
   title = "Visualize"
   return render_template(
      "index.html", 
      title=title,
      diagrams=Diagrams.query.all()
      )

@app.route('/about')
def about():
   title = "About"
   return render_template("about.html", title=title)

@app.route('/seaborn')
def seaborn():
   title = "Seaborn"
   return render_template("seaborn.html", title=title)