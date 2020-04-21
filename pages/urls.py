from .views import (home_view,
                    )
from django.urls import path

app_name = 'pages'
urlpatterns= [
    path('', home_view, name = 'home'),
]