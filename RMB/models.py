from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
import datetime
from allauth.socialaccount.models import SocialAccount
import hashlib

try:
    from django.utils.timezone import now
except ImportError:
    now = datetime.now
	
# UserProfile table extending User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    name = models.CharField(max_length=40, blank=True)
    surname = models.CharField(max_length=70, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    last_login = models.DateTimeField(auto_now_add=True)
    # This line is required. Links UserProfile to a User model instance.
    def __unicode__(self):
        return self.user.username

    class Meta:
        db_table = 'user_profile'
    #if account if verified return email addresses
    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False
 
	User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
    # Override the __unicode__() method to return out something meaningful!
#
def profile_image_url(self):
    fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')
 
    if len(fb_uid):
        return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)
        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())
		
# Categories model included category names
class Categories(models.Model):
    cat_descr = models.CharField(max_length =120, blank=False)

    def __unicode__(self):
       return self.cat_descr

#images model
class Images(models.Model):
    image = models.ImageField(upload_to='images', blank=False)
    img_name = models.CharField(max_length=120, blank=True)
    img_date = models.DateTimeField(auto_now_add=True)
    img_user = models.ForeignKey(User)
    img_cat_id = models.ForeignKey(Categories)
    
    def __unicode__(self):
        return self.img_name

#comments model
class Comments(models.Model):
    com_descr = models.CharField(max_length=400, blank=True, default='')
    com_by = models.ForeignKey(User)
    img_commented = models.ForeignKey(Images, default='')
    com_date_added = models.DateTimeField(auto_now_add=True)
    com_date_changed = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
       return self.com_descr

#likes model
class Likes(models.Model):
    image_liked = models.ForeignKey(Images, null=True)
    likes = models.IntegerField(blank=False , default=0)
    dislikes = models.IntegerField(blank=False, default=0)
	
    def __unicode__(self):
        return str(self.image_liked)