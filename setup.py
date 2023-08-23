from setuptools import setup

setup(
    name='aquaemi_forecast',
    version='0.1.0',    
    description='Forecast Model using ARIMA trained on Mekong Delta Water Parameters',
    url='',
    author='Aquaemi Team',
    author_email='anhminh.hoang1105@gmail.com',
    license='BSD 2-clause',
    packages=['aquaemiforecast'],
    install_requires=['numpy',
                      'pandas',
                      'matplotlib',
                      'statsmodels',
                      'sktime'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.8',
    ],
)