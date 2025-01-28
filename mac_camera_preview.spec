# -*- mode: python ; coding: utf-8 -*-

import os

# Get the absolute path to the project directory
project_dir = os.path.abspath(os.path.dirname(__name__))

a = Analysis(
    [os.path.join(project_dir, 'mac_camera_preview.py')],
    pathex=[os.path.join(project_dir, 'venv', 'bin')],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='mac_camera_preview',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Set to False for GUI application
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[os.path.join(project_dir, 'cameralogo.icns')],
)
app = BUNDLE(
    exe,
    name='PreView.app',
    icon=os.path.join(project_dir, 'cameralogo.icns'),
    bundle_identifier=None,
)