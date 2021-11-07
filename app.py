''' Import The Function That Creates The App '''
from __init__ import create_app

''' If This File Is Run '''
if __name__ == "__main__":

	# Run The App On Localhost On Port 8000
	app = create_app().run(host='127.0.0.1', port=8000)