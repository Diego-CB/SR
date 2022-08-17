''' 
--------------------------------------
  Universidad del Valle de Guatemala
  Author: Diego Cordova - 20212

  main.py
  - main program to write files
  
  Last modified (yy-mm-dd): 2022-08-08 
--------------------------------------
'''

if __name__ == '__main__':
  from Drivers import *
  from time import sleep

  def bye():
    print('Software Renderer ended succesfully!!\n')

  renders = {
    's': bye,
    '1': Mario,
    '2': Yoshi,
    '3': Tmap_Mario,
    '4': Tmap_Yoshi,
    '5': Face,
    '6': Tmap_Face
  }

  op = None
  while op != 's':
    op = input('\n' +
      'Seleccione un render:\n' +
      '1. Render de Mario.obj\n' +
      '2. Render de Yoshi.obj\n' +
      '3. Texture map de Mario.obj y sus texturas\n' +
      '4. Texture map de Yoshi.obj y sus texturas\n' +
      '5. Render de Face.obj\n' +
      '6. Texture map de Face.obj y sus texturas\n' +
      's. Salir\n' +
      ' -> '
    )

    try:
      renders[op]()
    except KeyError:
      print('Error: Seleccione una opcion valida')

    sleep(1)
