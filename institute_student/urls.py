from django.urls import path
from institute_student import views


urlpatterns = [
    path('home/',views.getstudent),
    path('<int:pk>/',views.StudentDetail.as_view()),
]


#class IngredientCreateView(CreateView):