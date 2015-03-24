from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from RMB.models import Likes,Comments, Images,Categories
from django.contrib.auth.decorators import login_required
from RMB.forms import UploadImagesForm

# Index page view
def index(request):
    context = RequestContext(request)
    context_dict = {}
    try:
        # RECENT LIKES with comments limit 9 per page
        image_likes = Likes.objects.order_by('-likes')[:9]
        all_comments = Comments.objects.order_by('-com_date_added') 
        context_dict['image_likes'] = image_likes
        context_dict['all_comments'] = all_comments
    except Likes.DoesNotExist:
        pass
    except Comments.DoesNotExist:
        pass
    return render_to_response('rmb/index.html', context_dict, context)



def worst_image(request):
    context = RequestContext(request)
    context_dict={}
    image_id = None
    if request.method=='GET':
        image_id=request.GET['worst_id']
    if image_id:
        image_likes = Images.objects.order_by('-dislikes') [:9]
        context_dict['image_likes'] = image_likes
    return render_to_response('rmb/worst_image.html', context_dict,context)

#commenting an image view
@login_required
def comment_image(request):
    cat_id = None
    com_id = None
    cat_id = request.GET['comment_id']
    com_id = request.GET['com']
 
    if cat_id:
        cat = Likes.objects.get(id=int(cat_id))
        print(cat.image_liked.img_user)
        new_entry = Comments(com_descr=com_id, com_by=request.user, img_commented=cat.image_liked)
        new_entry.save()
    return HttpResponse(comments)

#like an image view /w get ajax request, user needs to be registered
@login_required
def like_image(request):
    cat_id = None
    if request.method == 'GET':
        
        cat_id = request.GET['like_id']

    likes = 0
    if cat_id:
        cat = Likes.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes =  likes
            cat.save()

    return HttpResponse(likes)

#dislike an image view /w get ajax request, user needs to be registered
@login_required
def dislike_image(request):
    cat_id = None
    if request.method == 'GET':
        
        cat_id = request.GET['dislike_id']

    dislikes = 0
    if cat_id:
        cat = Likes.objects.get(id=int(cat_id))
        if cat:
            dislikes = cat.dislikes + 1
            cat.dislikes =  dislikes
            cat.save()

    return HttpResponse(dislikes)
	
#Must be signed in.
#Page to Upload images
#User can also view previous uploads.
@login_required
def upload_images(request):
    context = RequestContext(request)
    context_dict={}

    if request.method == 'POST': 
	#processes form
        form = UploadImagesForm(request.POST, request.FILES)

        if form.is_valid():

            upload_image = form.save(commit=False)
            upload_image.img_user = request.user
	

            if 'image' in request.FILES:
                upload_image.image  =request.FILES['image']
            print upload_image.img_user
            upload_image.save()
            #next sequence of code will send the image back as form is sent
            form = UploadImagesForm()
            context_dict = {'upload_image': form}
            all_images = Images.objects.filter(img_user=request.user)
            context_dict['all_images']=all_images
            #Likes created to associate likes to image
            like = Likes(likes=0,dislikes=0)
            like.image_liked=upload_image
            print like
            print 'helo'
            like.save()
            context_dict['like']=like


            return render(request, 'rmb/profile.html', context_dict)

        else:
            print form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        form = UploadImagesForm()
        context_dict = {'upload_image': form}
        all_images = Images.objects.filter(img_user=request.user)
        context_dict['all_images']=all_images
        all_cats = Categories.objects.all()
        context_dict['all_cats']=all_cats


        return render_to_response('rmb/profile.html', context_dict, context)

#newest images page
def newest(request):
    context = RequestContext(request)
    context_dict={}

    try:
        
        all_images = Images.objects.order_by('-img_date')
        image_likes = Likes.objects.all()
        context_dict['all_images']=all_images
        all_comments = Comments.objects.all()
        context_dict['image_likes'] = image_likes
        context_dict['all_comments'] = all_comments


    except Images.DoesNotExist:
        pass
    except Likes.DoesNotExist:
        pass
    except Comments.DoesNotExist:
        pass
    return render_to_response('rmb/newest.html', context_dict, context)

# noob beard images page
def noob(request):
    context = RequestContext(request)
    context_dict={}

    try:
        # RECENT RATINGS
        all_images = Images.objects.filter(img_cat_id='4')
        context_dict['all_images']=all_images
        image_likes = Likes.objects.all()
        all_comments = Comments.objects.all()
        context_dict['image_likes'] = image_likes
        context_dict['all_comments'] = all_comments


    except Images.DoesNotExist:
        pass
    except Likes.DoesNotExist:
        pass
    except Comments.DoesNotExist:
        pass
    return render_to_response('rmb/noob.html', context_dict, context)

#moustache images page
def moustache(request):
    context = RequestContext(request)
    context_dict={}

    try:
        # RECENT RATINGS
        all_images = Images.objects.filter(img_cat_id='3')
        context_dict['all_images']=all_images
        image_likes = Likes.objects.all()
        all_comments = Comments.objects.all()
        context_dict['image_likes'] = image_likes
        context_dict['all_comments'] = all_comments


    except Images.DoesNotExist:
        pass
    except Likes.DoesNotExist:
        pass
    except Comments.DoesNotExist:
        pass
    return render_to_response('rmb/moustache.html', context_dict, context)

#half beard images page
def half(request):
    context = RequestContext(request)
    context_dict={}

    try:
        # RECENT RATINGS
        all_images = Images.objects.filter(img_cat_id='2')
        context_dict['all_images']=all_images
        image_likes = Likes.objects.all()
        all_comments = Comments.objects.all()
        context_dict['image_likes'] = image_likes
        context_dict['all_comments'] = all_comments


    except Images.DoesNotExist:
        pass
    except Likes.DoesNotExist:
        pass
    except Comments.DoesNotExist:
        pass
    return render_to_response('rmb/half.html', context_dict, context)

#full beard images beard
def full(request):
    context = RequestContext(request)
    context_dict={}

    try:
        # RECENT RATINGS
        all_images = Images.objects.filter(img_cat_id='1')
        context_dict['all_images']=all_images
        image_likes = Likes.objects.all()
        all_comments = Comments.objects.all()
        context_dict['image_likes'] = image_likes
        context_dict['all_comments'] = all_comments

    except Images.DoesNotExist:
        pass
    except Likes.DoesNotExist:
        pass
    except Comments.DoesNotExist:
        pass
    return render_to_response('rmb/full.html', context_dict, context)

def worse(request):
    context = RequestContext(request)
    context_dict = {}
    try:
        # RECENT RATINGS
        image_likes = Likes.objects.order_by('-dislikes')[:9]
        all_comments = Comments.objects.order_by('com_date_added')
        context_dict['image_likes'] = image_likes
        context_dict['all_comments'] = all_comments
    except Images.DoesNotExist:
        pass
    except Likes.DoesNotExist:
        pass
    except Comments.DoesNotExist:
        pass
    return render_to_response('rmb/worse.html', context_dict, context)




