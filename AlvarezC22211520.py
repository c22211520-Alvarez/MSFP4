"""
Práctica Cuatro: Sistema Endócrino

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Gabriela Gissele Alvarez Garcia
Número de control: C22211520
Correo institucional: c22211520@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Instalar librerias en consola
#!pip install control
#!pip install slycot

# Librerías para cálculo numérico y generación de gráficas

import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# Datos de la simulación
x0,t0,tend,dt,w,h = 0,0,10,1E-3,7,3.5 #tiempo obtenido
N = round((tend-t0)/dt)+1
t = np.linspace(t0,tend,N)
u = np.ones(N)

#Funcion para entregar las funciones de transferencia segun el caso
def casos(R2,Cs):
    R1,Ls=1e3,100e-3
    
    # Componentes del circuito RC y función de transferencia
    num = [Ls,R2]
    den = [Cs*Ls*R1,(Cs*R1*R2)+Ls,R1+R2]
    sys = ctrl.tf(num, den)
    # Polos del sistema
    L= np.roots(den)
    return sys,L

#Funcion de transferencia del control
R2,Cs= 100e3,1e-6
sysControl,L = casos(R2,Cs)
print(f"Funcion de transferencia del control:{sysControl}")
print(f"Polos del sistema: L1 = {L[0]:.3e}, L2= {L[1]:.3e}\n")
#llamar funcion de transferencia del caso
R2,Cs= 1e3,1000e-6
sysCaso,L = casos(R2,Cs)
print(f"Funcion de transferencia del control:{sysCaso}")
print(f"Polos del sistema: L1 = {L[0]:.3e}, L2= {L[1]:.3e}\n")


# Componentes del controlador PI
kP,kI,kD =259.66355715696,12483.0782650462,0.173851580929407
Cr = 1e-6
Re = 1/(kI*Cr)
Rr = kP*Re
Ce = kD/Rr
numPID = [Re*Rr*Ce*Cr,Re*Ce + Rr*Cr,1]
denPID = [Re*Cr,0]
PID = ctrl.tf(numPID, denPID)

# Sistema de control en lazo cerrado
print(f"Capacitancia Cr: {Cr} Faradios \n")
print(f"Resistencia Re: {Re} Ohms \n")
print(f"Resistencia Rr: {Rr} Ohms \n")
print(f"Resistencia Ce: {Ce} Faradios \n")
print(f"Funcion de transferencia del caso en lazo cerrado: {PID} \n")

#Colores
clr1 = np.array([80,3,192])/255
clr3 = np.array([171,3,169])/255
clr2 = np.array([255,213,30])/255
clr4 = np.array([157, 2, 235])/255

#Funciones del sistema en lazo abierto y lazo cerrado
_,Vsx = ctrl.forced_response(sysControl,t,u,x0) #Control
_,Vsy = ctrl.forced_response(sysCaso,t,u,x0) #Caso

sysPID=ctrl.feedback(ctrl.series(PID,sysCaso),1,sign =-1) #Pi con caso
_,PID = ctrl.forced_response(sysPID,t,Vsx,x0) #PI Tratamiento usando control 

    
# Respuestas: Simulaciones numéricas
fg = plt.figure(1)
fg.set_size_inches(w,h)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.plot(t,u,'-',linewidth=1.0,color=clr4,label='Ve(t)')
plt.plot(t,Vsx,'--',linewidth=1.0,color=clr1,label='Vs(t) Control')
plt.plot(t,Vsy,'-',linewidth=1.0,color=clr2,label='Vs(t) Caso')
plt.plot(t,PID,':',linewidth=1.5,color=clr3,label='PID(t) Tratamiento')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(-0.1,1.1); plt.yticks(np.arange(-0.1,1.1,0.1))
plt.xlabel('t [s]')
plt.ylabel('V(t) [V]')
plt.legend(bbox_to_anchor=(0.5,-0.25),loc='center',ncol=4,frameon=False)
plt.show()
fg.savefig('Tratamiento_python.pdf',bbox_inches='tight')
    