from rest_framework.response import Response
from rest_framework.views import APIView

from celery_app.celery_tasks.sentry_tasks import task_test_sentry


# Create your views here.

class SimpleView(APIView):
    def get(self, request):
        task_test_sentry.delay()
        return Response({"status": "ok"})
