from setuptools import setup

def build_native(spec):
    # build an example rust library
   
    build = spec.add_external_build(
        cmd=['bash', '-x', 'cargo.sh'],
        path='./rust_test2'
    )

    spec.add_cffi_module(
        module_path='example._native',
        dylib=lambda: build.find_dylib('rust_test', in_path='target/release'),
        header_filename=lambda: build.find_header('rust_test.h', in_path='./'),
        rtld_flags=['NOW', 'NODELETE']
    )

setup(
    name='rust_test',
    version='0.0.1',
    packages=['example'],
    zip_safe=False,
    platforms='any',
    setup_requires=['milksnake'],
    install_requires=['milksnake'],
    milksnake_tasks=[
        build_native
    ]
)
