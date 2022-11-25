import ibm_db

# dsn = {
#     'driver':'{IBM DB2 ODBC DRIVER}',
#     "hostname": "ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud",
#     # "port": "31505",
#     "port":"446",
#     'username':'kvf99739',
#     'password' : 'P5JLl8PW4eKbIciW',
#     'name':'bludb',
    
    
#     }

# db_config_str = f"DATABASE={dsn['name']};HOSTNAME={dsn['hostname']};PORT={dsn['port']};PROTOCOL=TCP/IP;UID={dsn['username']};PWD={dsn['password']};"

conn = None

try:
  print('CONNECTING')
  conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=60000;PROTOCOL=TCPIP;UID=kvf99739;PWD=P5JLl8PW4eKbIciW;","","")
  print('CONNECTED')
except Exception as e:
  print(ibm_db.conn_errormsg())
 
