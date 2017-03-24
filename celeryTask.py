from celery import Celery
import time
from RedisQueue import RedisQueue

app = Celery('myapp')

# setting the celery backend broker details
app.conf.update(BROKER_URL='redis://localhost:6379',
                CELERY_RESULT_BACKEND='redis://localhost:6379')

# Getting the redis queue.
q = RedisQueue('test')

# This task gets input from the queue and calls other task which actually does a job.
# For our convienence the queue elements are not deleted at any point of time.
# The only way to stop this task is by calling .revoke() method or manually killing this task.
@app.task(bind=True)
def basic_celery_task(self):
    #time.sleep(5)
    self.job = call_within_call.delay(str(q.get() ) )
    print (self.job.get())
    
    # Loops infite to get the next element in the queue and calls other task
    while True:
        if self.job.state == 'SUCCESS':
            self.job = call_within_call.delay(str(q.get()))
            print (self.job.get() )
    return 'True'


# This task accepts input from basic_celery_task and works on it.
@app.task(bind=True)
def call_within_call(self,arg):
    # call the MC with URI
    time.sleep(5)
    return arg + 'Completed'