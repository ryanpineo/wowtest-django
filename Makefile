SHELL := /bin/sh

REPOPATH := $(CURDIR)
LOCALPATH := $(REPOPATH)/wowtest
PYTHONPATH := $(LOCALPATH)
PYTHON_BIN := $(VIRTUAL_ENV)/bin

PROJECT := wowtest
SETTINGS := devel
TEST_SETTINGS := test

DJANGO_SETTINGS_MODULE := $(PROJECT).settings.$(SETTINGS)
DJANGO_TEST_SETTINGS_MODULE := $(PROJECT).settings.$(TEST_SETTINGS)


runserver:
	$(LOCALPATH)/manage.py runserver --settings=$(DJANGO_SETTINGS_MODULE) --pythonpath=$(PYTHONPATH)

test:
	$(LOCALPATH)/manage.py test $(APP) --settings=$(DJANGO_TEST_SETTINGS_MODULE) --pythonpath=$(PYTHONPATH)
