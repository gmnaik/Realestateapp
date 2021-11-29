from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST.get('listing_id')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST.get('user_id')
        #realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)

            if has_contacted:
                messages.error(request, 'You have already made inquiry for this property.Plz wait until we contact you')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id,  name=name, email=email, phone=phone, message=message, user_id=user_id)
        
        #admin_info = User.objects.get(is_superuser=True)
        #admin_email = admin_info.email

        #send_mail(
            #'New Property Inquiry',
            #'You have new inquiry for property' + listing + '. Please login to your admin panel and contact the inquired customer.',
            #'gmnaiknaik1@gmail.com',
            #[admin_email , realtor_email],
            #fail_silently = False,
            #)

        contact.save()
        
        messages.success(request, 'Your request has been submitted, we will get back to you shortly')
        return redirect('/listings/'+listing_id)
  