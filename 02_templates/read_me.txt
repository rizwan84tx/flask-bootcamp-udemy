#### Templates ####
1.  All html template file should be inside a dir 'templates'
2.  App should not be in templates dir
3.  All static file (images) should go under the dir called 'static'
4.  Injecting python variable to HTML file via jinja template tagging {{variable}}
5.  Application syntax
    return render_template('index.html', name=my_name, name_list=name_list, info=info)
6.  Control flow: Using for loops and If..else statements {% <> %}
7.  For loops must be always inside <ul>{% for %}<>{% endfor %}</ul>
8.  Template inheritance
    a.  Inheritting a template into another
    b.  In base HTML
          <BASE DATA>
          {% block content %}
          {% endblock %}
          <BASE DATA>
    c.  Inheritting html
          {% extends 'ibase.html' %}
          {% block content %}
            <NEWDATA>
          {% endblock %}
9.  Link pages/views using 'url_for('view')'
    Example:
      <a href = "{{ url_for('index')}}">Index </a>
      where 'index' is the view in app
10. Linking static images
    Example:
      <a href="{{ url_for('static',filename='riz.jpg')}}">View PIC</a>
      Where 'static' is the folder name
