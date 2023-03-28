import sys
import os
from cx_Freeze import setup, Executable

files = ["icon.ico", "tests", "settings", "env"]

target = Executable(
    script="interactor.py",
    icon="icon.ico"
)

setup(
    name="SnakeM",
    version=1.0,
    description="snake the game",
    author="Martyn V. A.",
    options={"build_exe": {"include_files": files}},
    executables=[target]
)
