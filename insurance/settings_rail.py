from insurance.settings import*
from decouple import config

SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = ['*'] 
DEBUG = config('DEBUG', default=False, cast=bool)

