#from calculos.funciones_matematicos import *
from calculos.funciones_matematicos import suma, resta
from calculos.basicos.multiplicacion_division import multiplicacion, division

print("Uso de paquetes")
suma(14, 5)
resta(20, 6)
multiplicacion(7, 3)

#comandos
#py .\uso_paquetes.py
#pip --version
#pip freeze #verificar paquetes que instale
#py .\setup.py sdist  #carpeta raiz proyecto
#pip install .\paquetecalculo-1.0.tar.gz #en la carpeta dist
#pip uninstall paquetecalculo  #Borrar paquetes que instale
#----
##pip install requests==2.28.2 #instalar libreria con version
#---Entorno virtual
#py -m venv venv #genera entorno virtual
#cd .\venv\Scripts\
#.\activate #activar entorno virtual
#pip freeze
#pip install #instalar en el script del entorno virtual
#pip freeze > requirements.txt #va en la raiz del proyecto

#crear el requerimiento
#py -m venv venv #genera entorno virtual
#cd .\venv\Script\
#.\activate #dentro de script
#pip freeze
#pip install -r .\requirements.txt

