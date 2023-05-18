# FigmaAPI-Django requirement


testserver/base/views.py requires FigmaAPI token, ids and file_id which you can find at your Figma account.
Also change the django secret key to yours in testserver/testserver/settings.py.
# What does it do
Your figma project will get render at testserver/templates/home.html. To start write at terminal python manage.py runserver.
