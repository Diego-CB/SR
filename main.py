''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  main.py
  - main program to write files
  
  Last modified (yy-mm-dd): 2022-09-12
--------------------------------------
'''

if __name__ == '__main__':
  from Drivers import *
  from time import sleep
  
  def bye():
    print('Software Renderer ended succesfully!!\n')

  renders = {
    's': bye,
    '1': Mario_medium,
    '2': Mario_lowangle,
    '3': Mario_highangle,
    '4': Mario_dutch,
  }
  option_menu = ('\n' +
    'Seleccione un render:\n' +
    '1. Medium Shot\n' +
    '2. Low Angle\n' +
    '3. High Angle\n' +
    '4. Dutch Angle\n' +
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
