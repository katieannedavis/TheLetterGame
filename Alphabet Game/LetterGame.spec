# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py','GameFunctions.py', 'GameBoard.py'],
             pathex=['C:\\Users\\katie\\OneDrive\\Documents\\pythonPrograms\\Alphabet Game'],
             binaries=[],
             datas=[('C:\\Users\\katie\\OneDrive\\Documents\\pythonPrograms\\Alphabet Game\\letters\\*.mp3','letters'), ('C:\\Users\\katie\\OneDrive\\Documents\\pythonPrograms\\Alphabet Game\\icon.ico', '.'), ('C:\\Users\\katie\\OneDrive\\Documents\\pythonPrograms\\Alphabet Game\\ABC_Sloth.jpg', '.'), ('C:\\Users\\katie\\OneDrive\\Documents\\pythonPrograms\\Alphabet Game\\exit.png','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['numpy', 'multiprocessing'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          exclude_binaries=True,
          name='LetterGame',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='C:\\Users\\katie\\OneDrive\\Documents\\pythonPrograms\\Alphabet Game\\icon.ico')
