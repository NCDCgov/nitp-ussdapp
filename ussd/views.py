from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Testresult

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('+2347036414710')
        text = request.POST.get('text')

        response = ""

        if text == "":
            response = "CON Welcome to NCDC Result Verification Portal \n"
            # response .= "1. My Account \n"
            response += "Kindly put in your certificate number to continue"

        # elif text == "1":
        #     response = "END My Phone number is {0}".format(phone_number)
        elif text:
            try:
                result = Testresult.objects.get(cert_no=text)
                response = "END Name: {0} {1} \n".format(result.first_name, result.last_name)
                response += "Status: {0}".format(result.result)
            except Testresult.DoesNotExist:
                response = "END Certificate number not found"
                
        return HttpResponse(response)