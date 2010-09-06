DEBUG = TEMPLATE_DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/intellipages.db',
    }
}
INSTALLED_APPS = ['intellipages']