self.description = "Get URL on package from a sync db"

sp = pmpkg("dummy")
sp.files = ["bin/dummy",
            "usr/man/man1/dummy.1"]
self.addpkg2db("sync", sp)

self.args = "-Sp %s" % sp.name

self.addrule("BOTTLE_RETCODE=0")
self.addrule("BOTTLE_OUTPUT=%s" % sp.name)
self.addrule("BOTTLE_OUTPUT=file://")
