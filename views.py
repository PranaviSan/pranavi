from django.shortcuts import render
from django.http import HttpResponse
from airtable import Airtable
import re
import hashlib
airtable = Airtable('apppYweKTopuXYS2s','user',api_key='keyPETW39LD9OhiIF')




def hi(request):
    return render(request,'ONLINEAUCTIONAPP/Main.html')

def home1(request):
    return render(request,'ONLINEAUCTIONAPP/Home.html')

def login(request):
    return render(request,'ONLINEAUCTIONAPP/login.html')

def signup(request):
    return render(request,'ONLINEAUCTIONAPP/Signup.html')

def auction(request):
    return render(request,'ONLINEAUCTIONAPP/auction.html')

def feedback(request):
    return render(request,'ONLINEAUCTIONAPP/feedback.html')


def registrationSuccess(request):
    print(request)
    name = request.POST['name']
    phoneno = request.POST['pno']
    emailid=request.POST['email']
    password = request.POST['pwd']
    passwordhash= hashlib.md5(password.encode())
    userdata = airtable.search("Username", username)
    if (userdata != []):
        return render(request, "ONLINEAUCTIONAPP/Signup.html", {"error": "username already exists"})
    userdata = airtable.search("Email", emailid)
    if (userdata != []):
        return render(request, "ONLINEAUCTIONAPP/Signup.html", {"error": "email already registered"})
    userdata = airtable.search("Phoneno", phoneno)
    print(userdata)
    if (userdata != []):
        return render(request, "ONLINEAUCTIONAPP/Signup.html", {"error": "invalid phonenumber"})

    user_details = {
        "Name": name,
        "Phone number": phoneno,
        "Email": emailid,
        "Password": passwordhash.hexdigest(),

    }
    airtable.insert(user_details)

    return render(request, 'ONLINEAUCTIONAPP/success.html')


def loginsuccess(request):
    username = request.POST['uname']
    password = request.POST['pwd']
    passwordhash = hashlib.md5(password.encode())
    userdata=airtable.search("Username",username)
    if(userdata==[]):
        return render(request,"ONLINEAUCTION/login.html",{"error":"invalid username"})
    if(passwordhash.hexdigest()!=userdata[0]["fields"]["Password"]):
        return render(request, "ONLINEAUCTIONAPP/login.html", {"error": "invalid password"})
    return render(request,"ONLINEAUCTIONAPP/auction.html")