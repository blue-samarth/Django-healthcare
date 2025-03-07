import os
from secrets import token_urlsafe

class Config:
    """
    This class will handle all the configurations for the application
    """
    __slots__= ['SECRET_KEY', 'DB_NAME', 'DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT', 'DEBUG']

    def __init__(self, size_of_token: int = 32, DB_NAME: str = 'healthcare_db', DB_USER: str ='postgres',
                 DB_HOST: str = 'localhost', DB_PORT: str = '5432', DEBUG: bool = False):
        self.SECRET_KEY = token_urlsafe(size_of_token)
        self.DB_NAME = DB_NAME
        self.DB_USER = DB_USER
        self.DB_PASSWORD = 'password'
        self.DB_HOST = DB_HOST
        self.DB_PORT = DB_PORT
        self.DEBUG = DEBUG
    
    def add_in_env(self):
        """
        This method will create a env file and add the configurations to it
        """
        with open('.env', 'w') as file:
            file.write(f'SECRET_KEY={self.SECRET_KEY}\n')
            file.write(f'DB_NAME={self.DB_NAME}\n')
            file.write(f'DB_USER={self.DB_USER}\n')
            file.write(f'DB_PASSWORD={self.DB_PASSWORD}\n')
            file.write(f'DB_HOST={self.DB_HOST}\n')
            file.write(f'DB_PORT={self.DB_PORT}\n')
            file.write(f'DEBUG={self.DEBUG}\n')

if __name__ == '__main__':
    config = Config()
    config.add_in_env()