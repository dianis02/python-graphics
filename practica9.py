'''
Practica 9
Ramírez García Diana Isabel
'''
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation







'''Desempleo'''
'''
Se realizo una grafica para ver el comportamiento del desempleo
(creciente/decreciente )
Para esta se busco los porcentajes y estos formaron los puntos Y
Finalmente se puso etiquetas sobre los anios en el eje X
'''


plt.plot([1,2,3,4,5,6,7,8,9,10], [4.5,5.3, 5.3,5,5,4.8,4.5,4.3,3.6,3.3], 'rs--')

plt.xlabel('anios')
plt.ylabel('porcentaje')
plt.xticks(np.arange(0, 12, 1),('2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017'))
plt.title("Tasa de desempleo Nacional en los ultimos 10 anios")


'''------------------------------------------------------------------'''
''''Idiomas regiones Grafica de barras'''

'''
Se definieron 6 barras (una inexistente) para que te tal manera hubiese
espacio para las etiquetas de los idiomas hablados.
Se realizo una lista de cada idioma con sus porcentajes.
Se les dio formato a las barras (color, ancho y se utilizo bottom para
juntar los valores de los idiomas por region y nos diera el 100% en cada
barra, a este se le paso una lista
finalmente se puso etiquetas

'''


barras = 6

spanish=(9,58,6,0,0,0)
english=(70,1,8,4,0,0)
french=(3,0,8,6,0,0)
chinese=(1,0,0,0,34,0)
other=(17,6,17,58,34,0)
portuguese=(0,33,0,0,0,0)
creole=(0,2,0,0,0,0)
russian=(0,0,22,0,0,0)
german=(0,0,12,0,0,0)
turkish=(0,0,9,0,0,0)
italian=(0,0,8,0,0,0)
polish=(0,0,6,0,0,0)
ukrainian=(0,0,4,0,0,0)
arabic=(0,0,0,17,0,0)
swahili=(0,0,0,8,0,0)
kwa=(0,0,0,4,0,0)
hausa=(0,0,0,3,0,0)
hindustani=(0,0,0,0,12,0)
bengali=(0,0,0,0,8,0)
indonesian=(0,0,0,0,6,0)
japanese=(0,0,0,0,3,0)
punjabi=(0,0,0,0,3,0)


fig, ax = plt.subplots()
index = np.arange(barras)
bar_width = 0.35
estilo_error = {'ecolor': '0.5'}


plt.bar(index, other, bar_width,alpha=1,color='#DC143C',bottom=[83,92,83,42,66,0], yerr=2.5, error_kw=estilo_error,label='other')
plt.bar(index, english, bar_width,alpha=1,color='#7A378B',bottom=[0,91,43,31,0,0], yerr=2.5, error_kw=estilo_error,label='english')
plt.bar(index, spanish, bar_width,alpha=1,color='#00F5FF',bottom=[70,0,73,0,0,0], yerr=2.5, error_kw=estilo_error,label='spanish')
plt.bar(index, french, bar_width,alpha=1,color='y',bottom=[79,0,59,25,0,0], yerr=2.5, error_kw=estilo_error,label='french')
plt.bar(index, chinese, bar_width,alpha=0.4,color='r',bottom=[82,0,0,0,0,0], yerr=2.5, error_kw=estilo_error,label='chinese')
plt.bar(index, portuguese, bar_width,alpha=0.4,color='y',bottom=[0,58,0,0,0,0], yerr=2.5, error_kw=estilo_error,label='portuguese')
plt.bar(index, creole, bar_width,alpha=1,color='r',bottom=[0,98,0,0,0,0], yerr=2.5, error_kw=estilo_error,label='creole')
plt.bar(index, russian, bar_width,alpha=0.4,color='g',bottom=[0,0,0,0,0,0], yerr=2.5, error_kw=estilo_error,label='russian')
plt.bar(index, german, bar_width,alpha=0.4,color='#00BFFF',bottom=[0,0,22,0,0,0], yerr=2.5, error_kw=estilo_error,label='german')
plt.bar(index, turkish, bar_width,alpha=1,color='#EE7600',bottom=[0,0,34,0,0,0], yerr=2.5, error_kw=estilo_error,label='turkish')
plt.bar(index, italian, bar_width,alpha=1,color='#0000CD',bottom=[0,0,51,0,0,0], yerr=2.5, error_kw=estilo_error,label='italian')
plt.bar(index, polish, bar_width,alpha=1,color='#FF1493',bottom=[0,0,67,0,0,0], yerr=2.5, error_kw=estilo_error,label='polish')
plt.bar(index, ukrainian, bar_width,alpha=1,color='#3CB371',bottom=[0,0,79,0,0,0], yerr=2.5, error_kw=estilo_error,label='ukrainian')
plt.bar(index,arabic , bar_width,alpha=1,color='#CDCD00',bottom=[0,0,0,0,0,0], yerr=2.5, error_kw=estilo_error,label='arabic')
plt.bar(index,swahili , bar_width,alpha=1,color='#EE9572',bottom=[0,0,0,17,0,0], yerr=2.5, error_kw=estilo_error,label='swahili')
plt.bar(index,kwa, bar_width,alpha=1,color='#00FA9A',bottom=[0,0,0,35,0,0], yerr=2.5, error_kw=estilo_error,label='kwa')
plt.bar(index,hausa , bar_width,alpha=1,color='#FFC0CB',bottom=[0,0,0,39,0,0], yerr=2.5, error_kw=estilo_error,label='hausa')
plt.bar(index, hindustani, bar_width,alpha=1,color='#308014',bottom=[0,0,0,0,34,0], yerr=2.5, error_kw=estilo_error,label='hindustani')
plt.bar(index, bengali, bar_width,alpha=1,color='#FF4040',bottom=[0,0,0,0,46,0], yerr=2.5, error_kw=estilo_error,label='bengali')
plt.bar(index, indonesian, bar_width,alpha=1,color='#388E8E',bottom=[0,0,0,0,54,0], yerr=2.5, error_kw=estilo_error,label='indonesian')
plt.bar(index, japanese, bar_width,alpha=1,color='#FF00FF',bottom=[0,0,0,0,60,0], yerr=2.5, error_kw=estilo_error,label='japanese')
plt.bar(index, punjabi, bar_width,alpha=1,color='#C67171',bottom=[0,0,0,0,63,0], yerr=2.5, error_kw=estilo_error,label='punjabi')
              
plt.xlabel('idiomas')
plt.ylabel('Porcentajes')
plt.title('Idiomas mas hablados por regiones')


plt.xticks(index + bar_width,('america norte', 'latinoamerica', 'europa', 'africa','asia y pacifico'))
plt.yticks(np.arange(0, 201, 10))
plt.legend()




'''------------------------------------------------------------------'''

'''Grafica de Pastel de Idiomas'''


'''
Se calculo el porcentaje de cada idioma de que tan hablado es en el 
mundo y estos fueron los porcentajes dados a la grafica de pastel
'''

labels = 'spanish','english','french','chinese','other','portuguese','creole','russian','german','turkish','italian','polish','ukrainian','arabic','swahili','kwa','hausa','hindustani','bengali','indonesian','japanese','punjabi'

sizes = [14.6,16.6,3.4,7,26,6.6,0.4,4.4,2.4,1.8,1.6,1.2,0.8,3.4,1.6,0.8,0.6,2.4,1.6,1.2,0.6,0.6]

#explode = (0.3, 0, 0, 0, 0, 0)

f, ax1 = plt.subplots()

ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

ax1.axis('equal')
plt.title("Porcentaje idiomas del mundo")






'''------------------------------------------------------------------'''

'''Coordenadas Polares'''
'''
Se buscaron las ecuaciones de las graficas en terminos polares
,se definio una theta y 2 r's paralas dos graficas respectibvamente
se utilizo subplots de tal forma que ambas graficas aparezcan en una 
ventana
'''


a = 1.
theta = np.linspace(0,2*np.pi,1000)
r1 = 4*np.cos(4*theta)
r2= 3*np.cos(3*theta)

f, axarr = plt.subplots(2, subplot_kw=dict(projection='polar'))
axarr[0].plot(theta, r1)
axarr[1].plot(theta, r2)




'''------------------------------------------------------------------'''
'''Solido de Revolucion'''
'''
Se busco la ecuacion del paraboloide en terminos de cos y sin
las cuales representan x y y

'''

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

u = np.linspace(0, 2*np.pi, 60)
v = np.linspace(0, 2*np.pi, 60)
U, V = np.meshgrid(u, v)

Z = U
X = np.sqrt(U)*np.cos(V)
Y = np.sqrt(U)*np.sin(V)

ax.plot_surface(X, Y, Z, alpha=0.3, color='red')




'''------------------------------------------------------------------'''

'''Animacion'''
'''
Se realizo una grafica dando unos puntos en especificos para simular
un electro cardiograma
'''

ax = plt.subplot(111, axisbg='black')
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot([1, 1.5, 2, 2.5, 3,3.5],[2, 4,1 , 3, 2,2], 'g')
plt.xticks(np.arange(-2, 5, 1))



fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(-1, 3))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    line.set_color('green')
    ax.patch.set_facecolor('black')
    return line,

def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

anim=FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=10, blit=False)




plt.show()









