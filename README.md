Basic flask app
-------------------------------------------------------------------------------

app.py
------
app.py will start our flask server and serve routes defined by us


templates - folder
------------------
templates will store our html to be referenced and served from our app.py routes.

templates - layout.html
---------------------
layout is a defined html "template" to be extended from other html files so as
to write DRY code. To define a referenceable block within a template use flask syntax.
  SYNTAX:
  {% block BLOCK_IDENTIFIER %}{% endblock %}

includes - folder
-----------------
includes are "partial" snippets of html that do not have to contain head information
and will be referenced by other template files to include those snippets.
  SYNTAX:
  """
  {% include 'includes/_somehtml.html' %}
  """
