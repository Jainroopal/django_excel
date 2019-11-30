from django.shortcuts import render

# Create your views here.
from .models import main_year_data
# Create your views here.
from django.shortcuts import render
import openpyxl
import pandas as pd



def index(request):



    if "GET" == request.method:
        return render(request, 'index.html', {})
    else:
    	excel_file = request.FILES["excel_file"]
    	wb = pd.read_excel(excel_file)
    	excel_data = list()
    	for i,j in wb.iterrows():
    		excel_data.append(j)
    		col = excel_data[i][0]
    	# save data into database
    	for i in range(1,len(excel_data[0])):	
    		foo = main_year_data( Hydrate_Production = excel_data[0][i], Specific_Consumption = excel_data[1][i], No_of_days = excel_data[2][i],Consumption = excel_data[3][i],Daily_Consumption=excel_data[4][i])
    		foo.save()
    	return render(request,'index.html',{"excel_data":excel_data})
