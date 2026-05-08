# DarkSouls-LoreScraper
A small passion project regarding the lore of the Dark Souls world. Due to much of the series' story being told through item descriptions, I thought it easier to be able to gather and consolidate much of said descriptions into one easily manageable place for lore enthusiasts to interpret at their own discretion.  
5/7/2026 -- All essential features are complete. Any further edits are either fine-tuning the code, trimming the amount of lines, or adding additional feautures.  
And remember, be safe, friends. Don't you dare go Hollow. 🔥

To run the Django REST Framework API, note the following packages:  
```pip install psycopg2-binary``` for connecting to PostgreSQL Databases, or your choice of database  
```pip install django-cors-headers``` to resolve and securely allow the web browser to accept resources served from a different domain  
```pip install djangorestframework``` which installs the entire foundation for this project  
```pip install django-filter``` so that it is easier to query the API by specific fields/values
 
 ... and just a few more for all other necessary libraries:  
 ```pip install bs4``` aka Beautiful Soup 4, a Python library to permit web scraping navigation, such as extracting text, links, images, etc  
 ```pip install aiohttp``` is an asynchronous HTTP framework, mainly used to handle multiple web requests simultaneously for this project  
 ```pip install requests``` should be self-explanatory, in which it was used to utilize the HTTP POST method in regards to the API
 
 Optionally, but preferrably, XAMPP/Apache may be downloaded to host and give the project a more professional feel and experience.  
 It should be noted that doing so -- or not doing so -- would entail modifying the CORS settings in Django's settings.py file.
 
    With XAMPP, add CORS_ALLOWED_HEADERS = ['http://localhost', 'http://127.0.0.1'].
    Otherwise, set CORS_ALLOWED_HEADERS = to True.
