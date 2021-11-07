
'''--- The Base Configuration Class ---'''
class BaseConfig(object):
	# Learn how to store this key in an environment variable and keep it from being pushed to github
	SECRET_FORM_KEY = "qsdfsyudirnbfguirdjcuhowireymvsnvib7of4rmdxefkwymkzdhinqgmohpowzehlfuixhfwcimlufhxqlzeidmguocnw7erximw8sio34567890plmnbvdsq2345167890plmvc"
	DEBUG = False
	TESTING = False

	# Map scss source files to css destination file
	sassMap = {"./static/scss/app.scss": "./static/css/main.css"}


'''--- The Development Configuration Class ---'''
class DevelopmentConfig(BaseConfig):
	DEBUG = True
	TESTING = True


'''--- The Testing Configuration Class ---'''
class TestingConfig(BaseConfig):
	DEBUG = False
	TESTING = True


'''--- The Production Configuration Class ---'''
class ProductionConfig(BaseConfig):
	SECRET_FORM_KEY = "blahssoudfpaisbdciuapsidbfoaiuhieopwrmkfds_vyauchijcmnfuybawsergrt"
	DEBUG = False
	TESTING = False