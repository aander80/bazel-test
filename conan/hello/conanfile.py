from conan import ConanFile
from conan.tools.google import Bazel, BazelToolchain, BazelDeps, bazel_layout
from conan.tools.files import copy


class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"
    requires = "say/0.1"

    exports_sources = "WORKSPACE", "src/*"

    def layout(self):
        bazel_layout(self)

    def generate(self):
        tc = BazelToolchain(self)
        tc.generate()
        deps = BazelDeps(self)
        deps.generate()

    def build(self):
        bazel = Bazel(self)
        bazel.configure()
        bazel.build(label="//src:hello")

    def package(self):
        copy(self, f"{self.name}", self.build_path / "bazel-bin/src", self.package_path / "bin", keep_path=False)
