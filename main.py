''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  main.py
  - main program to write files
  
  Last modified (yy-mm-dd): 2022-08-23
--------------------------------------
'''

if __name__ == '__main__':
  from Drivers import *
  from time import sleep
  Face()

else:
  def bye():
    print('Software Renderer ended succesfully!!\n')

  renders = {
    's': bye,
    '1': Mario,
    '2': Yoshi,
    '3': Face
  }
  option_menu = ('\n' +
    'Seleccione un render:\n' +
    '1. Render de Mario.obj\n' +
    '2. Render de Yoshi.obj\n' +
    '3. Render de Face.obj\n' +
    's. Salir\n' +
    ' -> '
  )
  
  option = None
  while option != 's':
    option = input(option_menu)

    try:
      renders[option]()
      sleep(1)

    except KeyError:
      print('Error: Seleccione una opcion valida')
