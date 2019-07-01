#### Templates ####
1.  All html template file should be inside a dir 'templates'
2.  App should not be in templates dir
3.  All static file (images) should go under the dir called 'static'
4.  Injecting python variable to HTML file via jinja template tagging {{variable}}
5.  Application syntax
    return render_template('index.html', name=my_name, name_list=name_list, info=info)
6.  Control flow: Using for loops and If..else statements {% <> %}
7.  For loops must be always inside <ul>{% for %}<>{% endfor %}</ul>
