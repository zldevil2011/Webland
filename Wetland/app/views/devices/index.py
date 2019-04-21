# coding:utf8
import cookielib
import json
import urllib2
from datetime import *
import time
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app.models import AbnormalEvent, Data, Device, DeviceType, Project


@csrf_exempt
def device_list(request):
    """
    获取列表
    """
    user_id = request.session.get('user_id', None)
    print(user_id)
    try:
      device_list = Device.objects.filter(owner_id = user_id)
    except e:
      print('e:', str(e))
      device_list = [{'name':'zhaolong'}]
    device_list = device_list if len(device_list) > 0 else []

    res = {
      'success': True,
      'data': device_list
    }
    response = HttpResponse(json.dumps(res), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response

def device_data(request, device_id):
  """
  获取数据
  """
  data_type = request.GET.get('data_type', None)
  data_start_time = request.GET.get('start_time', None)
  data_end_time = request.GET.get('end_time', None)
  if data_start_time is None or data_end_time is None:
    data_start_time = datetime.combine(date.today(), time.min)
    data_end_time = data_start_time + timedelta(days = 1)
  base_data = Data.objects.filter(device_num = device_id, create_date__gte = data_start_time, create_date__lte = data_end_time)
  res_data = {}
  res_data['data_list'] = []
  res_data['data_time_tag'] = []

  current_time = datetime.today()
  if data_type == 'hour':
    # start_time_00 -> end_time__23 || current_hour
    step_start_time = data_start_time
    while step_start_time <= data_end_time and step_start_time <= current_time:
      start_time = step_start_time
      end_time = start_time + timedelta(hours = 1)
      data_list = [] if len(base_data) == 0 else base_data.filter(create_date >= start_time.date(), create_time.hour >= start_time.hour, create_time.hour < end_time.hour)
      res_data['data_list'].append(data_list)
      res_data['data_time_tag'].append(start_time.strftime("%Y-%m-%d %H:00"))
      step_start_time += timedelta(hours=1)

  elif data_type == 'day':
    step_start_time = data_start_time
    while step_start_time <= data_end_time and step_start_time <= current_time:
      start_time = step_start_time
      end_time = start_time + timedelta(days = 1)
      data_list = [] if len(base_data) == 0 else base_data.filter(create_date >= start_time.date(), create_date < end_time.date())
      res_data['data_list'].append(data_list)
      res_data['data_time_tag'].append(start_time.strftime("%Y-%m-%d"))
      step_start_time += timedelta(days=1)

  elif data_type == 'month':
    current_month = current_time.month
    for i in range(current_month):
      start_time = datetime(current_time.year, i+1, 1)
      end_time = datetime(current_time.year, i+2, 1)
      data_list = [] if len(base_data) == 0 else base_data.filter(create_date >= start_time.date(), create_date < end_time.date())
      res_data['data_list'].append(data_list)
      res_data['data_time_tag'].append(start_time.strftime("%Y-%m"))

  res_data['data_list'] = res_data['data_list'] if len(res_data['data_list']) > 0 else []
  res_data['data_type'] = data_type
  res = {
    'success': True,
    'data': res_data
  }
  response = HttpResponse(json.dumps(res), content_type="application/json")
  return response

def all_device_data(request):
  """
  获取数据
  """
  data_type = request.GET.get('data_type', None)
  data_start_time = request.GET.get('start_time', None)
  data_end_time = request.GET.get('end_time', None)
  if data_start_time is None or data_end_time is None:
    data_start_time = datetime.combine(date.today(), time.min)
    data_end_time = data_start_time + timedelta(days = 1)
  base_data = Data.objects.filter(create_date__gte = data_start_time, create_date__lte = data_end_time)
  res_data = {}
  res_data['data_list'] = []
  res_data['data_time_tag'] = []

  current_time = datetime.today()
  if data_type == 'hour':
    # start_time_00 -> end_time__23 || current_hour
    step_start_time = data_start_time
    while step_start_time <= data_end_time and step_start_time <= current_time:
      start_time = step_start_time
      end_time = start_time + timedelta(hours = 1)
      data_list = [] if len(base_data) == 0 else base_data.filter(create_date >= start_time.date(), create_time.hour >= start_time.hour, create_time.hour < end_time.hour)
      res_data['data_list'].append(data_list)
      res_data['data_time_tag'].append(start_time.strftime("%Y-%m-%d %H:00"))
      step_start_time += timedelta(hours=1)

  elif data_type == 'day':
    step_start_time = data_start_time
    while step_start_time <= data_end_time and step_start_time <= current_time:
      start_time = step_start_time
      end_time = start_time + timedelta(days = 1)
      data_list = [] if len(base_data) == 0 else base_data.filter(create_date >= start_time.date(), create_date < end_time.date())
      res_data['data_list'].append(data_list)
      res_data['data_time_tag'].append(start_time.strftime("%Y-%m-%d"))
      step_start_time += timedelta(days=1)

  elif data_type == 'month':
    current_month = current_time.month
    for i in range(current_month):
      start_time = datetime(current_time.year, i+1, 1)
      end_time = datetime(current_time.year, i+2, 1)
      data_list = [] if len(base_data) == 0 else base_data.filter(create_date >= start_time.date(), create_date < end_time.date())
      res_data['data_list'].append(data_list)
      res_data['data_time_tag'].append(start_time.strftime("%Y-%m"))

  res_data['data_list'] = res_data['data_list'] if len(res_data['data_list']) > 0 else []
  res_data['data_type'] = data_type
  res = {
    'success': True,
    'data': res_data
  }
  response = HttpResponse(json.dumps(res), content_type="application/json")
  return response

def device_register(request):
  success = False
  message = ''
  try:
    name = request.POST.get('name', None)
    device_type = request.POST.get('device_type', None)
    address =  request.POST.get('address', None)
    install_date =  request.POST.get('install_date', None)
    install_time =  request.POST.get('install_time', None)
    latitude =  request.POST.get('latitude', None)
    longitude =  request.POST.get('longitude', None)
    project_id =  request.POST.get('project_id', None)
    owner_id =  request.POST.get('owner_id', None)

    device_type_obj = DeviceType.objects.get(id=int(device_type))
    project_id_obj = Project.objects.get(id=int(project_id))
    owner_id_obj = User.objects.get(id=int(owner_id))
    device = Device(
      name = name,
      device_type = device_type_obj,
      address = address,
      install_date = install_date,
      install_time = install_time,
      latitude = latitude,
      longitude = longitude,
      project_id = project_id_obj,
      owner_id = owner_id_obj
    )
    device.save()
    success = True
  except e:
    message = str(e)
    print(str(e))
  res = {
    'success': success,
    'message': message
  }
  response = HttpResponse(json.dumps(res), content_type="application/json")
  return response

def abnormal_event_list(request):
  success = False
  message = ''
  device_id = request.POST.get('device_id', 'all')
  data_list = []
  if device_id == 'all':
    data_list = AbnormalEvent.objects.all().order_by('create_date')
  else:
    try:
      data_list = AbnormalEvent.objects.filter(device_id__id = int(device_id)).order_by('create_date')
    except e:
      message = str(e)
  res = {
    'success': success,
    'message': message,
    'data': data_list
  }
  response = HttpResponse(json.dumps(res), content_type="application/json")
  return response

@csrf_exempt
def total_data_sum(request):
  """
  获取当前数据量的汇总，包括：今日数据量、昨日数据量、日增加百分比
  """
  # 获取当日数据
  today_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
  yesterday_date = (date.today() + timedelta(days = -1)).strftime("%Y-%m-%d")
  todayDataList = Data.objects.filter(create_date = today_date)
  yesterdayDataList = Data.objects.filter(create_date = yesterday_date)

  today_data_num = len(todayDataList)
  yesterday_data_num = len(yesterdayDataList)
  if yesterday_data_num > 0:
    day_growth_rate = (today_data_num - yesterday_data_num) / yesterday_data_num
  else:
    day_growth_rate = 0

  res_dict = {
    'success': True,
    'data': {
      'todayDataNum': today_data_num,
      'yesterdayDataNum': yesterday_data_num,
      'dayGrowthRate': day_growth_rate,
    }
  }

  response = HttpResponse(json.dumps(res_dict), content_type="application/json")
  response["Access-Control-Allow-Origin"] = "*"
  return response
  
@csrf_exempt
def total_abnormal_sum(request):
  """
  获取异常报警的汇总，包括今日总数，过去两周的日数量
  """      
  data_list = AbnormalEvent.objects.all().order_by('create_date')
  today_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

  todayDataList = AbnormalEvent.objects.filter(create_date = today_date)

  res = {
    'success': True,
    'data': {
      'todayDataNum': len(todayDataList),
      'historyList': [],
    }
  }

  print(res)
  print(res['data'])
  for i in range (30, 0, -1):
    pre_day_date = (date.today() + timedelta(days = (-1 * int(i)))).strftime("%Y-%m-%d")
    pre_day_data_list = AbnormalEvent.objects.filter(create_date = pre_day_date)
    res['data']['historyList'].append({
      'date': pre_day_date,
      'count': len(pre_day_data_list)
    })

  response = HttpResponse(json.dumps(res), content_type="application/json")
  response["Access-Control-Allow-Origin"] = "*"
  return response

@csrf_exempt
def total_device_sum(request):
    """
    设备整体数据统计，包括设备数量
    """
    device_list = Device.objects.all()
    res = {
      'success': True,
      'data': {
        'deviceLength': len(device_list)
      }
    }
    response = HttpResponse(json.dumps(res), content_type="application/json")
    response["Access-Control-Allow-Origin"] = "*"
    return response