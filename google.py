from sys import argv
from os import path
import webbrowser

def main( ):
   if len( argv ) < 2:
      print( f'Usage: {__file__} <Google search query>' )
      exit( )
      
   print( f'Searching Google for \"' + ' '.join( argv[ 1: ] ) + '\"' )

   chromePath = path.basename( '/mnt/c/Program Files/Google/Chrome/Application/chrome.exe' )
   if not path.exists( chromePath ):
      print( 'Cannot find Chrome' )
      exit( )

   # Assemble URL
   url = f'http://www.google.com/search?q={argv[ 1 ]}'
   for arg in argv[ 2: ]:
      url += f'+{arg}'

   # Second parameter '2' indicates open a new tab if possible
   webbrowser.get( chromePath ).open( url, 2 )

if __name__ == '__main__':
   main( )