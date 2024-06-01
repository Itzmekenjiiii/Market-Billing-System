from logging import RootLogger
from re import L, search
from tkinter import *
from tkinter import messagebox
import random,os

billnumber=random.randint(500,1000)


#GUI==================================================================================================================================================================
root1=Tk()
root1.title('Billing System')
root1.geometry('1270x720')
root1.configure(bg='gray20')
root1.resizable(False,False)



#LABEL

#FIRST ROW------------------------------------------------------------------------------------------------------------------------------------------------------------
headingLabel=Label(root1,text="K E N J I 's   M I N I S T O R E", font=('arial',30,'bold'),bg='gray20',fg='skyblue',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

#SECOND ROW-----------------------------------------------------------------------------------------------------------------------------------------------------------
cd_frame=LabelFrame(root1,text='Customer Details',font=('arial',15,'bold'),fg='skyblue',bd=8,relief=GROOVE,bg='gray20')
cd_frame.pack(fill=X)

#NAME
n_label=Label(cd_frame,text='Name:',font=('arial',15,'bold'),fg='white',bg='gray20')
n_label.grid(row=0,column=1,padx=20)

n_entry=Entry(cd_frame,font=('arial',15,'bold'),bd=7,width=18)
n_entry.grid(row=0,column=2)

#PHONE
p_label=Label(cd_frame,text='Phone Number:',font=('arial',15,'bold'),fg='white',bg='gray20')
p_label.grid(row=0,column=3,padx=20)

p_entry=Entry(cd_frame,font=('arial',15,'bold'),bd=7,width=18)
p_entry.grid(row=0,column=4)

#BILL NUMBER
b_label=Label(cd_frame,text='Bill Number:',font=('arial',15,'bold'),fg='white',bg='gray20')
b_label.grid(row=0,column=5,padx=20)

b_entry=Entry(cd_frame,font=('arial',15,'bold'),bd=7,width=18)
b_entry.grid(row=0,column=6)

#SEARCH BTN
s_BTN=Button(cd_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,bg='beige',command=lambda:search_bill())
s_BTN.grid(row=0,column=7,padx=20,pady=10)


#EXIT==============================================================================================================================================================================

def exit():
        messagebox.showinfo('EXIT','THANK YOU FOR YOUR PURCHASE''\n HAVE A NICE DAY!')
        root1.withdraw()    


#TOTAL FUNCTIONS==============================================================================================================================================================

#TOTAL BTN
def total():
    #GLOBAl
    global bsp,fcp,fwp,hsp,hgp,blp
    global rip,oip,cop,mp,sp,tp
    global rop,pep,wp,spp,gip,ckp
    global totalbill

    #COSMETICS=======================================================================================================================================================================
    bsp=int(ba_entry.get())*20
    fcp=int(fa_entry.get())*50
    fwp=int(fw_entry.get())*100
    hsp=int(hp_entry.get())*150
    hgp=int(hg_entry.get())*80
    blp=int(bl_entry.get())*60

    #total cosmetic price
    tcp=bsp+fcp+fwp+hsp+hgp+blp
    cp_entry.delete(0,END)
    cp_entry.insert(0,str(tcp)+'php')

    #cosmetic tax
    ctax=tcp*0.12
    ct_entry.delete(0,END)
    ct_entry.insert(0,str(ctax)+'php')

    #GROCERY=========================================================================================================================================================================
    rip=int(ri_entry.get())*50
    oip=int(oi_entry.get())*50
    cop=int(co_entry.get())*25
    mp=int(m_entry.get())*50
    sp=int(s_entry.get())*60
    tp=int(t_entry.get())*40

    #total grocery price
    tgp= rip+oip+cop+mp+sp+tp
    gp_entry.delete(0,END)
    gp_entry.insert(0,str(tgp)+'php')

    #grocery tax 
    gtax=tcp*0.08
    gt_entry.delete(0,END)
    gt_entry.insert(0,str(gtax)+'php')

    #COLD DRINKS=====================================================================================================================================================================
    rop=int(ro_entry.get())*15
    pep=int(pe_entry.get())*15
    wp=int(w_entry.get())*10
    spp=int(sp_entry.get())*15
    gip=int(gi_entry.get())*35
    ckp=int(ck_entry.get())*15

    #total drinks price
    tdp= rop+pep+wp+spp+gip+ckp
    cdp_entry.delete(0,END)
    cdp_entry.insert(0,str(tdp)+'php')

    #cold drinks tax
    cdtax=tcp*0.08
    cdt_entry.delete(0,END)
    cdt_entry.insert(0,str(cdtax)+'php')

    totalbill=tcp+tgp+tdp+ctax+gtax+cdtax

#CLEAR FUNCTION======================================================================================================================================================================

def clear():

#CUSTOMER INFO=======================================================================================================================================================================

    n_entry.delete(0,END)
    p_entry.delete(0,END)
    b_entry.delete(0,END)

#COSMETICS===========================================================================================================================================================================

    ba_entry.delete(0,END)
    fa_entry.delete(0,END)
    fw_entry.delete(0,END)
    hp_entry.delete(0,END)
    hg_entry.delete(0,END)
    bl_entry.delete(0,END)

#GROCERIES===========================================================================================================================================================================

    ri_entry.delete(0,END)
    oi_entry.delete(0,END)
    co_entry.delete(0,END)
    m_entry.delete(0,END)
    s_entry.delete(0,END)
    t_entry.delete(0,END)

#COLD DRINKS=========================================================================================================================================================================

    ro_entry.delete(0,END)
    pe_entry.delete(0,END)
    w_entry.delete(0,END)
    gi_entry.delete(0,END)
    sp_entry.delete(0,END)
    ck_entry.delete(0,END)

#TOTAL PRICE AND TAX=================================================================================================================================================================

    cdp_entry.delete(0,END)
    cdt_entry.delete(0,END)
    gt_entry.delete(0,END)
    gp_entry.delete(0,END)
    ct_entry.delete(0,END)
    cp_entry.delete(0,END)

#RECEIPT=============================================================================================================================================================================

    txt_area.delete(1.0,END)



#PATH================================================================================================================================================================================
if not os.path.exists('bills'):
    os.mkdir('bills')


#SEARCH==========================================================================================================================================================================

def search_bill():
    for i in os.listdir('bills'):
        if i.split('.') [0] == b_entry.get():
            f = open(f'bills\{i}','r')
            txt_area.delete('1.0',END)
            for data in f:
                txt_area.insert(END,data)
            f.close()
            break

    else:
        messagebox.showerror('Error','Invalid Bill Number')



#SAVE BILL FUNCTION=======================================================================================================================================================================

def save_bill():
    global billnumber
    result= messagebox.askyesno('Confirm','Do you want to save the bill? ')
    if result :
        bill_content=txt_area.get(1.0,END)
        file = open(f'bills\{billnumber}. txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number: {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)



#BILL AREA FUNCTION==============================================================================================================================================================

billnumber=random.randint(500,1000)

def bill_area():
    if n_entry.get()=='' or p_entry.get()=='':
        messagebox.showerror('ERROR','Customer Details Are Required')

    elif cp_entry.get()=='' and gp_entry.get()=='' and cdp_entry.get()=='':
        messagebox.showerror('ERROR','NO PRODUCTS SELECTED')
    
    elif cp_entry.get()=='0 php' and gp_entry.get()=='0 php' and cdp_entry.get()=='0 php':
        messagebox.showerror('ERROR','NO PRODUCTS SELECTED')
    else:
    
        txt_area.delete('1.0',END)

    
    
        txt_area.insert(END,"\t\t******KENJI's MINISTORE******\n")
        txt_area.insert(END,'\t\t******Welcome Customer******\n')
        txt_area.insert(END,'\n============================================================')
        txt_area.insert(END,f'\nBill Number:{billnumber}') 
        txt_area.insert(END,f'\nCustomer Name:{n_entry.get()}')
        txt_area.insert(END,f'\nCustomer Phone Number:{p_entry.get()}')
        txt_area.insert(END,'\n============================================================')
        txt_area.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
        txt_area.insert(END,'\n============================================================')

    #Cosmetics

    #========================Product==========Quantity============Price==============================================================================================================

        if ba_entry.get()!='0':
            txt_area.insert(END,f'\nBath Soap\t\t\t{ba_entry.get()}\t\t\t{bsp} Php')
        if fa_entry.get()!='0':
            txt_area.insert(END,f'\nFace Cream\t\t\t{fa_entry.get()}\t\t\t{fcp} Php')
        if fw_entry.get()!='0':
            txt_area.insert(END,f'\nFace Wash\t\t\t{fw_entry.get()}\t\t\t{fwp} Php')
        if hp_entry.get()!='0':
            txt_area.insert(END,f'\nHair Spray\t\t\t{hp_entry.get()}\t\t\t{hsp} Php')
        if hg_entry.get()!='0':
            txt_area.insert(END,f'\nHair Gel\t\t\t{hg_entry.get()}\t\t\t{hgp} Php')
        if bl_entry.get()!='0':
            txt_area.insert(END,f'\nBody Lotion\t\t\t{bl_entry.get()}\t\t\t{blp} Php')

    #Groceries

        if ri_entry.get()!='0':
            txt_area.insert(END,f'\nRice\t\t\t{ri_entry.get()}\t\t\t{bsp} Php')
        if oi_entry.get()!='0':
            txt_area.insert(END,f'\nOil\t\t\t{oi_entry.get()}\t\t\t{fcp} Php')
        if co_entry.get()!='0':
            txt_area.insert(END,f'\nCoffee\t\t\t{co_entry.get()}\t\t\t{fwp} Php')
        if m_entry.get()!='0':
            txt_area.insert(END,f'\nMilk\t\t\t{m_entry.get()}\t\t\t{hsp} Php')
        if s_entry.get()!='0':
            txt_area.insert(END,f'\nSugar\t\t\t{s_entry.get()}\t\t\t{hgp} Php')
        if t_entry.get()!='0':
            txt_area.insert(END,f'\nTea\t\t\t{t_entry.get()}\t\t\t{blp} Php')

    #Cold Drinks

        if ro_entry.get()!='0':
            txt_area.insert(END,f'\nRoyal\t\t\t{ro_entry.get()}\t\t\t{bsp} Php')
        if pe_entry.get()!='0':
            txt_area.insert(END,f'\nPepsi\t\t\t{pe_entry.get()}\t\t\t{fcp} Php')
        if w_entry.get()!='0':
            txt_area.insert(END,f'\nWater\t\t\t{w_entry.get()}\t\t\t{fwp} Php')
        if sp_entry.get()!='0':
            txt_area.insert(END,f'\nSprite\t\t\t{sp_entry.get()}\t\t\t{hsp} Php')
        if gi_entry.get()!='0':
            txt_area.insert(END,f'\nGetorade\t\t\t{gi_entry.get()}\t\t\t{hgp} Php')
        if ck_entry.get()!='0':
            txt_area.insert(END,f'\nCoke\t\t\t{ck_entry.get()}\t\t\t{blp} Php')

    
    #==========================================================================================================================================================================================
    
        txt_area.insert(END,'\n============================================================')
        if ct_entry.get()!='0.0php':
            txt_area.insert(END,f'\nCOSMETIC TAX\t\t\t\t{ct_entry.get()}')

        if gt_entry.get()!='0.0php':
            txt_area.insert(END,f'\nGROCERY TAX\t\t\t\t{gt_entry.get()}')

        if cdt_entry.get()!='0.0php':
            txt_area.insert(END,f'\nDRINKS TAX\t\t\t\t{cdt_entry.get()}')

        txt_area.insert(END,'\n============================================================')

        txt_area.insert(END,f'\nTOTAL:\t\t\t\t{totalbill}Php')


    #==========================================================================================================================================================================================
        txt_area.insert(END,'\n============================================================')
        txt_area.insert(END,'\t\t\t****THANK YOU CUSTOMERS****\n')
        txt_area.insert(END,'\t\t******HAVE A NICE DAY******\n')


    


   

 
#THIRD ROW-----------------------------------------------------------------------------------------------------------------------------------------------------------

#PRODUCT
pr_frame=Frame(root1)
pr_frame.pack()

#COSMETICS COLUMN 0===================================================================================================================================================

c_frame=LabelFrame(pr_frame,text='Cosmetics',font=('arial',15,'bold'),fg='skyblue',bd=8,relief=GROOVE,bg='gray20')
c_frame.grid(row=0,column=0)

#INSIDE COSMETICS

#BATH SOAP
ba_label=Label(c_frame,text='Bath Soap',font=('arial',15,'bold'),fg='white',bg='gray20')
ba_label.grid(row=0,column=0,pady=9,sticky=W)

ba_entry=Entry(c_frame,font=('arial',15,'bold'),bd=5,width=10)
ba_entry.grid(row=0,column=1,pady=9)
ba_entry.insert(0,0)


#FACE CREAM
fa_label=Label(c_frame,text='Face Cream',font=('arial',15,'bold'),fg='white',bg='gray20')
fa_label.grid(row=1,column=0,pady=9,sticky=W)

fa_entry=Entry(c_frame,font=('arial',15,'bold'),bd=5,width=10)
fa_entry.grid(row=1,column=1,pady=9)
fa_entry.insert(0,0)


#FACE WASH
fw_label=Label(c_frame,text='Face Wash',font=('arial',15,'bold'),fg='white',bg='gray20')
fw_label.grid(row=2,column=0,pady=9,sticky=W)

fw_entry=Entry(c_frame,font=('arial',15,'bold'),bd=5,width=10)
fw_entry.grid(row=2,column=1,pady=9)
fw_entry.insert(0,0)


#HAIR SPRAY
hp_label=Label(c_frame,text='Hair Spray',font=('arial',15,'bold'),fg='white',bg='gray20')
hp_label.grid(row=3,column=0,pady=9,sticky=W)

hp_entry=Entry(c_frame,font=('arial',15,'bold'),bd=5,width=10)
hp_entry.grid(row=3,column=1,pady=9)
hp_entry.insert(0,0)


#HAIR GEL
hg_label=Label(c_frame,text='Hair Gel',font=('arial',15,'bold'),fg='white',bg='gray20')
hg_label.grid(row=4,column=0,pady=9,sticky=W)

hg_entry=Entry(c_frame,font=('arial',15,'bold'),bd=5,width=10)
hg_entry.grid(row=4,column=1,pady=9)
hg_entry.insert(0,0)

#BODY LOTION
bl_label=Label(c_frame,text='Body Lotion',font=('arial',15,'bold'),fg='white',bg='gray20')
bl_label.grid(row=5,column=0,pady=9,sticky=W)

bl_entry=Entry(c_frame,font=('arial',15,'bold'),bd=5,width=10)
bl_entry.grid(row=5,column=1,pady=9)
bl_entry.insert(0,0)



#GROCERY COLUMN 1=====================================================================================================================================================
g_frame=LabelFrame(pr_frame,text='Groceries',font=('arial',15,'bold'),fg='skyblue',bd=8,relief=GROOVE,bg='gray20')
g_frame.grid(row=0,column=1)

#INSIDE GROCERY

#RICE
ri_label=Label(g_frame,text='Rice',font=('arial',15,'bold'),fg='white',bg='gray20')
ri_label.grid(row=0,column=2,pady=9,sticky=W)


ri_entry=Entry(g_frame,font=('arial',15,'bold'),bd=5,width=10)
ri_entry.grid(row=0,column=3,pady=9)
ri_entry.insert(0,0)


#OIL
oi_label=Label(g_frame,text='Oil',font=('arial',15,'bold'),fg='white',bg='gray20')
oi_label.grid(row=1,column=2,pady=9,sticky=W)

oi_entry=Entry(g_frame,font=('arial',15,'bold'),bd=5,width=10)
oi_entry.grid(row=1,column=3,pady=9)
oi_entry.insert(0,0)


#COFFEE
co_label=Label(g_frame,text='Coffee',font=('arial',15,'bold'),fg='white',bg='gray20')
co_label.grid(row=2,column=2,pady=9,sticky=W)

co_entry=Entry(g_frame,font=('arial',15,'bold'),bd=5,width=10)
co_entry.grid(row=2,column=3,pady=9)
co_entry.insert(0,0)


#MILK
m_label=Label(g_frame,text='Milk',font=('arial',15,'bold'),fg='white',bg='gray20')
m_label.grid(row=3,column=2,pady=9,sticky=W)

m_entry=Entry(g_frame,font=('arial',15,'bold'),bd=5,width=10)
m_entry.grid(row=3,column=3,pady=9)
m_entry.insert(0,0)


#SUGAR
s_label=Label(g_frame,text='Sugar',font=('arial',15,'bold'),fg='white',bg='gray20')
s_label.grid(row=4,column=2,pady=9,sticky=W)

s_entry=Entry(g_frame,font=('arial',15,'bold'),bd=5,width=10)
s_entry.grid(row=4,column=3,pady=9)
s_entry.insert(0,0)


#TEA
t_label=Label(g_frame,text='Tea',font=('arial',15,'bold'),fg='white',bg='gray20')
t_label.grid(row=5,column=2,pady=9,sticky=W)

t_entry=Entry(g_frame,font=('arial',15,'bold'),bd=5,width=10)
t_entry.grid(row=5,column=3,pady=9)
t_entry.insert(0,0)


#COLD DRINKS COLUMN 2=================================================================================================================================================

d_frame=LabelFrame(pr_frame,text='Cold Drinks',font=('arial',15,'bold'),fg='skyblue',bd=8,relief=GROOVE,bg='gray20')
d_frame.grid(row=0,column=2)

#INSIDE DRINKS

#ROYAL
ro_label=Label(d_frame,text='Royal',font=('arial',15,'bold'),fg='white',bg='gray20')
ro_label.grid(row=0,column=4,pady=9,sticky=W)

ro_entry=Entry(d_frame,font=('arial',15,'bold'),bd=5,width=10)
ro_entry.grid(row=0,column=5,pady=9)
ro_entry.insert(0,0)

#PEPSI
pe_label=Label(d_frame,text='Pepsi',font=('arial',15,'bold'),fg='white',bg='gray20')
pe_label.grid(row=1,column=4,pady=9,sticky=W)

pe_entry=Entry(d_frame,font=('arial',15,'bold'),bd=5,width=10)
pe_entry.grid(row=1,column=5,pady=9)
pe_entry.insert(0,0)


#WATER
w_label=Label(d_frame,text='Water',font=('arial',15,'bold'),fg='white',bg='gray20')
w_label.grid(row=2,column=4,pady=9,sticky=W)

w_entry=Entry(d_frame,font=('arial',15,'bold'),bd=5,width=10)
w_entry.grid(row=2,column=5,pady=9)
w_entry.insert(0,0)


#SPRITE
sp_label=Label(d_frame,text='Sprite',font=('arial',15,'bold'),fg='white',bg='gray20')
sp_label.grid(row=3,column=4,pady=9,sticky=W)

sp_entry=Entry(d_frame,font=('arial',15,'bold'),bd=5,width=10)
sp_entry.grid(row=3,column=5,pady=9)
sp_entry.insert(0,0)


#GETORADE
gi_label=Label(d_frame,text='Getorade',font=('arial',15,'bold'),fg='white',bg='gray20')
gi_label.grid(row=4,column=4,pady=9,sticky=W)

gi_entry=Entry(d_frame,font=('arial',15,'bold'),bd=5,width=10)
gi_entry.grid(row=4,column=5,pady=9)
gi_entry.insert(0,0)


#COKE
ck_label=Label(d_frame,text='Coke',font=('arial',15,'bold'),fg='white',bg='gray20')
ck_label.grid(row=5,column=4,pady=9,sticky=W)

ck_entry=Entry(d_frame,font=('arial',15,'bold'),bd=5,width=10)
ck_entry.grid(row=5,column=5,pady=9)
ck_entry.insert(0,0)


#BILL AREA COLUMN 3===================================================================================================================================================

bill_frame=Frame(pr_frame,bd=10,width=20,relief=GROOVE)
bill_frame.grid(row=0,column=3)

bill_lbl=Button(bill_frame,text='R E C E I P T',font=('Arial',15,'bold'),bg='skyblue',bd=7,relief=GROOVE,command=lambda:bill_area())
bill_lbl.pack(fill=X)

Scrollbar=Scrollbar(bill_frame,orient=VERTICAL)
Scrollbar.pack(side=RIGHT,fill=Y)
txt_area=Text(bill_frame,height=18,width=60,yscrollcommand=Scrollbar.set)
txt_area.pack()
Scrollbar.config(command=txt_area.yview)


#FOURTH ROW------------------------------------------------------------------------------------------------------------------------------------------------------------

#BILL MENU

billmenuframe= LabelFrame(root1,text='BILL MENU',font=('arial',15,'bold'),fg='skyblue',bd=8,relief=GROOVE,bg='gray20')
billmenuframe.pack(fill=X)

#INSIDE BILL MENU

#COLUMN 0==============================================================================================================================================================

#COSMETIC PRICE
cp_label=Label(billmenuframe,text='Cosmetic Price',font=('arial',15,'bold'),fg='white',bg='gray20')
cp_label.grid(row=0,column=1,pady=9,padx=10,sticky=W)

cp_entry=Entry(billmenuframe,font=('arial',15,'bold'),bd=5,width=10)
cp_entry.grid(row=0,column=2,pady=9,padx=10)


#GROCERY PRICE
gp_label=Label(billmenuframe,text='Grocery Price',font=('arial',15,'bold'),fg='white',bg='gray20')
gp_label.grid(row=1,column=1,pady=9,padx=10,sticky=W)

gp_entry=Entry(billmenuframe,font=('arial',15,'bold'),bd=5,width=10)
gp_entry.grid(row=1,column=2,pady=9,padx=10)


#COLD DRINK PRICE
cdp_label=Label(billmenuframe,text='Cold Drink Price',font=('arial',15,'bold'),fg='white',bg='gray20')
cdp_label.grid(row=2,column=1,pady=9,padx=10,sticky=W)

cdp_entry=Entry(billmenuframe,font=('arial',15,'bold'),bd=5,width=10)
cdp_entry.grid(row=2,column=2,pady=9,padx=10)



#COLUMN 1===============================================================================================================================================================

#COSMETIC TAX
ct_label=Label(billmenuframe,text='Cosmetic Tax',font=('arial',15,'bold'),fg='white',bg='gray20')
ct_label.grid(row=0,column=3,pady=9,padx=10,sticky=W)

ct_entry=Entry(billmenuframe,font=('arial',15,'bold'),bd=5,width=10)
ct_entry.grid(row=0,column=4,pady=9,padx=10)


#GROCERY TAX
gt_label=Label(billmenuframe,text='Grocery Tax',font=('arial',15,'bold'),fg='white',bg='gray20')
gt_label.grid(row=1,column=3,pady=9,padx=10,sticky=W)

gt_entry=Entry(billmenuframe,font=('arial',15,'bold'),bd=5,width=10)
gt_entry.grid(row=1,column=4,pady=9,padx=10)


#COLD DRINK TAX
cdt_label=Label(billmenuframe,text='Cold Drink Tax',font=('arial',15,'bold'),fg='white',bg='gray20')
cdt_label.grid(row=2,column=3,pady=9,padx=10,sticky=W)

cdt_entry=Entry(billmenuframe,font=('arial',15,'bold'),bd=5,width=10)
cdt_entry.grid(row=2,column=4,pady=9,padx=10)


#COLUMN 2==============================================================================================================================================================

#INSIDE COLUMN 2 ROW 4
btnframe=Frame(billmenuframe,bd=8,relief=GROOVE)
btnframe.grid(row=0,column=5,rowspan=3)

#TOTAL
totalbtn=Button(btnframe,text='Total',font=('arial',16,'bold'),bg='skyblue',fg='black',bd=5,width=8,command=lambda: total())
totalbtn.grid(row=0,column=0,pady=20,padx=1)

#BILL
billbtn=Button(btnframe,text='Save',font=('arial',16,'bold'),bg='skyblue',fg='black',bd=5,width=8,command=lambda:save_bill())
billbtn.grid(row=0,column=1,pady=20,padx=1)

#EMAIL
#emailbtn=Button(btnframe,text='Email',font=('arial',16,'bold'),bg='skyblue',fg='black',bd=5,width=8)
#emailbtn.grid(row=0,column=2,pady=20,padx=1)

#SHOW
showbtn=Button(btnframe,text='Show',font=('arial',16,'bold'),bg='skyblue',fg='black',bd=5,width=8)
showbtn.grid(row=0,column=3,pady=20,padx=1)

#CLEAR
clrbtn=Button(btnframe,text='Clear',font=('arial',16,'bold'),bg='skyblue',fg='black',bd=5,width=8,command=lambda:clear())
clrbtn.grid(row=0,column=2,pady=20,padx=1)

#EXIT
exitbtn= Button(btnframe,text='EXIT',fg='black',font=('arial',16,'bold'),bg='red',bd=5,width=8,command=lambda:exit())
exitbtn.grid(row=0,column=4,pady=20,padx=1)

















root1.mainloop()







