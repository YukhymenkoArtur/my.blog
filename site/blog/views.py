# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect, HttpResponse ####

# from .models import Item
# from .forms import ItemForm


from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Item
from .forms import ItemForm




def index(request):
	queryset = Item.objects.all()
	context = {
	"items": queryset
	}
	print(context)
	print(request.user)
	return render(request, "blog/index.html", context)
# Create your views here.


def detail(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	template = "blog/detail.html"
	context ={
		"item": item
	}
	return render(request, template, context)




def create(request):
	template = "blog/create.html"
	form = ItemForm(request.POST or None)	
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return HttpResponseRedirect(reverse("detail", args=(post.id,)))
	else:
		form = ItemForm()	
		context = {
			"form": form
		}
	return render(request, template, context)


def post_edit(request, item_id):
        post = get_object_or_404(Item, id=item_id)
        if request.method == "POST":
            form = ItemForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return HttpResponseRedirect(reverse("detail", args=(post.id,)))
        else:
            form = ItemForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


def deleted(request, pk):
	item = get_object_or_404(Item, pk=pk)
	sample = Item.objects.filter(pk=item.pk).delete()
	
	return HttpResponseRedirect(reverse("index"))


#new_today

# def Posts(request, id):
# if request.method=='GET':
# 	post=Post.objects.get(id=id)
# 	comments=Comment.objects.filter(post=str(id)).all()
# 	if request.user.is_authenticated():
# 		addform=ComForm(request.POST or None, instance=request.user)
# 			return render_to_response("posts.html", locals(), context_instance=RequestContext(request, processors=[default]))
# 		if request.method=='POST':
# 	comment=ComForm(request.POST)
# 		if comment.is_valid():
# 		comment.save(request.user, id)
# 		return HttpResponseRedirect("/posts/"+id)