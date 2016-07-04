import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests

# Create your views here
@api_view(['GET'])
def get_reminder(request):
    return render(request, 'web/index.html')


@api_view(['GET'])
def get_uber_time(request):
    latitude = request.GET.get('lat')
    longitude = request.GET.get('long')
    if longitude and latitude:
        response = requests.get(
            'https://api.uber.com/v1/estimates/time',
            params={'start_longitude':longitude, 'start_latitude': latitude},
            headers={'Authorization': 'Token BPehDhjfmMaomcn2ZbnWuyaqRzrZoTS1ezAMlZs1'}).json()
        ubergo_time = None
        for time in response['times']:
            if time['localized_display_name'] == 'uberGO':
                ubergo_time = time['estimate']
        return Response({'time': ubergo_time}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'longitude and latitude are required parameters'},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_maps_time(request):
    start_longitude = request.GET.get('slon')
    start_latitude = request.GET.get('slat')
    end_longitude = request.GET.get('elon')
    end_latitude = request.GET.get('elat')
    if start_latitude and start_longitude and end_latitude and end_longitude:
        params = {'origins': start_latitude + ',' + start_longitude,
                  'destinations': end_latitude + ',' + end_longitude,
                  'key': 'AIzaSyB6ky0s6kmaxH15hsxsNHKuZeI6n_OG2eA'
                  }
        url = 'https://maps.googleapis.com/maps/api/distancematrix/json'
        response = requests.get(url, params=params).json()
        time = response['rows'][0]['elements'][0]['duration']['value']
        return Response({'time': time}, status=status.HTTP_200_OK)
    else:
        message = 'start_longitude, start_latitude, end_longitude, end_latitude are required parameters'
        return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def send_email(request):
    try:
        toaddr = request.GET.get('email')
        fromaddr = "uber.remind@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Uber Reminder"
        body = "It's time to book reminder"
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "rdpasswo")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        return Response({'message': 'email sent'}, status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({'message': ex.message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
