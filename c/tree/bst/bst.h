#ifndef DS_BST_H
#define DS_BST_H

#include "../../ds_types.h"

typedef struct ds_bst ds_bst_t;

ds_bst_t *ds_bst_create(ds_compare_fn compare_key, ds_free_fn free_key,
                        ds_free_fn free_value);
void ds_bst_destroy(ds_bst_t *tree);

size_t ds_bst_size(const ds_bst_t *tree);
bool ds_bst_is_empty(const ds_bst_t *tree);

bool ds_bst_insert(ds_bst_t *tree, void *key, void *value);
void *ds_bst_get(const ds_bst_t *tree, const void *key);
bool ds_bst_contains(const ds_bst_t *tree, const void *key);
bool ds_bst_remove(ds_bst_t *tree, const void *key, void **old_key,
                   void **old_value);

void *ds_bst_min_key(const ds_bst_t *tree);
void *ds_bst_max_key(const ds_bst_t *tree);

void ds_bst_clear(ds_bst_t *tree);
void ds_bst_inorder(ds_bst_t *tree, ds_kv_visit_fn visit, void *ctx);
void ds_bst_preorder(ds_bst_t *tree, ds_kv_visit_fn visit, void *ctx);
void ds_bst_postorder(ds_bst_t *tree, ds_kv_visit_fn visit, void *ctx);

#endif
