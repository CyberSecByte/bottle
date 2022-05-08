self.description = "bottle-db-upgrade DB version 9 (symlink support removal)"

self.filesystem = [ "mnt_real/subdir/", "mnt -> mnt_real/subdir/", "bar -> ./" ]

fpkg = pmpkg("filesystem")
fpkg.files = ["mnt_real/", "mnt/", "mnt/foo", "bar/", "bar/baz"]
fpkg.backup = ["mnt/foo"]

self.addpkg2db("local", fpkg)
self.dbver = 8

self.cmd = ["bottle-db-upgrade",
        "--root", self.rootdir(),
        "--dbpath", self.dbdir(),
        "--config", self.configfile() ]

self.addrule("BOTTLE_RETCODE=0")
self.addrule("FILE_EXIST=var/lib/bottle/local/ALPM_DB_VERSION")
self.addrule("PKG_BACKUP=filesystem|mnt_real/subdir/foo")
self.addrule("PKG_FILES=filesystem|mnt_real/")
self.addrule("PKG_FILES=filesystem|mnt_real/subdir/")
self.addrule("PKG_FILES=filesystem|mnt_real/subdir/foo")
self.addrule("PKG_FILES=filesystem|baz")
self.addrule("!PKG_FILES=filesystem|mnt/")
self.addrule("!PKG_FILES=filesystem|bar/")
