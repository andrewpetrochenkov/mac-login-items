import setuptools

setuptools.setup(
    name='mac-login-items',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/login-items','scripts/login-items-add','scripts/login-items-names','scripts/login-items-paths','scripts/login-items-rm']
)
