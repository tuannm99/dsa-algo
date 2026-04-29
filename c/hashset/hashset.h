#ifndef DS_HASHSET_H
#define DS_HASHSET_H

#include "../ds_types.h"

typedef struct ds_hashset ds_hashset_t;

ds_hashset_t *ds_hashset_create(size_t initial_capacity, ds_hash_fn hash_value,
                                ds_compare_fn compare_value,
                                ds_free_fn free_value);
void ds_hashset_destroy(ds_hashset_t *set);

size_t ds_hashset_size(const ds_hashset_t *set);
bool ds_hashset_is_empty(const ds_hashset_t *set);

bool ds_hashset_add(ds_hashset_t *set, void *value);
bool ds_hashset_contains(const ds_hashset_t *set, const void *value);
bool ds_hashset_remove(ds_hashset_t *set, const void *value, void **old_value);

void ds_hashset_clear(ds_hashset_t *set);
void ds_hashset_foreach(ds_hashset_t *set, ds_visit_fn visit, void *ctx);

#endif
