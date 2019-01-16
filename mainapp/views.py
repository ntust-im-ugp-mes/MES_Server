from django.shortcuts import render
import os
import numpy as np
import pandas as pd
import threading
from socket import *
from time import ctime
# Create your views here.
# Pi與MES連線已進行資料交換
def connection():
	host = ''
	port = 11000
	ADDR = (host, port)
	BUFSIZ = 1024

	tcpSocket = socket(AF_INET, SOCK_STREAM)
	tcpSocket.bind(ADDR)
	#set the max number of tcp connection
	tcpSocket.listen(5)
	while True:
		print('waiting for connection...')
		clientSocket, clientAddr = tcpSocket.accept()
		print('conneted form: %s' %clientAddr[0])
		
		while True:
			try:
				global status
				predata = clientSocket.recv(BUFSIZ).decode('utf-8')
				if(predata==''):
					errortext = 'Empty Command'
					clientSocket.send(errortext.encode('utf-8'))
					break
                    
				data = predata.split(',')
                
				if(data[1]=="in"):
					station_list.loc['State'][station_list.T.loc[station_list.loc['Name']==data[0]].index[0]] = 'Working'
				elif(data[1]=="out"):
					station_list.loc['State'][station_list.T.loc[station_list.loc['Name']==data[0]].index[0]] = 'Idle'
				elif(data[1]=="error"):
					station_list.loc['State'][station_list.T.loc[station_list.loc['Name']==data[0]].index[0]] = 'Error'
				else:
					errortext = 'Undefined Command'
					clientSocket.send(errortext.encode('utf-8'))
					break
				print(status)
								
			except IOError as e:
				print(e)
				clientSocket.close()
				break
			if not predata:
				break
			returnData = data[0] + ', I received your data : ' + data[1]
			clientSocket.send(returnData.encode('utf-8'))
			
			print('Received : ' + data[1] + ' from ' + data[0] + '\n')
		clientSocket.close()
	tcpSocket.close()
#---

#---Initial Program---
#讀取產線描述檔
datapath=os.getcwd()
list_path=os.path.join(datapath,'data\production_line_description.json')
Production_List=pd.read_json(list_path)

station_list = pd.DataFrame(Production_List['production_line']['station']) #讀取工作站明細
status_by_station = np.full(len(station_list.T),'-') #初始化工作站內的物品狀態


t = threading.Thread(target=connection)
t.start()

#---

status='-'
def ViewBase(request):
    return render(request, 'base.html')


def ViewSchedule(request):
    return render(request, 'Schedule.html')


#---生產監控---
def ViewMoniter(request):    
 
	status_by_station = station_list.loc['State']

	object_list = ['A'] #物件明細（暫時簡化，所以這裡等於object_name）
	status_by_object = np.full(len(object_list),'-') #物品所在的位置

	station_name = station_list.loc['Name'] #從明細擷取名稱部分，用於顯示
	#---
	
	stations=[]
	objects=[]
	sbo_out = [] #物件視角最後輸出字串
	for i in range(len(station_list.T)):
		stations.append( {'Station':station_name[i], 'Status':status_by_station[i], 'Detail':'-'} )
		pd.DataFrame(stations).to_csv(os.path.join(datapath,'static\data\Station_Status.csv'),index=None)

	for i in range(len(object_list)):
		objects.append( {'name':object_list[i], 'status':status_by_object[i], 'detail':'-'} )

	
	stations = pd.DataFrame(stations).to_csv(index=None)
	#輸出參數至base.html
	return render(request, 'Moniter.html',{'stations': os.path.join(datapath,'data\123.csv'),
											'objects': objects,
										})
#---


def ViewQuality(request):
    return render(request, 'Quality.html')


def ViewEquipment(request):
    return render(request, 'Equipment.html')


def ViewInventory(request):
    return render(request, 'Inventory.html')


def ViewStatistics(request):
    return render(request, 'Statistics.html')