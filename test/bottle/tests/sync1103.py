self.description = "Get package list from sync dbs"

sp = pmpkg("dummy")
sp.files = ["bin/dummy",
            "usr/man/man1/dummy.1"]
self.addpkg2db("sync", sp)

self.args = "-Sl"

self.addrule("BOTTLE_RETCODE=0")
self.addrule("BOTTLE_OUTPUT=^sync %s" % sp.name)
