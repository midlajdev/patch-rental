import json
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http.response import HttpResponse
from web.models import Testimonial,Promoter,Faq,Subscribe


def index(request):
    testimonials=Testimonial.objects.all()
    promoters=Promoter.objects.all()
    rent_tracking_faqs=Faq.objects.filter(faq_type="rent_tracking")
    new_deposite_faqs=Faq.objects.filter(faq_type="new_deposite")
    existing_deposite_faqs=Faq.objects.filter(faq_type="existing_deposite")

    context={
        "testimonials": testimonials,
        "promoters": promoters,
        "rent_tracking_faqs":rent_tracking_faqs,
        "new_deposite_faqs":new_deposite_faqs,
        "existing_deposite_faqs":existing_deposite_faqs,
        
    }
    return render(request, 'index.html',context=context)


def subscribe(request):
    email=request.POST.get('email')

    if not Subscribe.objects.filter(email=email).exists():

        Subscribe.objects.create(email=email)

        response_data={
            "status":"success",
            "title":"successfully registered",
            "message":"You subscribed to our newsletter successfully"
        }
    else:
        response_data={
            "status":"error",
            "title":"You are already subscribed",
            "message":"No need to register again"
        }
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")
