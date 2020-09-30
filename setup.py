import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='moneyonchain',
    version='0.0.47',
    packages=['moneyonchain'],
    url='https://github.com/moneyonchain/py_Moneyonchain/',
    author='Martin Mulone',
    author_email='martin.mulone@moneyonchain.com',
    description='Python interfaces to Money On Chain projects',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='AGPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    package_data={
        "moneyonchain": ["config.json", "abi/*.abi", "abi/*.bin",
                         "abi_rrc20/*.abi", "abi_rrc20/*.bin",
                         "abi_rdoc/*.abi", "abi_rdoc/*.bin",
                         "abi_dex/*.abi", "abi_dex/*.bin"]
    },
    python_requires='>=3.6',
    install_requires=[
        'web3>=5.7.0'
    ],
)
