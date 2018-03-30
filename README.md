# Bookmarks Web App

Created by following the Udemy tutorial by Packt called [Modern Web Development with Django](https://www.udemy.com/learning-path-django-modern-web-development-with-django/learn/v4/overview).

## Features

This app includes the following features:

- Registration and User Profiles
- Social Authentication using social-auth-app-django
- Ability to bookmark and save images from other websites
- Use of thumbnails to display images
- Ability to "like" and "dislike" items
- Pagination via delayed loading using AJAX
- Ability to "follow" other users
- An Activity Stream to track what other users are doing.
- Improved query performance by de-normalizing data (making it redundant) and updating the redundant data using Django signals.
- Storing and Ranking items using Redis


## Requirements

This Bookmarks app is built with:

- Django 2.0.3
- Pillow
- [Python Social Auth](https://python-social-auth.readthedocs.io/en/latest/)
- [sorl-thumbnail](https://sorl-thumbnail.readthedocs.io/en/latest/#)
- [Redis](https://redis.io/) and [Redis-py](https://redis-py.readthedocs.io/en/latest/)


## Notes

### Redis
To start the Redis server, from the c:\program files\redis directory, type:

    C:\Program Files\Redis> redis-server.exe redis.windows.conf

To use the Redis CLI, open another terminal and type:

    C:\Program Files\Redis> redis-cli.exe

