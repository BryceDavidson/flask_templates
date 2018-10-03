Basic flask app
-------------------------------------------------------------------------------

app.py
------
app.py will start our flask server and serve routes


/templates
------------------
templates will store our html to be referenced from app.py using "render_templates"

/templates/layout.html
---------------------
layout is a defined html "template" to be extended from other html files.
#### SYNTAX:
```
{% block BLOCK_IDENTIFIER %}{% endblock %}
```

templates/includes
-----------------
includes are "partial" snippets of html that do not have to contain head information
and will be referenced by other template files to include those snippets.

#### SYNTAX:
```
{% include 'includes/_somehtml.html' %}
```

flask html syntax
------------
LOGIC:
#### can hold variables, is "dynamic" data within html
```
{%  %}
```
VALUES:
#### for inserting variables
```
{{ object.variable }}
```
