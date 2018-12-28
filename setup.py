from setuptools import setup, findpackages

with open('README.md', encoding='UTF-8') as f:
    readme=f.read()

setup(
        name='tfstate2ansible',
        version='0.1.0',
        description='Takes a tfstate file from Terraform and picks out the hosts for an ansible inventory file'
        long_description=readme,
        author='Brad Cesarone',
        author_email='bc@beckonconn.com',
        packages=find_packages('src'),
        package_dir={'':'src'},
        install_requires=[]
)
