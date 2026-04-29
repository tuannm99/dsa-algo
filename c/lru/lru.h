#ifndef DS_LRU_H
#define DS_LRU_H

#include "../ds_types.h"

typedef struct ds_lru ds_lru_t;

ds_lru_t *ds_lru_create(size_t capacity, ds_hash_fn hash_key,
                        ds_compare_fn compare_key, ds_free_fn free_key,
                        ds_free_fn free_value);
void ds_lru_destroy(ds_lru_t *cache);

size_t ds_lru_size(const ds_lru_t *cache);
size_t ds_lru_capacity(const ds_lru_t *cache);
bool ds_lru_is_empty(const ds_lru_t *cache);

bool ds_lru_put(ds_lru_t *cache, void *key, void *value, void **evicted_key,
                void **evicted_value);
void *ds_lru_get(ds_lru_t *cache, const void *key);
bool ds_lru_contains(const ds_lru_t *cache, const void *key);
bool ds_lru_peek(ds_lru_t *cache, const void *key, void **value);
bool ds_lru_remove(ds_lru_t *cache, const void *key, void **old_key,
                   void **old_value);

bool ds_lru_resize(ds_lru_t *cache, size_t new_capacity, void **evicted_keys,
                   void **evicted_values, size_t *evicted_count);
void ds_lru_clear(ds_lru_t *cache);
void ds_lru_foreach(ds_lru_t *cache, ds_kv_visit_fn visit, void *ctx);

#endif
