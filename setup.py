from setuptools import setup, find_packages

setup(
    name='ai-research-agent',
    version='0.2.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'openai==0.27.0',
        'pinecone-client==2.2.0',
        'langgraph==1.0.0',
        'requests==2.28.1',
        'PyYAML==6.0',
        'serpapi==3.3.1',
        'arxiv==0.2.0'
    ],
    entry_points={
        'console_scripts': [
            'ai-research-agent=main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A multi-agent AI research system with ReAct-style reasoning and tool usage.',
    license='MIT',
    url='https://github.com/USERNAME/AI-Research-Agent',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
)
