from django.shortcuts import render

# Create your views here.
from .models import main_year_data
# Create your views here.
from django.shortcuts import render
import openpyxl
import pandas as pd
import numpy as np


def index(request):



    if "GET" == request.method:
        return render(request, 'index.html', {})
    else:
    	excel_file = request.FILES["excel_file"]
    	wb = pd.read_excel(excel_file)
    	wb = wb.replace(np.nan,None)
    	excel_data = list()
    	# for i,j in wb.iterrows():
    	# 	excel_data.append(j)
    	# 	col = excel_data[i][0]
    	# save data into database
    	for i in wb.columns:
    		excel_data.append(wb[i])
    	print(excel_data)
    	

    	for i in range(len(excel_data[0])):	
    		foo = main_year_data(BauxitePlan= excel_data[0][i],  Apr = excel_data[1][i], May  = excel_data[2][i],Jun = excel_data[3][i], Jul=excel_data[4][i],Aug = excel_data[5][i],Sep = excel_data[6][i],Oct = excel_data[7][i],Nov = excel_data[8][i],Dec = excel_data[9][i], Jan = excel_data[10][i], Feb = excel_data[11][i],Mar = excel_data[12][i])
    		foo.save()
    	return render(request,'index.html',{"excel_data":excel_data})
