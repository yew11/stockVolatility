from tkinter import *
from pandas_datareader.data import Options
#---------------function------------
def get_one_ticker():
    ticker=company.get()
    option_data = Options(ticker,data_source='yahoo').get_all_data()
    option_data.reset_index(inplace=True)
    option_data.drop('JSON', axis=1, inplace=True)
    print option_data

#-----------------------------tk layout
app = Tk()
title = Label(app, text="Web Crawl Software").grid(row = 0, column = 1, sticky = 'ns')

company=StringVar(app)
##ROW 1 information
enter_text = Label(app, text="Enter Your Option Name: ").grid(row = 1, sticky = W)  # 'prompt'
enter_text_entry = Entry(app, bd =5,textvariable=company).grid(row = 1, column = 1)  # real enter

go = Button(app, text = 'Go!',command=get_one_ticker).grid(row = 1, column = 2, pady = 10)# go, executive go

##ROW 2 information
random_pick = Button(text = "Random Generate").grid(row = 2, column= 0) # 'prompt'
k = Entry(app, bd =3, width = 3).grid(row =2, column = 1)  # type in k
go1 = Button(app, text = 'Go!').grid(row = 2, column = 2, pady = 10)  # go


##ROW 3 information
list1 = ['1','2','3','4']
var1 =StringVar(app)
var1.set('1')
dropdown =OptionMenu(app, var1,  *list1)
choose = Label(app, text = "Choose industries: ").grid(row = 3, column = 0)# 'prompt'
dropdown.grid(row = 3, column = 1)  # drop down list selection
k1 = Entry(app, bd =3, width = 3).grid(row =3, column = 2)# K
go2 = Button(app, text = 'Go!').grid(row = 3, column = 3, pady = 10) # go

##ROW 4 information
##text box information



app.title ("WebCrawl")
app.geometry("480x320+0+0")
app.mainloop()

