from flask import Flask
import celeryTask
from RedisQueue import RedisQueue


flask_app = Flask(__name__)

# Example URL to stop the current celery task
@flask_app.route("/terminate",methods=['GET'])
def rfGetVersions():
	result.revoke(terminate=True)
	return("Celery task Terminated")


# Create a redis queue, which sits on redis server.
q = RedisQueue('test')
q.put('Task 1')
q.put('Task 2')
q.put('Task 3')
q.put('Task 4')


print ("Celery background tasks starting.....")

# This is actually calling a celery thread and asssiging it a task 'basic_celery_task'
# By using .delay() method we are actually saying it execute in background, so that the flask can serve web URIs.
result = celeryTask.basic_celery_task.delay()
print ("Started!")

flask_app.run(host="127.0.0.1",port=5001, threaded=True)