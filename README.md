# bazel-test

## Conan

Currently only tested with conan 2.

### say/hello

This shows a simple usage of Bazel in a library package and a binary package.

To create these, simply run

``` shell
$ cd conan
$ conan create say
$ conan create hello
# Run hello
$ conan cache path <full-package-reference> # hello/0.1#4254aa7a6bbb9872913ee0ce25a87b75:cd0085d955e54eda07a341e405c370abfff97742#2588c3fc48db84bf88997c82b5936953
$ /home/<user>/.conan2/p/b/hello61d0c0396a6cd/p/bin/hello
hello
```
