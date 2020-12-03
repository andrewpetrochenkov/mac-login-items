import setuptools

setuptools.setup(
    name='mac-login-items',
    version='2020.10.26',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/login-items','scripts/login-items-add','scripts/login-items-names','scripts/login-items-paths','scripts/login-items-rm']
)
