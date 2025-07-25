from django.shortcuts import render
from django.http import JsonResponse
from .models import Donor, PatientRequest
from django.views.decorators.csrf import csrf_exempt
import pywhatkit
import datetime
import json

# ✅ Send WhatsApp message via pywhatkit
def send_whatsapp_message(number, message):
    try:
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute + 1

        if minute >= 60:
            minute = 0
            hour = (hour + 1) % 24

        # Assumes Indian number; adjust if needed
        pywhatkit.sendwhatmsg(f"+91{number}", message, hour, minute)
        print(f"WhatsApp message scheduled to +91{number} at {hour}:{minute}")
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")

# ✅ Chatbot API
@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").lower()

        if "thalassemia" in user_message:
            reply = "Thalassemia is a blood disorder affecting hemoglobin production."
        elif "symptom" in user_message:
            reply = "Common symptoms include fatigue, weakness, and pale skin."
        elif "treatment" in user_message:
            reply = "Treatments include regular blood transfusions and chelation therapy."
        elif "donate" in user_message:
            reply = "Thank you! You can register as a donor on our donor page."
        else:
            reply = "I'm still learning! Please ask about symptoms, treatment, or donation."

        return JsonResponse({"reply": reply})

    return JsonResponse({"reply": "Invalid request method."})

# ✅ Match blood group and notify donor
def match_blood_group(request):
    if request.method == 'POST':
        blood_group = request.POST.get('blood_group', '').strip().upper()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')

        patient = PatientRequest.objects.create(
            name=name,
            blood_group=blood_group,
            contact_number=phone,
            location=location
        )

        match = Donor.objects.filter(blood_group__iexact=blood_group).first()

        if match:
            donor_number = match.phone
            send_whatsapp_message(
                number=donor_number,
                message=f"🔔 Match found! A patient named {name} at {location} needs blood group {blood_group}. Contact: {phone}"
            )
            return render(request, 'blood/result.html', {'donor': match})
        else:
            return render(request, 'blood/map.html')

    return render(request, 'blood/getter.html')

# ✅ Donor submission via JSON
@csrf_exempt
def donor_submit(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            Donor.objects.create(
                name=data['full_name'],
                age=data['age'],
                gender=data['gender'],
                blood_group=data['blood_group'].strip().upper(),
                phone=data['contact'],
                email=data['email'],
                location=data['address'],
                last_donation=data['last_donation']
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

# ✅ Static page views
def show_donor_form(request):
    return render(request, 'blood/donor.html')

def homepage(request):
    return render(request, 'blood/homepage.html')

def request_form(request):
    return render(request, 'blood/getter.html')

def awareness_page(request):
    return render(request, 'blood/aware.html')

def register_form(request):
    return render(request, 'blood/register.html')

def map_view(request):
    return render(request, 'blood/map.html')

def chatbot_page(request):
    return render(request, 'chatbot.html')
