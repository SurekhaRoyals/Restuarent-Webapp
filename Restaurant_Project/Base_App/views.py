from django.shortcuts import render
# from django.http import HttpResponse
from Base_App.models import BookTable,AboutUs,Feedback,ItemList,Items


# Create your views here.
def HomeView(req):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    # intro = Home.objects.all()
    return render(req, 'home.html', {'items':items,'list':list, 'review':review})

def AboutView(req):
    data = AboutUs.objects.all()
    return render(req, 'about.html',{'data': data})

def MenuView(req):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(req, 'menu.html', {'items':items,'list':list})

def BookTableView(req):
    if req.method == "POST":
        name = req.POST.get('user_name')
        phone_number = req.POST.get('phone_number')
        email = req.POST.get('user_email')
        total_persons = req.POST.get('total_persons')
        booking_date = req.POST.get('booking_table')

        if name != '' and len(phone_number) == 10 and email !='' and total_persons != '' and booking_date != '':
            data = BookTable(Name = name, Phone_number = phone_number, Email = email, Total_person = total_persons, Booking_date = booking_date)
           
            data.save()
    return render(req, 'book_table.html')

def FeedbackView(req):
    return render(req, 'feedback.html')
















































































