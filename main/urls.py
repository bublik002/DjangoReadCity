from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.cache import cache_page
from .views import *
from rest_framework import routers
from django.conf.urls import handler404
from django.contrib.auth.urls import *
from django.conf import settings
from django.conf.urls.static import static

router = routers.SimpleRouter()

urlpatterns = [
    path('', HomePageView.as_view(template_name='main.html'), name='home'),
    path('add', FillingModel),
    path('library/<slug:book>', LibraryView.as_view(), name='library'),
    path('bookmark/<int:id>', BookMarks),
    path('basket/<int:book>', Basket),
    path('registration', RegistrationView.as_view(), name='reg_url'),
    # path('registration/email', BasePage.as_view(template_name='main.html'), name='reg_url'),
    path('login', AuthorizationView.as_view(), name='login_url'),
    path('logout', Logout, name='login_url'),
    path('bookmarks', BookmarksView.as_view(template_name='bookmarks.html'), name='bookmarks'),
    path('basket', BasketView.as_view(template_name='Basket.html'), name='bookmarks'),
    path('book/<int:id>', BookView.as_view(), name='book'),
    path('search', SearchBookView.as_view(), name='search'),
    path('api', HomePageView.as_view(template_name='drf_doc.html'), name='api'),
    path('create-entry', CreateBooksView.as_view(), name='create_entry'),

    # path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/book_list/category/<str:cat>', BooksApiListCategoryView.as_view()),
    path('api/v1/book_list/id/<int:id>', BooksApiListIDView.as_view()),
    path('api/v1/book_list/', BooksApiListAllView.as_view()),

    path('api/v1/book_destroy/<int:id>', BooksDestroyView.as_view()),

    path('api/v1/book_update/<int:id>', BooksApiUpdateView.as_view()),

    path('api/v1/book_create/', BooksCreateAPIView.as_view()),

    path('api/v1/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

