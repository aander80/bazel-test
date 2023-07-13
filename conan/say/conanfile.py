from conan import ConanFile
from conan.tools.google import Bazel, BazelToolchain, BazelDeps, bazel_layout
from conan.tools.files import copy


class SayConan(ConanFile):
    name = "say"
    version = "0.1"

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
        bazel.build(label="//src:say")

    def package(self):
        copy(self, "*.a", self.build_path / "bazel-bin", self.package_path / "lib", keep_path=False)
        copy(self, "*.h", self.source_path / "src", self.package_path / "inc", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = [f"{self.name}"]
        self.cpp_info.includedirs = ["inc"]
        self.cpp_info.libdirs = ["lib"]
