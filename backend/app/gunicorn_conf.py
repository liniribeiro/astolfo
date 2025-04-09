import multiprocessing

# FastAPI app location
wsgi_app = "main:app"

# Server socket
bind = "0.0.0.0:8000"

# Workers configuration
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Timeouts
timeout = 30
graceful_timeout = 30

# PID file (optional)
# pidfile = "gunicorn.pid"

# Max requests per worker (to prevent memory leaks)
max_requests = 1000
max_requests_jitter = 50