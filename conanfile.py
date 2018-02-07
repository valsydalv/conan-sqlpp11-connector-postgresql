from conans import ConanFile, CMake, tools

class Sqlpp11connectorpostgresqlConan(ConanFile):
    name = "sqlpp11-connector-postgresql"
    version = "0.2"
    license = "MIT"
    url = "https://github.com/StiventoUser/conan-sqlpp11-connector-postgresql"
    description = "A connector for sqlpp11 library."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "pg_root": "ANY" }
    default_options = "shared=False", "pg_root="
    generators = "cmake"
    requires = "sqlpp11/0.54@vkrapivin/testing"

    def getPostgreSQLIncludeDir(self):
        return subprocess.check_output("pg_config --includedir", shell=True)

    def getPostgreSQLLibDir(self):
        return subprocess.check_output("pg_config --libdir", shell=True)
    
    def source(self):
        self.run("git clone https://github.com/StiventoUser/sqlpp11-connector-postgresql.git")
        with tools.chdir("sqlpp11-connector-postgresql"):
            self.run("git checkout %s" % "develop") # TODO update to version checkout
            # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
            # if the packaged project doesn't have variables to set it properly
            tools.replace_in_file("CMakeLists.txt", "project(sqlpp11-connector-postgresql VERSION 0.1 LANGUAGES CXX)", '''project(sqlpp11-connector-postgresql VERSION 0.1 LANGUAGES CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        if self.settings.os == "Windows":
            if not self.options.pg_root._value:
                raise ValueError('pg_root must be specified.')
            cmake.definitions["POSTGRESQL_ROOT_DIR"] = self.options.pg_root
        else:
            cmake.definitions["PostgreSQL_ROOT_DIRECTORIES"] = "%s %s %s" (self.options.pg_root._value, self.getPostgreSQLIncludeDir(), self.getPostgreSQLLibDir())
        cmake.definitions["sqlpp11_ROOT_DIR"] = self.deps_cpp_info["sqlpp11"].rootpath
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

        if self.settings.os == "Windows":
            self.cpp_info.includedirs.append('%s/include' % self.options.pg_root._value)
            self.cpp_info.libdirs.append('%s/lib' % self.options.pg_root._value)
        else:
            self.cpp_info.includedirs.append(self.getPostgreSQLIncludeDir())
            self.cpp_info.libdirs.append(self.getPostgreSQLLibDir())
        self.cpp_info.libs.append('libpq')
