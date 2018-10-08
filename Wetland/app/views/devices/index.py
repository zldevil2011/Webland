# coding:utf8
from django.http import HttpResponse
from app.models import Device, Data
import urllib2
import cookielib
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import *


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