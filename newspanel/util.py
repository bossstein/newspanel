from .models import Article
from .models import Author
from .models import Category
from .models import Pub_status
from django.core import serializers

# The following three check if the auther, category, and publication status objects exist and create them. This needs to be updated for a production like enviroment. I need a datadump of defaut static objects for pub_status and catagories.
def create_default_authors():
    # Test Authors
    if len(Author.objects.order_by()) == 0:
        Author.objects.create("Anne")
        Author.objects.create("Charlie")
        Author.objects.create("Diane")
        Author.objects.create("Bob")
        Author.objects.create("Eric")

def create_default_categories():
    # Test Categories
    if len(Category.objects.order_by()) == 0:
        Category.objects.create("Sport")
        Category.objects.create("Art, Music & Entertainment")
        Category.objects.create("Poltics")

def create_default_pub_status():
    # Test Pub_status
    if len(Pub_status.objects.order_by()) == 0:
        Pub_status.objects.create("Draft")
        Pub_status.objects.create("Approved")
        Pub_status.objects.create("Published")
        Pub_status.objects.create("Old")

# returns an XML string containing all of the articles on the DP to populate an app.
def xml_feed():
    return serializers.serialize("xml",Article.objects.all())