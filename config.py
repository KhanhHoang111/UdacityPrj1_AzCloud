import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'blobprj1'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'hUloykEiRnAcCNAYb1WwNGnfkbGWcLR+Q0lsaItfwzfVbxkW2PXTGXZ6i0WzsmWURC6XkgPSidN9+ASt6ek8Dw=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    SQL_DRIVER = '{ODBC Driver 18 for SQL Server}' 

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'sqlserverprj1.database.windows.net' 
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'SQLdatabase' 
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'azureuser' 
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Kkhanhss#154'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + '/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'

    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://azureuser:Kkhanhss#154@sqlserverprj1.database.windows.net/SQLdatabase?driver=ODBC+Driver+17+for+SQL+Server'


    AUTHORITY = "https://login.microsoftonline.com/f958e84a-92b8-439f-a62d-4f45996b6d07"  # For multi-tenant app, else put tenant name
    
    REDIRECT_PATH = "/auth"
    CLIENT_ID = "4b157fa6-0e67-4173-bba4-579f9d3a19f5"
    CLIENT_SECRET = "~RV8Q~dNlEbc.xFVSVHfXVc4Wvv.ifwkamzZNa5w"

    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
