
# import ibm_db
# db_config= {
#     'hostname':'ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud',
#     'uid':'kvf99739',
#     'pwd':'P5JLl8PW4eKbIciW',
#     'driver':'{IBM DB2 ODBC DRIVER}',
#     'database':'bludb',
#     "protocol":"TCPIP",
#     'port':'31505'
#     }
# print(db_config)
# try
import ibm_db
dsn_hostname="ea286ace-86c7-4d5b-8580-3fbfa46b1c66.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
dsn_uid="kvf99739"
dsn_pwd="P5JLl8PW4eKbIciW"
dsn_driver="{IBM DB2 ODBC DRIVER}"
dsn_database="bludb"
dsn_port="31505"
dsn_protocol="TCPIP"

dsn={
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
}

print(dsn)