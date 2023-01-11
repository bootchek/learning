import multiprocessing

bind = "0.0.0.0:8000"
workers = 3
# Access log - records incoming HTTP requests
accesslog = "gunicorn.access.log"
# Error log - records Gunicorn server goings-on
errorlog = "gunicorn.error.log"
# How verbose the Gunicorn error logs should be
# loglevel = "info"