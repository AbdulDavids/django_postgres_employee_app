# gunicorn_config.py

bind = "0.0.0.0:8000"  # IP and port to bind to
workers = 3  # Number of worker processes
timeout = 120  # Worker timeout in seconds
