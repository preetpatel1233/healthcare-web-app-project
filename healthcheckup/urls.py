from django.contrib import admin
from django.urls import path
from healthcheckup import myview
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",myview.homepage,name='home'),
    path('bmi/', myview.bmi_page,name='bmi'),
    path('Diet/', myview.Diet_page,name='Diet'),
    path('Workout/', myview.workout_page,name='Workout'),
    path('aboutus', myview.aboutme,name='about'),
]
