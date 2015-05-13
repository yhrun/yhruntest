#coding=utf-8

from setuptools import setup,find_packages
setup(
  name = 'GT_Python_SDK',
  version = '0.1.0',
  packages = find_packages('GT_Python_SDK'), 
  package_dir = {'':'GT_Python_SDK'}, 
  description = "egg test mydemo",
  
  long_description = "egg test demo.",  
  author = 'zhouguoqing',
  author_email = 'yhruner@gmail.com',

  license = 'GPL',
  keywords = 'test api mydemo',
  platforms = "Independant",
  url = '',
)

