self.description = "Query--check files, all there"

pkg = pmpkg("dummy")
pkg.files = [
    "usr/lib/libdummy.so.0",
    "usr/lib/libdummy.so -> libdummy.so.0",
    "usr/share/dummy/C/",
    "usr/share/dummy/C/msgs",
    "usr/share/dummy/en -> C"]
self.addpkg2db("local",pkg)

self.args = "-Qk"

self.addrule("BOTTLE_RETCODE=0")
self.addrule("!BOTTLE_OUTPUT=warning.*(No such file or directory)")
