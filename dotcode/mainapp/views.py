from django.shortcuts import redirect, render
from .models import *
from logapp import views


def wallfeed(request):
	context = {
		'all_posts' : Post.objects.all(),
		'replies' : Reply.objects.all()
	}
	return render(request,"wall_feed.html", context)


def community(request):
    user = request.session["user_id"]
    context = {
        'users' : get_user(user),
        'all_problems': allproblems(),
        "all_roles": get_freelancers(),
        'all_users' : all_users(),
    }
    return render(request,"community.html", context )

# def client_profile(request,i):
#     pass

def freelancer_profile(request,i):
    context = {
        'lancer' : thislancer(i),
        'asd' : User.objects.get(id = i)
    }
    
    return render(request, 'freelancer-page2.html', context)

def create_post(request,id):
	x = request.POST['write_post']
	Post.objects.create(post = x, user_post = User.objects.get(id = id))
	return redirect('/main/wallfeed')

def create_comment(request,id,post_id):
	#x = request.POST['comment2']
	createcomment(request.POST,id,post_id)

	#Comment.objects.create(Text =  x, post = Post.objects.get(id = post_id), user_comment = User.objects.get(id = id))
	return redirect('/main/wallfeed')

def create_reply(request,comment_id):
	Reply.objects.create(Text = request.POST['reply2'], comment = Comment.objects.get(id = comment_id),user_reply = User.objects.get(id = request.session['user_id']))
	
	return redirect('/main/wallfeed')


# def create_comment(request):
#     pass




# def create_messages(request):
#     pass

def create_problem(request):
    user = request.session["user_id"]

    problem = createproblem(request.POST, user)

    return redirect('/main/community')


