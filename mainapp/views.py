from django.shortcuts import render
import os
import numpy as np
import pandas as pd
# Create your views here.


def ViewBase(request):
    return render(request, 'base.html')


def ViewSchedule(request):
    return render(request, 'Schedule.html')


def ViewMoniter(request):
    path=os.getcwd()

    #讀取產線描述檔
    list_path=os.path.join(path,'data\production_line_description.json')
    Production_List=pd.read_json(list_path)


    #資料模擬
    station_list = pd.DataFrame(Production_List['production_line']['station']) #讀取工作站明細
    status_by_station = np.full(len(station_list.T),'-') #工作站內的物品狀態


    object_list = ['A'] #物件明細（暫時簡化，所以這裡等於object_name）
    status_by_object = np.full(len(object_list),'-') #物品所在的位置

    station_name = station_list.loc['Name'] #從明細擷取名稱部分，用於顯示
    #---

    sbs_out = [] #工作站視角最後輸出字串
    sbo_out = [] #物件視角最後輸出字串
    for i in range(len(station_list.T)):
        sbs_out.append(station_name[i]+'：'+status_by_station[i]) #字串處理（結合名稱和狀態）

    for i in range(len(object_list)):
        sbo_out.append(object_list[i]+'：'+status_by_object[i]) #字串處理（結合名稱和狀態）


    #輸出參數至base.html
    return render(request, 'Moniter.html',{'status_by_station': sbs_out,
                                        'status_by_object': sbo_out,
                                        })


def ViewQuality(request):
    return render(request, 'Quality.html')


def ViewEquipment(request):
    return render(request, 'Equipment.html')


def ViewInventory(request):
    return render(request, 'Inventory.html')


def ViewStatistics(request):
    return render(request, 'Statistics.html')