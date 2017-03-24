# celery-flask-POC
> Basic Flask Celery application which runs serialized backrground tasks with help of Redis server as Backend.
>
> To run this application, following are pre-requisites
>
+ python 3.4.xx
+ flask (pip install flask)
+ celery (pip install celery=3.1.25)
    - If you are working on windows, kindly install celery=3.1.25 . 3.1.25 works fine for all OS.
+ redis server
   - If using other than windows follow this documentation https://redis.io/download#installation
   - If using windows, the redis server is in this repo. Open the Directory 'Redis-x64-3.2.100' and execute 'redis-server.exe'
   - This will start redis server. It will be serving on localhost:6379
    
+ We need to run redis server and celery worker (in that order) before we run our main application.
  - First we open a terminal and run
    - `celery -A celeryTask:app worker --loglevel=info`
    - Celery makes sure that redis server is running and then starts a worker for the task 'celeryTask'
    
+ After celery is running its worker we open another terminal and run `python main.py`
  - This will start the flask application and triggers 'celeryTask' as a background task.
  - If we need to kill or stop the current celerytask, visit `http://127.0.0.1:5001:/terminate` . 
  - This URI call is basically supposed to kill the current celery task.
  - Celery is very fundamental in nature. Lots of options to schedule, stop, pause, resume, wait, kill, terminate...
  
  
+ In background, celery is reading task info from a redis simple queue which is served from `redis@localhost:6379`.
  - `RedisQueue.py` is the file which creates a simple program to create a simple redis queue.
  - It is a simple queue(FIFO). Redis server has the capacity to remember the last read element.
      - It does not effect if we stop redis server, stop celery task worker or stop flask abruptly. Redis is stateful.
      

------------------------------------------------------------------------------------------------------------------------
  
  
  
# Goal
> Goal is to schedule actual MC URL calls with celery workers. 
> We can store the MC URL information in redis queue so that celery workers collect them as soon as they finish their previous jobs.


