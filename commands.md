tp1.delay()
tp2.delay()
tp3.delay()
tp0.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp0.delay()
tp1.delay()
tp2.delay()
tp3.delay()
tp0.delay()

t = group(tp0.s(), tp1.s(), tp2.s(), tp3.s())
t()

c = chain(tp3.s(), tp1.s(), tp2.s(), tp0.s())
c()

from newapp.tasks import *
from celery import chain

python manage.py shell

---------

# remove all containers and imaages then build them again
docker-compose down --rmi all && docker-compose up --build

----------
from celery_app.celery import *
t1.apply_async((1,),priority=2)
t2.apply_async((1,),priority=5)
t3.apply_async((1,),priority=9)
t1.apply_async((1,),priority=2)
t2.apply_async((1,),priority=5)
t3.apply_async((1,),priority=9)


celery inspect active_queues
celery inspect active

----------------
