from django.shortcuts import render,redirect

from store.forms import CustomUserForm

def register(request):

    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")


    context = {'form':form}
    return render(request,"store/auth/register.html",context)