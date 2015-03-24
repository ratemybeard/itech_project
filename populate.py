import os
import sys
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from datetime import datetime

try:
    from django.utils.timezone import now
except ImportError:
    now = datetime.now

def populate():
############################################################################################################################
# 													add sites															   #
############################################################################################################################
    newip = add_site(domain='http://127.0.0.1:8000',name='http://127.0.0.1:8000')

############################################################################################################################
#                                               add social applications													   #
############################################################################################################################
    newFacebook = add_social(provider='facebook',name='Facebook',client_id='1398685107113698',secret='50c5f4cae952e44b46db1357648b9751')
    newGoogle = add_social(provider='google', name='Google',client_id='168253091474-giiulibfgiu92f9de49htbno2jdtc9nm.apps.googleusercontent.com',secret='MI_uXI23vDiVZXX1QAUyBJfa')
    newFacebook.save()
    newGoogle.save()
    newFacebook.sites.add(newip)
    newGoogle.sites.add(newip)
############################################################################################################################
#													add users															   #
############################################################################################################################
    user1 = add_user(username='John', password='john123', email='john@gmail.com')
    user2 = add_user(username='Marco', password='marco123', email='marco@gmail.com')
    user3 = add_user(username='Kate', password='kate123', email='kate@gmail.com')
    user4 = add_user(username='Iain', password='iain123', email='iain@gmail.com')
    user5 = add_user(username='Ann', password='ann123', email='ann@gmail.com')
    user6 = add_user(username='Jen', password='jen123', email='jen@gmail.com')
    user7 = add_user(username='Jim', password='jim123', email='jim@gmail.com')
    user8 = add_user(username='Leif', password='leif123', email='leif@gmail.com')
    user9 = add_user(username='Lisa', password='lisa123', email='lisa@gmail.com')
    user10 = add_user(username='George', password='george123', email='george@gmail.com')
############################################################################################################################
#												add user profiles														   #
############################################################################################################################
    userprofile1 = add_profile(user=user1,name='John',surname='Snow',picture='',last_login=now())
    userprofile2 = add_profile(user=user2,name='Marco',surname='Polo',picture='',last_login=now())
    userprofile3 = add_profile(user=user3,name='Kate',surname='Strathmore',picture='',last_login=now())
    userprofile4 = add_profile(user=user4,name='Iain',surname='Steward',picture='',last_login=now())
    userprofile5 = add_profile(user=user5,name='Ann',surname='Summers',picture='',last_login=now())
    userprofile6 = add_profile(user=user6,name='Jen',surname='Jonovitch',picture='',last_login=now())
    userprofile7 = add_profile(user=user7,name='Jim',surname='Boy',picture='',last_login=now())
    userprofile8 = add_profile(user=user8,name='Leif',surname='Azz',picture='',last_login=now())
    userprofile9 = add_profile(user=user9,name='Lisa',surname='Winter',picture='',last_login=now())
    userprofile10 = add_profile(user=user10,name='George',surname='Frankies',picture='',last_login=now())
############################################################################################################################
#												add categories															   #
############################################################################################################################
    cat1 = add_category(cat_descr='Full Beard')
    cat2 = add_category(cat_descr='Half Beard')
    cat3 = add_category(cat_descr='Moustaches')
    cat4 = add_category(cat_descr='Noob Beard')
############################################################################################################################
#												add images																   #
############################################################################################################################
    image1 = add_images(img_name='beard1' ,img_date=now(),img_user=user1,img_cat_id=cat1)
    image2 = add_images(img_name='beard2',img_date=now(),img_user=user2,img_cat_id=cat2)
    image3 = add_images(img_name='beard3',img_date=now(),img_user=user3,img_cat_id=cat3)
    image4 = add_images(img_name='beard4',img_date=now(),img_user=user4,img_cat_id=cat4)
    image5 = add_images(img_name='beard5',img_date=now(),img_user=user5,img_cat_id=cat1)
    image6 = add_images(img_name='beard6',img_date=now(),img_user=user6,img_cat_id=cat2)
    image7 = add_images(img_name='beard7',img_date=now(),img_user=user7,img_cat_id=cat3)
    image8 = add_images(img_name='beard8',img_date=now(),img_user=user8,img_cat_id=cat4)
    image9 = add_images(img_name='beard9',img_date=now(),img_user=user9,img_cat_id=cat1)
    image10 = add_images(img_name='beard10',img_date=now(),img_user=user10,img_cat_id=cat2)
    image11 = add_images(img_name='beard11',img_date=now(),img_user=user1,img_cat_id=cat3)
    image12 = add_images(img_name='beard12',img_date=now(),img_user=user3,img_cat_id=cat4)
    image13 = add_images(img_name='beard13',img_date=now(),img_user=user4,img_cat_id=cat1)
    image14 = add_images(img_name='beard14',img_date=now(),img_user=user3,img_cat_id=cat2)
    image15 = add_images(img_name='beard15',img_date=now(),img_user=user6,img_cat_id=cat3)
    image16 = add_images(img_name='beard16',img_date=now(),img_user=user4,img_cat_id=cat4)
    image17 = add_images(img_name='beard17',img_date=now(),img_user=user3,img_cat_id=cat1)
    image18 = add_images(img_name='beard18',img_date=now(),img_user=user6,img_cat_id=cat2)
    image19 = add_images(img_name='beard19',img_date=now(),img_user=user7,img_cat_id=cat3)
    image20 = add_images(img_name='beard20',img_date=now(),img_user=user8,img_cat_id=cat4)
    image21 = add_images(img_name='beard21',img_date=now(),img_user=user9,img_cat_id=cat2)
############################################################################################################################
#													add likes															   #
############################################################################################################################
    add_like(image_liked=image1 , likes=4,dislikes=0)
    add_like(image_liked=image2 , likes=2,dislikes=0)
    add_like(image_liked=image3 , likes=12,dislikes=0)
    add_like(image_liked=image4 , likes=32,dislikes=0)
    add_like(image_liked=image5 , likes=12,dislikes=0)
    add_like(image_liked=image6 , likes=13,dislikes=0)
    add_like(image_liked=image7 , likes=24,dislikes=0)
    add_like(image_liked=image8 , likes=33,dislikes=0)
    add_like(image_liked=image9 , likes=44,dislikes=0)
    add_like(image_liked=image10, likes=51,dislikes=0)
    add_like(image_liked=image11, likes=11,dislikes=0)
    add_like(image_liked=image12, likes=21,dislikes=0)
    add_like(image_liked=image13, likes=13,dislikes=0)
    add_like(image_liked=image14, likes=14,dislikes=40)
    add_like(image_liked=image15, likes=15,dislikes=0)
    add_like(image_liked=image16, likes=11,dislikes=0)
    add_like(image_liked=image17, likes=12,dislikes=0)
    add_like(image_liked=image18, likes=13,dislikes=0)
    add_like(image_liked=image19, likes=14,dislikes=0)
    add_like(image_liked=image20, likes=15,dislikes=0)
    add_like(image_liked=image21, likes=11,dislikes=0)
############################################################################################################################
#													add comments														   #
############################################################################################################################
    add_comment(com_descr = 'fucking awsome picture, loved it', com_by= user1,img_commented=image1, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'not bad', com_by= user2,img_commented=image1, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'loved the beard , but thats a bit creepy', com_by= user3,img_commented=image20, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'Hello Kitty!', com_by= user4,img_commented=image20, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'thumbs up', com_by= user5,img_commented=image2, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'not even a beard', com_by= user6,img_commented=image2, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'are you even human mate?', com_by= user7,img_commented=image3, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'nanchos with that please', com_by= user8,img_commented=image4, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'this picture does not makes any sense', com_by= user1,img_commented=image5, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'noob noob noob noob noob', com_by= user9,img_commented=image1, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'thanks, you just ruined my day', com_by= user10,img_commented=image3, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'fucking awsome', com_by= user1,img_commented=image15, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'Meh', com_by= user2,img_commented=image1, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'two seconds of my life wasted', com_by= user3,img_commented=image1, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'ladies man!!!!!!!!!!!!', com_by= user4,img_commented=image1, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'wtf is that?!?!!', com_by= user5,img_commented=image1, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'thats what i call a beard', com_by= user6,img_commented=image1, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'nice', com_by= user7,img_commented=image1, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'November is already finished', com_by= user8,img_commented=image1, com_date_added = now(), com_date_changed= now())
    add_comment(com_descr = 'Hitler Mustache?!!', com_by= user9,img_commented=image1, com_date_added = now(), com_date_changed= now())
############################################################################################################################
# 						Print out what we have added to the user. - Just show the categories and users					   #
############################################################################################################################
    for a in UserProfile.objects.all():
        for b in Categories.objects.all():
            print "- {0} - {1}".format(str(a), str(b))
############################################################################################################################
#												definitions																   #
############################################################################################################################
def add_site(domain,name):
    z = Site.objects.get_or_create(domain=domain, name=name) [0]
    return z
############################################################################################################################
def add_social(provider,name,client_id,secret):
    y = SocialApp.objects.get_or_create(provider=provider,name=name,client_id=client_id,secret=secret) [0]
    return y
############################################################################################################################
def add_user(username,password, email):
    p = User.objects.get_or_create(username=username,password=password, email=email)[0]
    return p
############################################################################################################################
def add_profile(user,name,surname,picture,last_login):
    a = UserProfile.objects.get_or_create(user=user,name=name,surname=surname,picture=picture,last_login=last_login) [0]
    return a
############################################################################################################################
def add_category(cat_descr):
    b = Categories.objects.get_or_create(cat_descr=cat_descr) [0]
    return b
############################################################################################################################
def add_images(img_name,img_date,img_user,img_cat_id):
    c = Images.objects.get_or_create(img_name=img_name,img_date=img_date,img_user=img_user,img_cat_id=img_cat_id) [0]
    return c
############################################################################################################################
def add_like(image_liked,likes,dislikes):
    d = Likes.objects.get_or_create(image_liked=image_liked,likes=likes,dislikes=dislikes) [0]
    return d
def add_comment(com_descr,com_by,img_commented,com_date_added,com_date_changed):
    e = Comments.objects.get_or_create(com_descr = com_descr, com_by = com_by, img_commented=img_commented,com_date_added= com_date_added, com_date_changed = com_date_changed) [0]
    return e
############################################################################################################################
# Start execution here!																									   #
############################################################################################################################
if __name__ == '__main__':
    print "Starting Rate My Beard population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Itech_project.settings')
    application = get_wsgi_application()
    from django.contrib.sites.models import Site
    from allauth.socialaccount.models import SocialApp
    from RMB.models import User,UserProfile,Categories,Images,Likes,Comments
    populate()

