from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from customer import views

urlpatterns = {
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/', views.CustomerDetails.as_view()),
    path('codeReference/', views.CodeReferenceList),
    path('codeReference/<int:pk>/', views.CodeReferenceDetails.as_view()),

}

urlpatterns = format_suffix_patterns(urlpatterns)