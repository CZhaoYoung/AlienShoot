# -*- mode: python -*-

block_cipher = None


a = Analysis(['alien_invasion.py'],
             pathex=['D:\\pycharm\\AlienShoot'],
             binaries=[],
             datas=[],
             hiddenimports=['alien', 'bullet', 'Button', 'game_functions', 'game_stats', 'scoreboard', 'settings', 'ship'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += (('alien.bmp','D:\\pycharm\\AlienShoot\\images\\alien.bmp,'DATA'),
('ship.bmp','D:\\pycharm\\AlienShoot\\images\\ship.bmp','DATA'))

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='alien_invasion',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
