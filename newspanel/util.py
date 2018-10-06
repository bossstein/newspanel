from .models import Article
from .models import Author
from .models import Catagory
from .models import Pub_status
from django.core import serializers

# The following three check if the auther, catagory, and publication status objects exist and creat them is they do not.

def create_default_authors():
    # Test Authors
    if len(Author.objects.order_by()) == 0:
        Author.objects.create("Anne")
        Author.objects.create("Charlie")
        Author.objects.create("Diane")
        Author.objects.create("Bob")
        Author.objects.create("Eric")

def create_default_catagories():
    # Test Catagories
    if len(Catagory.objects.order_by()) == 0:
        Catagory.objects.create("Sport")
        Catagory.objects.create("Art, Music & Entertainment")
        Catagory.objects.create("Poltics")

def create_default_pub_status():
    # Test Catagories
    if len(Catagory.objects.order_by()) == 0:
        Pub_status.objects.create("Draft")
        Pub_status.objects.create("Approved")
        Pub_status.objects.create("Published")
        Pub_status.objects.create("Old")

# returns an XML string containing all of the articles on the DP to populate an app.
def xml_feed():
    return serializers.serialize("xml",Article.objects.all())