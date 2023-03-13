1. Создаем двух пользователей
us1 = User.objects.create_user(username='Ivanov')
us2 = User.objects.create_user(username='Pushkin')

2. Создаем два объекта модели Author
author1 = Author.objects.create(authorUser=us1)
author2 = Author.objects.create(authorUser=us2)

3. Добавляем 4 категории в модель Category
category1 = Category.objects.create(name='c1')
category2 = Category.objects.create(name='c2')
category3 = Category.objects.create(name='c3')
category4 = Category.objects.create(name='c4')

#author1 = Author.objects.get(id=1)
#author2 = Author.objects.get(id=2)

4. Добавляем 2 статьи и 1 новость
post1 = Post.objects.create(author=author1, categoryType='NW', title='sometitle',text='somebigtext')
post2 = Post.objects.create(author=author2, categoryType='NW', title='sometitle',text='somebigtext')
news = Post.objects.create(author=author1, news=True,title='sometitle',text='somebigtext')

5. Присваиваем им категории
post1 = Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
post2 = Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))

post3 = Post.objects.get(id=2).postCategory.add(Category.objects.get(id=2))
post4 = Post.objects.get(id=1).postCategory.add(Category.objects.get(id=4))

post5 = Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
post6 = Post.objects.get(id=2).postCategory.add(Category.objects.get(id=1))

6. Создаем 4 комментария к разным объектам модели Post
comment1 = Comment.objects.create(commentUser=Author.objects.get(id=1).authorUser, commentPost=Post.objects.get(id=1),text='somebigtext')
comment2 = Comment.objects.create(commentUser=Author.objects.get(id=2).authorUser, commentPost=Post.objects.get(id=2),text='somebigtext')
comment3 = Comment.objects.create(commentUser=Author.objects.get(id=1).authorUser, commentPost=Post.objects.get(id=1),text='somebigtext')
comment4 = Comment.objects.create(commentUser=Author.objects.get(id=1).authorUser, commentPost=Post.objects.get(id=2),text='somebigtext')

7. Применяем функции like() и dislike()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).dislike()
Comment.objects.get(id=3).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).dislike()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=2).dislike()

7/1 Проверяем рейтинг
Comment.objects.get(id=1).rating
Comment.objects.get(id=2).rating
Comment.objects.get(id=3).rating
Comment.objects.get(id=4).rating
Post.objects.get(id=1).rating
Post.objects.get(id=2).rating

8. Обновуляем рейтинги пользователей
author1 = Author.objects.get(id=1)
author1.update_rating()
author1.ratingAuthor

author2 = Author.objects.get(id=2)
author2.update_rating()
author2.ratingAuthor

9. Выводим username и рейтинг лучшего пользователя
a = Author.objects.order_by('-ratingAuthor')[:1]


10. Выводиь дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье
Post.objects.order_by('-rating').values('dateCreation', 'author__authorUser__username', 'rating', 'title')[0]
Post.objects.order_by('-rating')[0].preview()