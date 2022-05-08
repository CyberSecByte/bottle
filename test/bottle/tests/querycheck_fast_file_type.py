self.description = "check file type without mtree"

self.filesystem = [ "bar/", "foo -> bar/" ]

pkg = pmpkg("dummy")
pkg.files = [ "foo/" ]
self.addpkg2db("local",pkg)

self.args = "-Qk"

self.addrule("BOTTLE_RETCODE=1")
self.addrule("BOTTLE_OUTPUT=warning.*(File type mismatch)")
