from setuptools import setup, find_packages

setup(
    name='mcq-generator',
    version='0.1.0',
    author='Yashash Gupta',
    author_email="yashashgupta96@gmail.com",
    install_requires=['openai','pandas','langchain','streamlit','python-dotenv','pyPDF2'],
    packages=find_packages()
)