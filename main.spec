# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Christian\\Desktop\\cgt-soft\\VENVs\\sw-rune-py35\\lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\Christian\\Desktop\\cgt-soft\\sw-rune'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon = 'swrc.ico')
