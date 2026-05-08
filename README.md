# DarkSouls-LoreScraper
A small passion project regarding the lore of the Dark Souls world. Due to much of the series' story being told through item descriptions, I thought it easier to be able to gather and consolidate much of said descriptions into one easily manageable place for lore enthusiasts to interpret at their own discretion. Work in progress.

To run the Django REST Framework API, note the following packages:
'psycopg2-binary' for connecting to PostgreSQL Databases, or your choice of database
'django-cors-headers' to resolve and securely allow the web browser to accept resources served from a different domain
'djangorestframework' which installs the entire foundation for this project
'django-filter' so that it is easier to query the API by specific fields/values
 
 ... and just a few more for all other necessary libraries:
 'bs4' aka Beautiful Soul 4, a Python library to permit web scraping navigation, such as extracting text, links, images, etc
 'aiohttp' is an asynchronous HTTP framework, mainly used to handle multiple web requests simultaneously for this project
 'requests' should be self-explanatory, in which it was used to utilize the HTTP POST method in regards to the API
 

 Optionally, but preferrably, XAMPP/Apache may be downloaded to host and give the project a more professional feel and experience.
 It should be noted that doing so -- or not doing so -- would entail modifying the CORS settings in Django's settings.py file.
    With XAMPP, add CORS_ALLOWED_HEADERS = ['http://localhost', 'http://127.0.0.1'].
    Otherwise, set the field equal to True.
