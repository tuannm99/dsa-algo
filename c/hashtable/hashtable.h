#ifndef DS_HASHTABLE_H
#define DS_HASHTABLE_H

#include "../ds_types.h"

typedef struct ds_hashtable ds_hashtable_t;

ds_hashtable_t *ds_hashtable_create(size_t initial_capacity,
                                    ds_hash_fn hash_key,
                                    ds_compare_fn compare_key,
                                    ds_free_fn free_key, ds_free_fn free_value);
void ds_hashtable_destroy(ds_hashtable_t *table);

size_t ds_hashtable_size(const ds_hashtable_t *table);
size_t ds_hashtable_capacity(const ds_hashtable_t *table);
bool ds_hashtable_is_empty(const ds_hashtable_t *table);

bool ds_hashtable_set(ds_hashtable_t *table, void *key, void *value);
void *ds_hashtable_get(const ds_hashtable_t *table, const void *key);
bool ds_hashtable_contains(const ds_hashtable_t *table, const void *key);
bool ds_hashtable_delete(ds_hashtable_t *table, const void *key, void **old_key,
                         void **old_value);

bool ds_hashtable_resize(ds_hashtable_t *table, size_t new_capacity);
void ds_hashtable_clear(ds_hashtable_t *table);
void ds_hashtable_foreach(ds_hashtable_t *table, ds_kv_visit_fn visit,
                          void *ctx);

#endif
