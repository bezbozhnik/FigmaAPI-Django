# FigmaAPI-Django requirement


testserver/base/views.py requires FigmaAPI token, ids and file_id which you can find at your Figma account.
Also change the django secret key to yours in testserver/testserver/settings.py.
# What does it do
Your figma project will get rendered at testserver/templates/home.html . To get started, write python in the terminal "python manage.py runserver" start the server.
