# For development use (simple logging, etc):
python3 server.py
# export FLASK_APP=server
# flask run
# For production use: 
# gunicorn server:app -w 1 --log-file -