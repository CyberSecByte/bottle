/*
 *  bottle.h
 *
 *  Copyright (c) 2006-2022 Pacman Development Team <bottle-dev@lists.archlinux.org>
 *  Copyright (c) 2002-2006 by Judd Vinet <jvinet@zeroflux.org>
 *
 *  This program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2 of the License, or
 *  (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#ifndef PM_BOTTLE_H
#define PM_BOTTLE_H

#include <alpm_list.h>

#define BOTTLE_CALLER_PREFIX "BOTTLE"

/* database.c */
int bottle_database(alpm_list_t *targets);
/* deptest.c */
int bottle_deptest(alpm_list_t *targets);
/* files.c */
int bottle_files(alpm_list_t *files);
/* query.c */
int bottle_query(alpm_list_t *targets);
/* remove.c */
int bottle_remove(alpm_list_t *targets);
/* sync.c */
int bottle_sync(alpm_list_t *targets);
int sync_prepare_execute(void);
/* upgrade.c */
int bottle_upgrade(alpm_list_t *targets);

#endif /* PM_BOTTLE_H */
