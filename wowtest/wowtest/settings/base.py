from unipath import Path

# Full path to django project root.
BASE = Path(__file__).absolute().ancestor(3)

REPO_BASE = BASE.ancestor(1)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
THIRD_PARTY_APPS = (
    'mptt',
    'rest_framework',
    'corsheaders'
)
WOWTEST_APPS = (
    'store',
    'users',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + WOWTEST_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'users.User'

ROOT_URLCONF = 'wowtest.urls'

WSGI_APPLICATION = 'wowtest.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wowtest',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}
