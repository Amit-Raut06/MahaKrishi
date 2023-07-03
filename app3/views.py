from django.shortcuts import render,redirect
from .models import Fram_dt


# Create your views here.
def login(request):

     if request.method=='POST':

       username=request.POST['username']
       password= request.POST['password']
       from django.contrib import auth
       user=auth.authenticate(username=username,password=password)
       if user  is  not None:
           auth.login(request, user)
           if user.is_superuser: return redirect('user/')
          # return redirect('/user/')
          # return redirect('/')
           return render(request, 'user_info.html')
       else:
          return redirect('login')

     else:
          return render(request, 'login.html')


# Create your views here.
def user(request):
    if request.method == 'POST':
        fname = request.POST['FirstName']
        lname = request.POST['LastName']
        email = request.POST['EmailID']
        gender = request.POST['Gender']
        region = request.POST['Region']
        stype = request.POST['soil_type']
        subtp = request.POST['sub_type']
        nextcrop = ''

        if subtp == 'Rabi':
            if region=='Kolhapur':
                if stype == 'R Brown(EW)': nextcrop = ['Groundnuts', 'Maize']
                elif stype == 'R Brown(LW)' : nextcrop = ['Turi', 'Ragi']

            elif region=='Solapur':
                if stype == 'M Brown(EW)': nextcrop = ['Sugarcane', 'Pigeonpea']
                elif stype == 'M Brown(LW)' : nextcrop = ['Chickpea', 'FenuGreek']
                elif stype == 'D Black(EW)' : nextcrop = ['Sorghum', 'Sunflower']
                elif stype == 'D Black(LW)' : nextcrop = ['Chickpea']

        elif subtp == 'Kharib':
            if region == 'Kolhapur':
                if stype == 'R Brown(EW)': nextcrop = ['Gram', 'Raddish', 'Cabbage']
                elif stype == 'R Brown(LW)': nextcrop = ['Gram', 'Vatana', 'Raddish']

            elif region == 'Solapur':
                if stype == 'M Brown(EW)': nextcrop = ['Wheat', 'Sunflower']
                elif stype == 'M Brown(LW)': nextcrop = ['Tomato', 'Wheat']
                elif stype == 'D Black(EW)': nextcrop = ['Sorghum', 'Safflower']
                elif stype == 'D Black(LW)': nextcrop = ['Carrot', 'Onion']

        x = Fram_dt(fname=fname, lname=lname, email=email, gender=gender,
                    region=region, stype=stype, subtp=subtp, nextcrop=nextcrop)
        x.save()
        d = {'fname': fname, 'lname': lname,'email' : email,'gender': gender,'region': region,'stype': stype,'subtp': subtp,'nextcrop': nextcrop}
        return render(request, "details.html", d)

    else:
        dt = Fram_dt.objects.all()
        return render(request, 'info.html', {'dt': dt})