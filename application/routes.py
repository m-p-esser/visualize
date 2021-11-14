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

@app.route('/<diagram_name>')
def diagram(diagram_name):
   diagram_name_formatted = diagram_name.replace('_', ' ').capitalize()
   return render_template(
      "diagram.html", 
      diagram_name=diagram_name,
      diagram_name_formatted=diagram_name_formatted
      )

# @app.errorhandler(404)
# def not_found():
#     """Page not found."""
#     return make_response(
#         render_template("404.html"),
#         404
#      )


# @app.errorhandler(400)
# def bad_request():
#     """Bad request."""
#     return make_response(
#         render_template("400.html"),
#         400
#     )


# @app.errorhandler(500)
# def server_error():
#     """Internal server error."""
#     return make_response(
#         render_template("500.html"),
#         500
#     )