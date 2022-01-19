from django.urls import path


app_name = 'webapp'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home_view, name='home'),
    path('adicionar utilizador/', views.add_utilizador_view, name='adicionar utilizador'),
    path('adicionar utente/', views.add_pacient_view, name='adicionar Utente'),
    path('adicionar medicamento/', views.add_drug_view, name='add_drug'),
    path('adicionar consulta/', views.add_exam_view, name='add_exam'),
    path('adicionar prescrição/', views.add_prescription_view, name='add_prescription'),
    path('add_appointment/', views.add_appointment_view, name='add_appointment'),
    path('search_user/', views.search_user_view, name='search_user'),
    path('search_pacient/', views.search_pacient_view, name='search_pacient'),
    path('search_drug/', views.search_drug_view, name='search_drug'),
    path('search_appointment/', views.search_appointment_view, name='search_appointment'),
    path('search_prescription/', views.search_prescription_view, name='search_prescription'),
    path('search_exam/', views.search_exam_view, name='search_exam'),
    path('upload_users/', views.upload_users_view, name='upload_users'),
    path('upload_pacients/', views.upload_pacients_view, name='upload_pacients'),
    path('upload_drugs/', views.upload_drugs_view, name='upload_drugs'),
]