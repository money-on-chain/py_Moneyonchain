import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='moneyonchain',
    version='2.0.0',
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
        "moneyonchain": ["config.json",
                         "networks.json",
                         "governance/abi/*.abi",
                         "governance/abi/*.bin",
                         "governance/abi_rdoc/*.abi",
                         "governance/abi_rdoc/*.bin",
                         "governance/abi_rrc20/*.abi",
                         "governance/abi_rrc20/*.bin",
                         "governance/abi_tex/*.abi",
                         "governance/abi_tex/*.bin",
                         "medianizer/abi/*.abi",
                         "medianizer/abi/*.bin",
                         "medianizer/abi_rdoc/*.abi",
                         "medianizer/abi_rdoc/*.bin",
                         "medianizer/abi_rrc20/*.abi",
                         "medianizer/abi_rrc20/*.bin",
                         "moc/abi/*.abi",
                         "moc/abi/*.bin",
                         "oracle/abi/*.abi",
                         "oracle/abi/*.bin",
                         "rdoc/abi/*.abi",
                         "rdoc/abi/*.bin",
                         "rrc20/abi/*.abi",
                         "rrc20/abi/*.bin",
                         "tex/abi/*.abi",
                         "tex/abi/*.bin",
                         "tokens/abi/*.abi",
                         "tokens/abi/*.bin"
                         ]
    },
    python_requires='>=3.6',
    install_requires=[
        'web3>=5.7.0',
        'eth-brownie==1.12.2',
        'PyYAML==5.3.1',
        'tabulate'
    ],
)
