import requests
import json
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required
def chatbot_home(request):
    return render(request, 'chatbot.html')

@csrf_exempt
@require_POST
def ask_bot(request):
    data = json.loads(request.body)
    user_message = data.get("message", "")

    together_api_key = "model_api_key"  

   
    info_path = os.path.join(settings.BASE_DIR, 'chatbot', 'hostel_info.json')
    try:
        with open(info_path, 'r', encoding='utf-8') as f:
            hostel_info = json.load(f)
    except Exception as e:
        return JsonResponse({"reply": f"⚠️ Could not load hostel info: {str(e)}"})

  
    hostel_context = f"""
You are a helpful assistant for {hostel_info['name']} located at {hostel_info['location']}.

📍 Address:
- {hostel_info['address']}

Information
- For more admission process visit {hostel_info['admission-process']}
- students {hostel_info['college-students']}

🚌 Transportation:
- Nearest Bus Stop: {hostel_info['nearest_bus_stop']} via BMTC lines: {', '.join(hostel_info['bus_lines'])}
- Nearest Metro: {hostel_info['nearest_metro_station']} on {hostel_info['metro_line']} Line

🏢 Hostel Details:
- Room Types: {hostel_info['room_types']}
- Mess Timings: {hostel_info['mess_timings']}
- Warden Contact: {hostel_info['warden']}
- Wi-Fi Availability: {hostel_info['wifi']}
- Gate Close Time: {hostel_info['gate_close_time']}

🏠 Facilities:
- {', '.join(hostel_info['facilities'])}

📍 Nearby Landmarks:
- {', '.join(hostel_info['nearby_landmarks'])}

ℹ️ Notes:
{hostel_info['notes']}

💬 Answer user queries only based on this data.
"""

    headers = {
        "Authorization": f"Bearer {together_api_key}",
        "Content-Type": "application/json"
    }

    url = "https://api.together.xyz/v1/chat/completions"

    payload = {
        "model": "meta-llama/Llama-3-8b-chat-hf",
        "messages": [
            {"role": "system", "content": hostel_context},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "max_tokens": 400
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        result = response.json()

        if 'choices' in result and len(result["choices"]) > 0:
            reply = result["choices"][0]["message"]["content"]
        else:
            reply = "❌ Sorry, I couldn't get a valid response from the AI."

        return JsonResponse({"reply": reply})

    except Exception as e:
        return JsonResponse({"reply": f"⚠️ Error: {str(e)}"})
