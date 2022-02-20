from django.urls import path,include
from . import views
urlpatterns = [
    path('account/', views.AccountView.as_view()),
    path('account/<int:id>', views.AccountDetail.as_view()),
    path('driver/', views.DriverView.as_view()),
    path('driver/<int:id>', views.DriverDetail.as_view()),
    path('posting/', views.PostingView.as_view()),
    path('posting/<int:id>', views.PostingDetail.as_view()),
    path('report/', views.ReportView.as_view()),
    path('report/<int:id>', views.ReportDetail.as_view()),
    path('passenger/', views.PostingPassengerView.as_view()),
    path('passenger/<int:num>', views.PostingPassengerDetail.as_view()),
    path('passenger/<int:num>$<int:id>', views.PostingPassengerDetailBeta.as_view())
]