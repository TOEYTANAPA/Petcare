from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import Car1, Car2,Booking
from django.core import serializers
from django.shortcuts import render_to_response

# Create your views here.
def IndexView(request):
   
    return render(request, 'booking.html', {'key': 'key','value' : 'value'})	

def getTime(request):

    if request.is_ajax() :
        data = request.GET.get('use', False)
        data = json.loads(data)
        daySel = str(data['day'])+"/"+str(data['month'])+"/"+str(data['year'])
        print ("++++++ : "+daySel)
        car1 = Car1.objects.filter(day = daySel)
        car2 = Car2.objects.filter(day = daySel)
        response1 = serializers.serialize("json", car1)
        response2 = serializers.serialize("json", car2)
        count1 = Car1.objects.filter(day=daySel).count()
        count2 = Car2.objects.filter(day=daySel).count()
        print("++++++++++1")
        print(count1)
        print("++++++++++2")
        print(count2)
    
        if(data['la'] >= 14.06810492):
            
            
            # print ("count is "+ str(count))
            if(count1 <= 0) :
                return HttpResponse(json.dumps({"count": count1,"car":"car1"}), content_type='application/json')
            if(count1 >= 6 and count2 < 6):
                print("+++++++1")
                return HttpResponse(json.dumps({"response": response2,"count": count2,"car":"car2"}), content_type='application/json')
            if(count1 >= 6 and count2 >= 6):
                print("+++++++1.2")
                return HttpResponse(json.dumps({"count": "full","car":"full"}), content_type='application/json')
            print("+++++++1.3")
            return HttpResponse(json.dumps({"response": response1,"count": count1,"car":"car1"}), content_type='application/json')
        else :
            
           
            # print ("count is "+str(count))
            if(count2 <= 0):
                return HttpResponse(json.dumps({"count": count2,"car":"car2"}), content_type='application/json')
            if(count2 >= 6 and count1 < 6 ):
                print("++++++++2")
                return HttpResponse(json.dumps({"response": response1,"count": count1,"car":"car1"}), content_type='application/json')
            if(count2 >= 6 and count1 >= 6):
                print("+++++++2.1")
                return HttpResponse(json.dumps({"count": "full"}), content_type='application/json')
            
            return HttpResponse(json.dumps({"response": response2,"count": count2,"car":"car2"}), content_type='application/json')
        # print(data)

   
    	
    return JsonResponse({'foo':'bar'})


def submit(request):
    if request.is_ajax() and request.GET:
        data = request.GET.get('json', False)
        x = data
        data = json.loads(data)
        if(data.get('count') == 1):
            day = data.get('day',None)
            time = data.get('time',None)
            if(data.get('car') == 'car1'):
                Car1.objects.create(day=day, time=time)
            else :
                Car2.objects.create(day=day, time=time)
            Booking.objects.create(user=data.get('user'),dog=data.get('dog'),total=data.get('total'),
                               service=json.dumps(data.get('service')),location=data.get('location'),day=day,time=time) 
        else :
            day = data.get('day',None)
            time1 = data.get('time1',None)
            time2 = data.get('time2',None)
            totaltime = "["+time1+","+time2+"]"
            if(data.get('car') == 'car1'):
                Car1.objects.create(day=day, time=time1)
                Car1.objects.create(day=day, time=time2)
            else :
                Car2.objects.create(day=day, time=time1)
                Car2.objects.create(day=day, time=time2)
            Booking.objects.create(user=data.get('user'),dog=json.dumps(data.get('dog')),total=data.get('total'),
                               service=json.dumps(data.get('service')),location=data.get('location'),day=day,time=totaltime
                            )

    return JsonResponse({'data': x})

    # return render_to_response('receipt.html',{ 'object_list': data})
        # template_context = {
        #     'my_json':   json.dumps(data) 
        # }

    # return render_template('receipt.html', **template_context )
    # # return HttpResponseRedirect('/receipt',{'data':'data'}, content_type='application/json')

def receipt(request,data):
    # print("+++++++++++++++++++++"+data)
    # j = json.loads(data)
    return render(request, 'receipt.html',{'data':data})