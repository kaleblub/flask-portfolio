class BaseConfig(object):
	# Learn how to store this key in an environment variable and keep it from being pushed to github
	SECRET_FORM_KEY = "qsdfsyudirnbfguirdjcuhowireymvsnvib7of4rmdxefkwymkzdhinqgmohpowzehlfuixhfwcimlufhxqlzeidmguocnw7erximw8sio34567890plmnbvdsq2345167890plmvc"
	DEBUG = False
	TESTING = False

	SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

class DevelopmentConfig(BaseConfig):
	DEBUG = True
	TESTING = True

class TestingConfig(BaseConfig):
	DEBUG = False
	TESTING = True

class ProductionConfig(BaseConfig):
	SECRET_FORM_KEY = "blahssoudfpaisbdciuapsidbfoaiuhieopwrmkfds_vyauchijcmnfuybawsergrt"
	DEBUG = False
	TESTING = False