#ifndef DS_LFU_H
#define DS_LFU_H

#include "../ds_types.h"

typedef struct ds_lfu ds_lfu_t;

ds_lfu_t *ds_lfu_create(size_t capacity, ds_hash_fn hash_key,
                        ds_compare_fn compare_key, ds_free_fn free_key,
                        ds_free_fn free_value);
void ds_lfu_destroy(ds_lfu_t *cache);

size_t ds_lfu_size(const ds_lfu_t *cache);
size_t ds_lfu_capacity(const ds_lfu_t *cache);
bool ds_lfu_is_empty(const ds_lfu_t *cache);

bool ds_lfu_put(ds_lfu_t *cache, void *key, void *value, void **evicted_key,
                void **evicted_value);
void *ds_lfu_get(ds_lfu_t *cache, const void *key);
bool ds_lfu_contains(const ds_lfu_t *cache, const void *key);
bool ds_lfu_peek(ds_lfu_t *cache, const void *key, void **value);
bool ds_lfu_remove(ds_lfu_t *cache, const void *key, void **old_key,
                   void **old_value);

size_t ds_lfu_frequency(const ds_lfu_t *cache, const void *key);
bool ds_lfu_touch(ds_lfu_t *cache, const void *key);
bool ds_lfu_resize(ds_lfu_t *cache, size_t new_capacity, void **evicted_keys,
                   void **evicted_values, size_t *evicted_count);
void ds_lfu_clear(ds_lfu_t *cache);
void ds_lfu_foreach(ds_lfu_t *cache, ds_kv_visit_fn visit, void *ctx);

#endif
