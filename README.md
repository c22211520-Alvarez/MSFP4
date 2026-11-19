[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=c22211520-Alvarez/MSFP4)
# Práctica 4: Modelado y control del sistema endócrino

Repositorio académico de la asignatura **Modelado de Sistemas Fisiológicos**, correspondiente al programa de **Ingeniería Biomédica** del Tecnológico Nacional de México / Instituto Tecnológico de Tijuana. Esta práctica integra el modelado matemático mediante analogías eléctricas, el análisis de estabilidad, el diseño de controladores clásicos, la experimentación *in silico* (Simulink y Python) y la comprobación física en el Laboratorio de Electrónica enfocada en el sistema endócrino.

El caso de estudio representa la dinámica de secreción, transporte y respuesta hormonal mediante un circuito eléctrico equivalente de segundo orden. Se compara la respuesta de un individuo sano (control) frente a un caso simulado de alteración endócrina, aplicando un controlador PI/PID para mitigar la diferencia entre ambas respuestas.

**Docente:** Dr. Paul Antonio Valle Trujillo  
**Correo:** paul.valle@tectijuana.edu.mx  
**Departamento:** Ingeniería Eléctrica y Electrónica  
**Institución:** Tecnológico Nacional de México / Instituto Tecnológico de Tijuana  
**Asignatura:** Modelado de Sistemas Fisiológicos  
**Programa:** Ingeniería Biomédica  
**Estudiante:** Gabriela Gissele Alvarez Garcia · C22211520 · c22211520@tijuana.tecnm.mx

**Repositorio de la asignatura:** https://github.com/DrPaulValle/MSF-IBF1020  
**Sede:** Blvd. Alberto Limón Padilla s/n, Tijuana, C. P. 22454, B. C., México.

---

<a id="contenido"></a>
## Contenido

1. [Resumen](#resumen)
2. [Competencia y objetivos](#objetivos)
3. [Relación con el temario](#temario)
4. [Modelo físico y analogía eléctrica](#analogia)
5. [Formulación matemática](#modelo)
6. [Análisis temporal y de estabilidad](#analisis)
7. [Señales de entrada y condiciones de simulación](#senales)
8. [Implementación en MATLAB, Simulink y Simscape](#matlab)
9. [Control en lazo cerrado y sintonización](#pid)
10. [Reproducción en Python](#python)
11. [Controlador analógico y laboratorio](#laboratorio)
12. [Resultados y verificación cruzada](#resultados)
13. [Diagrama Fisiológico (BioRender)](#biorender)
14. [Referencias](#referencias)

---

<a id="resumen"></a>
## Resumen

El modelado de sistemas fisiológicos permite comprender la dinámica del cuerpo humano y evaluar estrategias de control. En esta práctica, se analiza una representación fenomenológica del sistema endócrino. El sistema considera una señal de entrada que estimula la secreción hormonal, un elemento resistivo que representa pérdidas, un capacitor que simula la acumulación temporal de la hormona y una rama inductiva-resistiva que representa el retardo o inercia de la respuesta del tejido diana.

Mediante la **analogía eléctrica**, se evalúan dos condiciones fisiológicas: un individuo sano (control, $R_2 = 100\text{ k}\Omega$, $C = 1\ \mu\text{F}$) y un caso simulado de alteración (caso, $R_2 = 1\text{ k}\Omega$, $C = 1000\ \mu\text{F}$). Utilizando la respuesta del individuo sano como referencia, se diseña un controlador para reducir el error. El desarrollo se realiza *in silico* mediante MATLAB/Simulink y Python, y se contrasta con la implementación física en el laboratorio de electrónica, complementado con un diagrama fisiológico elaborado en BioRender.

**Palabras clave:** Sistema endócrino; Analogía eléctrica; Secreción hormonal; Controlador PI/PID; Simscape Electrical; Python; BioRender; Laboratorio de electrónica.

[Volver al contenido](#contenido)

---

<a id="objetivos"></a>
## Competencia y objetivos

### Competencia a desarrollar
Modeliza sistemas fisiológicos mediante analogías eléctricas, ecuaciones diferenciales y funciones de transferencia para analizar su comportamiento dinámico y diseña estrategias de control mediante técnicas de control clásico.

### Objetivos específicos
- Analizar la descripción funcional del sistema endócrino y proponer su circuito eléctrico equivalente.
- Obtener el modelo de ecuaciones integro-diferenciales y la función de transferencia del control y del caso.
- Evaluar la estabilidad y el error en estado estacionario de ambos escenarios.
- Implementar el modelo en Simulink (ecuaciones, función de transferencia y circuito) y Python.
- Sintonizar un controlador PI/PID para reducir la diferencia entre el caso alterado y la referencia sana.
- Elaborar un diagrama biológico del sistema en BioRender.
- Implementar el controlador analógico y el circuito en el laboratorio físico.

[Volver al contenido](#contenido)

---

<a id="temario"></a>
## Relación con el temario

La práctica integra contenidos correspondientes a tres unidades de la asignatura **Modelado de Sistemas Fisiológicos (IBF-1020)**:
- **Unidad I (Sistemas de control retroalimentados):** Análisis de error, estabilidad y diagramas de bloques.
- **Unidad II (Modelado matemático):** Analogía eléctrica del sistema endócrino, leyes de Kirchhoff y función de transferencia.
- **Unidad III (Controladores):** Diseño y sintonización de controladores clásicos (PI/PID).

[Volver al contenido](#contenido)

---

<a id="analogia"></a>
## Modelo físico y analogía eléctrica

El sistema endócrino se aproxima mediante un circuito eléctrico cuyas equivalencias principales son:

| Parámetro | Control (Sano) | Caso (Alterado) | Interpretación Fisiológica |
| :--- | :---: | :---: | :--- |
| **$V_e(t)$** | Escalón unitario | Escalón unitario | Estímulo para la secreción hormonal |
| **$R_1$** | $1\ \text{k}\Omega$ | $1\ \text{k}\Omega$ | Pérdidas y oposición durante el transporte |
| **$C$** | $1\ \mu\text{F}$ | $1000\ \mu\text{F}$ | Acumulación temporal de hormona |
| **$L$** | $100\ \text{mH}$ | $100\ \text{mH}$ | Retardo o inercia de la respuesta del tejido diana |
| **$R_2$** | $100\ \text{k}\Omega$ | $1\ \text{k}\Omega$ | Utilización, disipación o eliminación de la señal |

*La modificación de R2 y C en el caso altera la dinámica de la respuesta hormonal.*

[Volver al contenido](#contenido)

---

<a id="modelo"></a>
## Formulación matemática

A partir del análisis del circuito equivalente, aplicando las leyes de Kirchhoff, se obtienen las ecuaciones integro-diferenciales que rigen el sistema:

**1. Ecuación de voltaje en la entrada:**
$$
V_e(t) = R_1 F_e(t) + \frac{1}{C} \int (F_e(t) - F_s(t)) \, dt
$$

**2. Ecuación de voltaje en la salida:**
$$
V_s(t) = L \frac{dF_s(t)}{dt} + R_2 F_s(t) = \frac{1}{C} \int (F_e(t) - F_s(t)) \, dt
$$

### Procedimiento Algebraico (Transformada de Laplace)

Aplicando Laplace con condiciones iniciales nulas y agrupando términos:

$$
V_e(s) = F_e(s) \left( R_1 + \frac{1}{Cs} \right) - F_s(s) \left( \frac{1}{Cs} \right)
$$

$$
V_s(s) = F_s(s)(Ls + R_2) = F_e(s)\left(\frac{1}{Cs}\right) - F_s(s)\left(\frac{1}{Cs}\right)
$$

Despejando $F_e(s)$ de la segunda ecuación y sustituyendo en la primera, se obtiene:

$$
F_e(s) = F_s(s) (CLs^2 + CsR_2 + 1)
$$

Sustituyendo en $V_e(s)$ y simplificando, llegamos a la **Función de Transferencia** final:

$$
G(s) = \frac{V_s(s)}{V_e(s)} = \frac{Ls + R_2}{CLs^2 R_1 + (CR_1 R_2 + L)s + (R_1 + R_2)}
$$

### Ecuación Diferencial (EDO)

Invirtiendo la función de transferencia, la EDO que rige la dinámica del sistema es:

$$
CL R_1 \frac{d^2 V_s(t)}{dt^2} + (CR_1 R_2 + L) \frac{d V_s(t)}{dt} + (R_1 + R_2) V_s(t) = L \frac{d V_e(t)}{dt} + R_2 V_e(t)
$$

[Volver al contenido](#contenido)

---

<a id="analisis"></a>
## Análisis temporal y de estabilidad

- **Polos y estabilidad:** El denominador de la función de transferencia es de segundo grado. Al sustituir los valores de los componentes para ambos casos, los polos se encuentran en el semiplano izquierdo del plano complejo $s$, garantizando un sistema estable.
- **Error en estado estacionario:** Al evaluar el límite de $sG(s)$ cuando $s \to 0$, el sistema se comporta como un sistema tipo 1 (integrador), por lo que el error teórico ante una entrada escalón es cero.
- **Diferencia dinámica:** El caso alterado (con $C=1000\ \mu\text{F}$) presentará una respuesta mucho más lenta (mayor constante de tiempo) y con mayor amplitud que el control sano.

[Volver al contenido](#contenido)

---

<a id="implementacion"></a>
## Implementación en MATLAB, Simulink y Simscape

Se construyeron las siguientes representaciones equivalentes en Simulink:
1. **Ecuaciones integro-diferenciales:** Mediante bloques de suma, ganancia e integración.
2. **Función de transferencia:** Usando el bloque `Transfer Fcn` con la ecuación obtenida.
3. **Circuito equivalente:** Mediante componentes eléctricos en `Simscape Electrical`.

[Volver al contenido](#contenido)

---

<a id="pid"></a>
## Control en lazo cerrado y sintonización

Se implementó un controlador en Simulink con retroalimentación negativa. La señal de error se define como:
$$
e(t) = V_{s,\text{control}}(t) - V_{s,\text{caso}}(t)
$$

**Ganancias Sintonizadas (Herramienta Tune):**
- **$k_P$:** `259.663557`
- **$k_I$:** `12483.078265`
- **$k_D$:** `0.173851`


[Volver al contenido](#contenido)

---

<a id="python"></a>
## Reproducción en Python

Se implementó el siguiente código en Python (usando `control` y `matplotlib`) para verificar los resultados:
1. Definición del vector temporal con un paso de $1\times10^{-3}$ s.
2. Definición de las funciones de transferencia para el control y el caso.
3. Simulación de la respuesta en lazo abierto ante un escalón unitario.
4. Incorporación del controlador y simulación del lazo cerrado (usando `ctrl.feedback`).
5. Generación y almacenamiento de las gráficas comparativas.

[Volver al contenido](#contenido)

---

<a id="laboratorio"></a>
## Controlador analógico y laboratorio

### Materiales y equipo
- Resistencias ($1\text{k}\Omega$, $100\text{k}\Omega$, y las calculadas para el PID).
- Capacitores ($1\ \mu\text{F}$, $1000\ \mu\text{F}$, y los del PID).
- Inductor de $100\ \text{mH}$ (o el valor comercial disponible).
- Amplificadores operacionales (LM741 o TL081).
- Generador de funciones, fuente de alimentación simétrica ($\pm15\text{V}$) y osciloscopio.

### Implementación
1. **Lazo Abierto:** Se construyó el circuito Caso y el circuito Control por separado. Se aplicó un pulso o escalón y se registraron las salidas.
2. **Lazo Cerrado:** Se construyó el restador (usando un buffer/seguidor de voltaje para el control), el controlador analógico (PI) y el sumador para inyectar la señal al circuito Caso.
3. **Comparación:** Se analizaron las diferencias entre la simulación y el circuito físico, atribuyendo las discrepancias a las tolerancias de los componentes, la resistencia interna del inductor y las limitaciones de los amplificadores operacionales.

[Volver al contenido](#contenido)

---

<a id="resultados"></a>
## Resultados y verificación cruzada

- **Línea Control (Sana):** Alcanza el valor de referencia.
- **Línea Caso (Lazo abierto):** Presenta una dinámica más lenta y menor amplitud.
- **Línea Tratamiento (Caso con PI):** Logra estabilizarse y alcanza la referencia impuesta por el control, demostrando la eficacia del lazo cerrado.
- Se verificó que las gráficas obtenidas en MATLAB, Simulink y Python son consistentes entre sí, validando el modelo matemático antes de la implementación física.

[Volver al contenido](#contenido)

---

<a id="biorender"></a>
## Diagrama Fisiológico (BioRender)

Se elaboró un diagrama del sistema endócrino utilizando la plataforma **BioRender**. 
En este diagrama se ilustra:
- La glándula secretora y el torrente sanguíneo (transporte).
- El órgano diana y los receptores.
- La retroalimentación negativa fisiológica.
- El mapeo de los componentes: $V_e$ (estímulo), $R_1$ (transporte), $C$ (almacenamiento/acumulación), $L$ (inercia de respuesta del órgano diana) y $R_2$ (eliminación/utilización).

*El archivo PDF original del diagrama se encuentra anexado en este repositorio.*

[Volver al contenido](#contenido)

---

<a id="referencias"></a>

Referencias
[1] M. C. Khoo, Physiological Control Systems: Analysis, Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018.
[2] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026.
[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.
[4] K. Ogata, Ingeniería de Control Moderna, 5a ed. Pearson Educación, 2010.
