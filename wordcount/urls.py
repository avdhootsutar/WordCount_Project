from django.urls import path
from . import views
urlpatterns = [
          path('',views.homepage),
          path('countthis/',views.countpage, name='count'),
]
