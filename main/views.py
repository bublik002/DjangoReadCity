import random
from django.core.paginator import Paginator
from rest_framework import generics
from django.forms import model_to_dict
from django.shortcuts import render
from django.views.generic import FormView, ListView
import json
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic.base import TemplateView
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from .forms import LoginUserForm, CreateUserForm
from .add_scripts import Validation
from django.shortcuts import redirect
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


# Чтение и создание записей
class BookApiCreateView(ListCreateAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer


# Обновление записей
class BookApiUpdateView(UpdateAPIView):
    queryset = BooksModel.objects.all()
    serializer_class = BookSerializer


# Чтение и создание записей
class CategoryApiCreateView(ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


# Обновление записей
class CategoryApiUpdateView(UpdateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


# Чтение, изменение и добавление отдельной записи (get, put, patch, delete)
class BookAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = BooksModel
    serializer_class = BookSerializer


# Чтение, изменение и добавление отдельной записи (get, put, patch, delete)
class CategoryAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel
    serializer_class = CategorySerializer

# class BookApiView(APIView):
#     def get(self, requests):
#         lst = BooksModel.objects.all()
#         return Response({'get': BookSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "method PUT not allowed"})
#
#         try:
#             instance = CategoryModel.objects.get(pk=pk)
#         except Exception:
#             return Response({'error': 'Objects does not exist'})
#
#         serializer = CategorySerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "method PUT not allowed"})
#
#         try:
#             instance = CategoryModel.objects.get(pk=pk)
#             instance.delete()
#         except Exception:
#             return Response({'error': 'Objects does not exist'})
#
#         return Response({"post": f"Object {str(pk)} is deleted"})


# class BookApiView(generics.ListAPIView):
#     queryset = BooksModel.objects.all()
#     serializer_class = BookSerializer


def FillingModel(request):
    file = open('C:/Users/user/Desktop/projects/ReadCity/main/parsing/book_json.jsonlines', 'r',
                encoding="utf-8").read().split('\n')
    categorymodel = CategoryModel.objects.all()
    booksmodel = BooksModel.objects.all()
    for book_ in file:
        book = json.loads(book_).items()
        try:
            for k, v in book:

                if len(categorymodel.filter(subcategory1=v['subcategory1'],
                                            subcategory2=v['subcategory2'])) == 0:
                    categorymodel.create(subcategory1=v['subcategory1'],
                                         subcategory2=v['subcategory2'])

                category = categorymodel.filter(subcategory1=v['subcategory1'],
                                                subcategory2=v['subcategory2'])

                print('категории ', v['subcategory1'], v['subcategory2'])
                if len(booksmodel.filter(title=v['title'], img=v['img'])) == 0:

                    price = int(''.join([i for i in v['price'] if i in '0123456789']))
                    booksmodel_created = booksmodel.create(title=v['title'], img=v['img'], price=price,
                                                           info_txt=v['description'], author=v['author'])

                    booksmodel_created.category.set(category)

                    booksmodel_created.id_book = v['chars']['ID товара']
                    try:
                        booksmodel_created.ISBN = v['chars']['ISBN']
                    except:
                        booksmodel_created.ISBN = ""
                    booksmodel_created.year_of_publishing = v['chars']['Год издания']
                    booksmodel_created.num_page = v['chars']['Количество страниц']
                    booksmodel_created.size = v['chars']['Размер']

                    booksmodel_created.weight = v['chars']['Вес, г']
                    print(v['chars']['Издательство'])
                    booksmodel_created.publishing_house = v['chars']['Издательство']

                    if 'Возрастные ограничения' in v['chars']:
                        booksmodel_created.age_rest = v['chars']['Возрастные ограничения'][:-1]
                    if 'Тип обложки' in v['chars']:
                        booksmodel_created.cover_type = v['chars']['Тип обложки']

                    if 'Издательский бренд' in v['chars']:
                        booksmodel_created.publishing_brand = v['chars']['Издательский бренд']

                    if 'Серия' in v['chars']:
                        booksmodel_created.series = v['chars']['Серия']

                    if 'Тираж' in v['chars']:
                        booksmodel_created.circulation = v['chars']['Тираж']

                    booksmodel_created.save()
        except:
            pass

    return redirect('/')


class MenuView(TemplateView):
    def get_context_data(self, **kwargs):
        print(self.request.GET)
        context = super().get_context_data(**kwargs)
        sub = {}

        for cat in CategoryModel.objects.all():
            sub[cat.subcategory1] = cat.sub_slugify1

        context['cat'] = sub

        return context


class HomePageView(ListView):
    model = BooksModel

    def get_queryset(self):
        ran = random.randint(0, len(BooksModel.objects.all()) - 6)

        return self.model.objects.all()[ran:ran + 6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sub = {}

        for cat in CategoryModel.objects.all():
            sub[cat.subcategory1] = cat.sub_slugify1

        context['cat'] = sub

        if not self.request.user.is_anonymous:
            context['viewed'] = User.objects.get(email=self.request.user).viewed.all()[:6]
            print(User.objects.get(email=self.request.user).viewed.all())
        else:
            context['viewed'] = None
        return context


class BookmarksView(ListView):
    model = User

    def get_queryset(self):
        self.get_user = self.model.objects.get(email=self.request.user.email)
        return self.get_user.bookmarks.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["num_books"] = len(self.bookmarks_profile)

        numbers_products = len(self.get_user.bookmarks.all())
        if numbers_products == 1:
            end_numbers_products = " товар"
        elif (4 >= numbers_products % 10 >= 2) and not (10 < numbers_products < 20):
            end_numbers_products = " товара"
        else:
            end_numbers_products = " товаров"
        context["num_books"] = str(numbers_products) + end_numbers_products
        return context


class BookView(ListView):
    template_name = 'book.html'
    model = BooksModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        get_book = self.model.objects.get(slug_title=self.kwargs['book'])
        sub = {}

        if not self.request.user.is_anonymous:
            User.objects.get(email=self.request.user).viewed.add(get_book)

        for cat in CategoryModel.objects.all():
            sub[cat.subcategory1] = cat.sub_slugify1

        context['cat'] = sub
        context['book'] = get_book

        property_book1 = {
            "Переводчик": get_book.interpreter,
            "ID": get_book.id_book,
            "Издательство": get_book.publishing_house,
            "Серия": get_book.series,
            "Год публикации": get_book.year_of_publishing,

        }
        property_book2 = {
            "ISBN": get_book.ISBN,
            "Количество страниц": get_book.num_page,
            "Размер": get_book.size,
            "Тип обложки": get_book.cover_type,
            "Тираж": get_book.circulation,
            "Вес": get_book.weight,
            "Возрастное ограничение": get_book.age_rest,
        }
        context['property_book1'] = property_book1
        context['property_book2'] = [property_book1, property_book2]
        context['reviews'] = get_book.review.all()
        return context

    def get_queryset(self):
        ran = random.randint(0, len(self.model.objects.all()) - 18)

        return [
            self.model.objects.all()[ran:ran + 6],
            self.model.objects.all()[ran + 6: ran + 6 * 2],
            self.model.objects.all()[ran + 6 * 2: ran + 6 * 3],
        ]


class AuthorizationView(LoginView, MenuView):
    form_class = LoginUserForm

    def get_success_url(self):
        return reverse('home')


def Logout(request):
    logout(request)
    return redirect('/')


class LibraryView(ListView):
    model = BooksModel
    template_name = "library.html"
    paginate_by = 16
    def get_queryset(self):
        category = CategoryModel.objects.filter(sub_slugify1=self.kwargs['book'])

        if len(category) == 0:
            category = CategoryModel.objects.all()

        return BooksModel.objects.filter(category__in=category)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.kwargs['book'] != 'all':
            context['category'] = CategoryModel.objects.filter(sub_slugify1=self.kwargs['book'])[0].subcategory1
        else:
            context['category'] = 'Все книги'

        category_dict = {}
        for cat in CategoryModel.objects.all():
            category_dict[cat.subcategory1] = cat.sub_slugify1

        context['cat'] = category_dict
        return context


def BookMarks(request, **kwargs):
    book_add = BooksModel.objects.get(slug_title=kwargs['book'])
    user = User.objects.get(email=request.user.email)
    if book_add not in user.bookmarks.all():
        user.bookmarks.add(book_add)
    else:
        user.bookmarks.remove(book_add)
    return redirect('/')


def Basket(request, **kwargs):
    book_add = BooksModel.objects.get(slug_title=kwargs['book'])
    user = User.objects.get(email=request.user.email)
    if book_add not in user.basket.all():
        user.basket.add(book_add)
    else:
        user.basket.remove(book_add)
    return redirect('/')


class SearchBookView(ListView):
    model = BooksModel
    template_name = "library.html"

    def get_queryset(self):
        s = self.request.GET.get('s')
        data = []
        book = self.model.objects.filter(title__icontains=s)
        author = self.model.objects.filter(author__contains=s)
        category1 = CategoryModel.objects.filter(subcategory1__icontains=s)
        category2 = CategoryModel.objects.filter(subcategory2__icontains=s)

        for model in [book, author]:
            for object in model:
                data.append(object)

        for object in category1:
            for element in self.model.objects.filter(category=object):
                data.append(element)

        for object in category2:
            for element in self.model.objects.filter(category=object):
                data.append(element)
        return data


class BasketView(ListView):
    model = User

    def get_queryset(self):
        self.get_user = self.model.objects.get(email=self.request.user.email)
        return self.get_user.basket.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["num_books"] = len(self.bookmarks_profile)

        numbers_products = len(self.get_user.basket.all())
        if numbers_products == 1:
            end_numbers_products = " товар"
        elif (4 >= numbers_products % 10 >= 2) and not (10 < numbers_products < 20):
            end_numbers_products = " товара"
        else:
            end_numbers_products = " товаров"
        context["num_books"] = str(numbers_products) + end_numbers_products
        return context


class RegistrationView(FormView, MenuView):
    form_class = CreateUserForm
    template_name = 'registration/registration.html'
    success_url = '/'

    def EmailConfirmation(self):
        pass

    def form_valid(self, form):
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        phone_number = form.cleaned_data['phone_number']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        data_entry = form.cleaned_data['data_entry']

        valid = Validation(email, first_name, last_name, phone_number, password1, password2, data_entry)

        if len(valid) > 0:
            for error in valid:
                form.add_error(error[0], error[1])
                return self.form_invalid(form)

        user = form.save()

        # user.is_active = False
        user.save()

        return super(RegistrationView, self).form_valid(form)





def page_not_found_view(request, exception):
    return render(request, 'error.html', status=404)