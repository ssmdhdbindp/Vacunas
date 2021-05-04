##############################################################################
#                            RUN MAIN                                         #
###############################################################################

from application.dash import app
from settings import config


$ cat runtime.txt
python-3.9.5

app.run_server(debug=config.debug, host=config.host, port=config.port)
