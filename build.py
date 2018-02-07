import platform
from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(args="--build missing")
    if platform.system() == "Windows":
        builder.add(settings={"arch": "x86", "build_type": "Debug", "compiler": "Visual Studio", "compiler.version": 14, "compiler.runtime": "MTd"},
            options={"pg_root": "C:/Program Files/PostgreSQL/10"}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86", "build_type": "Release", "compiler": "Visual Studio", "compiler.version": 14, "compiler.runtime": "MT"},
            options={"pg_root": "C:/Program Files/PostgreSQL/10"}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86_64", "build_type": "Debug", "compiler": "Visual Studio", "compiler.version": 14, "compiler.runtime": "MTd"},
            options={"pg_root": "C:/Program Files/PostgreSQL/10"}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86_64", "build_type": "Release", "compiler": "Visual Studio", "compiler.version": 14, "compiler.runtime": "MT"},
            options={"pg_root": "C:/Program Files/PostgreSQL/10"}, env_vars={}, build_requires={})
    else:
        builder.add(settings={"arch": "x86", "build_type": "Debug", "compiler.libcxx": "libstdc++11"},
            options={}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86", "build_type": "Release", "compiler.libcxx": "libstdc++11"},
            options={}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86_64", "build_type": "Debug", "compiler.libcxx": "libstdc++11"},
            options={}, env_vars={}, build_requires={})
        builder.add(settings={"arch": "x86_64", "build_type": "Release", "compiler.libcxx": "libstdc++11"},
            options={}, env_vars={}, build_requires={})
    builder.run()
