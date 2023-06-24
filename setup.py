import sys
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.egg_info import egg_info

def install_package(package):
    import pip
    try:
        from pip._internal import main
        main(['install', package])
    except AttributeError:
        from pip import __main__
        __main__._main(['install', package])

if "--with-audio" in sys.argv:
    install_package('opencv-python')
    install_package('pyaudio')
    sys.argv.remove("--with-audio")
else:
    install_package('opencv-python')

setup(
    name="video2asciiX",
    version="1.4.0",
    author="Joel Ibaceta",
    author_email="donotreply@gmail.com",
    license='MIT',
    description="It is a simple python package to play videos in the terminal",
    long_description="A simple tool to play a video using ascii characters instead of pixels",
    url="https://github.com/joelibaceta/video-to-ascii",
    project_urls={
        'Source': 'https://github.com/mcjka/video2asciiX',
        'Tracker': 'https://github.com/mcjka/video2toasciiX/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=['xtermcolor', 'ffmpeg-python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='video ascii terminal opencv',
    entry_points={
        "console_scripts": [
            'video-to-ascii=video_to_ascii.cli:main'
        ]
    }
)
