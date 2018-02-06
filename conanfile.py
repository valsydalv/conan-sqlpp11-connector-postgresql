from conans import ConanFile, CMake, tools

class Sqlpp11connectorpostgresqlConan(ConanFile):
    name = "sqlpp11-connector-postgresql"
    version = "0.2"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Sqlpp11connectorpostgresql here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "pg_root": "ANY" }
    default_options = "shared=False"
    generators = "cmake"
    requires = "sqlpp11/0.54@vkrapivin/testing"

    def source(self):
        self.run("git clone https://github.com/StiventoUser/sqlpp11-connector-postgresql.git")
        with tools.chdir("sqlpp11-connector-postgresql"):
            self.run("git checkout %s" % "develop")
            # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
            # if the packaged project doesn't have variables to set it properly
            tools.replace_in_file("CMakeLists.txt", "project(sqlpp11-connector-postgresql VERSION 0.1 LANGUAGES CXX)", '''project(sqlpp11-connector-postgresql VERSION 0.1 LANGUAGES CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.definitions["sqlpp11_ROOT_DIR"] = self.deps_cpp_info["sqlpp11"].rootpath
        cmake.definitions["POSTGRESQL_ROOT_DIR"] = self.options.pg_root
        cmake.configure(source_folder="sqlpp11-connector-postgresql")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s' % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="sqlpp11-connector-postgresql/include")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        if self.options.shared == "True":
            self.cpp_info.libs = ['sqlpp11-connector-postgresql-dynamic']
        else:
            self.cpp_info.libs = ['sqlpp11-connector-postgresql-static']
        self.cpp_info.libs.append('libpq.lib')

        self.cpp_info.includedirs.append('%s/include' % self.options.pg_root._value)
        self.cpp_info.libdirs.append('%s/lib' % self.options.pg_root._value)
