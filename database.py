import sqlalchemy
from sqlalchemy import create_engine, text
import os
db_connection_string = os.environ['DB_CONNECTION_STRING']                            
engine = create_engine(
  db_connection_string,
  connect_args={
  "ssl": {  
      "ssl_ca": "/etc/ssl/cert.pem"
      
  }
  })
with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))

def load_jobs():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

  jobs = []

  result_all = result.all()
  jobs = [row._asdict() for row in result_all]
  return jobs  