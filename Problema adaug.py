# se da o suma de lei sa se converteasca suma data intrun numar minim de bancnote Nota in Rm exista bancnote de 1000 500 200 100 50 20 10 5 2 1
a=int(input("Introduceti suma:"))
b=a//1000
c=(a-(b*1000))//500
d=(a-(b*1000)-(c*500))//200
e=(a-(b*1000)-(c*500)-(d*200))//100
f=(a-(b*1000)-(c*500)-(d*200)-(e*100))//50
g=(a-(b*1000)-(c*500)-(d*200)-(e*100)-(f*50))//20
h=(a-(b*1000)-(c*500)-(d*200)-(e*100)-(f*50)-(g*20))//10
i=(a-(b*1000)-(c*500)-(d*200)-(e*100)-(f*50)-(g*20)-(h*10))//5
j=(a-(b*1000)-(c*500)-(d*200)-(e*100)-(f*50)-(g*20)-(h*10)-(i*5))//2
k=(a-(b*1000)-(c*500)-(d*200)-(e*100)-(f*50)-(g*20)-(h*10)-(i*5)-(j*2))//1
print (b,"Bancnote de 1000 lei",c,"bancnote de 500 lei",d,"bancnote de 200 lei",e,"bancnote de 100 lei",f,"bancnote de 50 lei",g,"Bancnote de 20 lei",h,"bancnote de 10 lei",i,"bancnote de 5 lei",j,"bancnote de 2 lei",h,"bancnote de 1 lei")