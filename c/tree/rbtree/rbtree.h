#ifndef DS_RBTREE_H
#define DS_RBTREE_H

#include "../../ds_types.h"

typedef struct ds_rbtree ds_rbtree_t;

ds_rbtree_t *ds_rbtree_create(ds_compare_fn compare_key, ds_free_fn free_key,
                              ds_free_fn free_value);
void ds_rbtree_destroy(ds_rbtree_t *tree);

size_t ds_rbtree_size(const ds_rbtree_t *tree);
bool ds_rbtree_is_empty(const ds_rbtree_t *tree);

bool ds_rbtree_insert(ds_rbtree_t *tree, void *key, void *value);
void *ds_rbtree_get(const ds_rbtree_t *tree, const void *key);
bool ds_rbtree_contains(const ds_rbtree_t *tree, const void *key);
bool ds_rbtree_remove(ds_rbtree_t *tree, const void *key, void **old_key,
                      void **old_value);

void *ds_rbtree_min_key(const ds_rbtree_t *tree);
void *ds_rbtree_max_key(const ds_rbtree_t *tree);

void ds_rbtree_clear(ds_rbtree_t *tree);
void ds_rbtree_inorder(ds_rbtree_t *tree, ds_kv_visit_fn visit, void *ctx);

#endif
