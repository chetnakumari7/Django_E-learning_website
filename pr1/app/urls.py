from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.a2, name='a2'),
    path('', views.a2, name=''),

    path('Signin/', views.Signin,name='signin'),path('login/',views.login1,name='login'),
    path('login_signup/', views.login_signup,name='login_signup'),path('courses/',views.Courses,name='courses'),
    path('contactus/', views.contact,name='contact'),
    path('course1/',views.courses_1,name='courses_1'),
    path('course2/',views.courses_2,name='courses_2'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('course/<str:cname>/<int:cid>',views.course_details,name='course_details'),
    path('courseupsc/<str:gname>/<int:gid>',views.govt_details,name='govt_details'),
    path('schoolcourse/<str:sname>/<int:sid>',views.school_details,name='school_details'),
    path('teachus/',views.teach_us,name='teach'),
    path('search/',views.search, name='search'),
    path('logout/',views.logoutUser,name="logout"),
    path('hcourse/<str:hname>/<int:hid>', views.home_details, name='hdetails')
    
     

    ]
    # Add more URL patterns as needed