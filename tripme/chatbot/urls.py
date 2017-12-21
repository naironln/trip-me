from django.conf.urls import include, url
from .views import TripmeBotView

app_name = "tripme"
urlpatterns = [
	url('^tripme/?$', TripmeBotView.as_view(), name='tripme')
]