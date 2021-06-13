from lab.html_views import *

from user.html_views import *

app.add_url_rule('/', 'home', home)
app.add_url_rule('/doctor-login', 'doctor-login', doctor_login)


app.run()