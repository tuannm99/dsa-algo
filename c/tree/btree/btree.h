#ifndef DS_BTREE_H
#define DS_BTREE_H

#include "../../ds_types.h"

typedef struct ds_btree ds_btree_t;

ds_btree_t *ds_btree_create(size_t min_degree, ds_compare_fn compare_key,
                            ds_free_fn free_key, ds_free_fn free_value);
void ds_btree_destroy(ds_btree_t *tree);

size_t ds_btree_size(const ds_btree_t *tree);
bool ds_btree_is_empty(const ds_btree_t *tree);
size_t ds_btree_min_degree(const ds_btree_t *tree);

bool ds_btree_insert(ds_btree_t *tree, void *key, void *value);
void *ds_btree_get(const ds_btree_t *tree, const void *key);
bool ds_btree_contains(const ds_btree_t *tree, const void *key);
bool ds_btree_remove(ds_btree_t *tree, const void *key, void **old_key,
                     void **old_value);

void *ds_btree_min_key(const ds_btree_t *tree);
void *ds_btree_max_key(const ds_btree_t *tree);

void ds_btree_clear(ds_btree_t *tree);
void ds_btree_traverse(ds_btree_t *tree, ds_kv_visit_fn visit, void *ctx);

#endif
