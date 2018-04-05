[ ![Download](https://api.bintray.com/packages/vkrapivin/conan/sqlpp11-connector-postgresql%3Avkrapivin/images/download.svg) ](https://bintray.com/vkrapivin/conan/sqlpp11-connector-postgresql%3Avkrapivin/_latestVersion)
[![Build Status](https://travis-ci.org/StiventoUser/conan-sqlpp11-connector-postgresql.svg?branch=testing%2F0.2)](https://travis-ci.org/StiventoUser/conan-sqlpp11-connector-postgresql)
[![Build status](https://ci.appveyor.com/api/projects/status/syim7jkbn8e38r6n?svg=true)](https://ci.appveyor.com/project/StiventoUser/conan-sqlpp11-connector-postgresql)

[Conan.io](https://conan.io) package for [sqlpp11-connector-postgresql](https://github.com/matthijs/sqlpp11-connector-postgresql) project
 
The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/vkrapivin/conan/sqlpp11-connector-postgresql%3Avkrapivin).

## For Users: Use this package

### Basic setup

    $ conan install sqlpp11/0.54@vkrapivin/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    sqlpp11-connector-postgresql/0.2@vkrapivin/testing

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create vkrapivin/testing

## Add Remote

    $ conan remote add vkrapivin https://api.bintray.com/conan/vkrapivin/conan 

## Upload

    $ conan upload sqlpp11-connector-postgresql/0.2@vkrapivin/testing --all -r vkrapivin

## License
[LICENSE_TYPE](LICENSE)
