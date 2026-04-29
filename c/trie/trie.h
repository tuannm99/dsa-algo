#ifndef DS_TRIE_H
#define DS_TRIE_H

#include "../ds_types.h"

typedef struct ds_trie ds_trie_t;

ds_trie_t *ds_trie_create(ds_free_fn free_value);
void ds_trie_destroy(ds_trie_t *trie);

size_t ds_trie_size(const ds_trie_t *trie);
bool ds_trie_is_empty(const ds_trie_t *trie);

bool ds_trie_insert(ds_trie_t *trie, const char *key, void *value);
void *ds_trie_get(const ds_trie_t *trie, const char *key);
bool ds_trie_contains(const ds_trie_t *trie, const char *key);
bool ds_trie_remove(ds_trie_t *trie, const char *key, void **old_value);

bool ds_trie_has_prefix(const ds_trie_t *trie, const char *prefix);
size_t ds_trie_prefix_count(const ds_trie_t *trie, const char *prefix);
void ds_trie_foreach_prefix(ds_trie_t *trie, const char *prefix,
                            ds_kv_visit_fn visit, void *ctx);

void ds_trie_clear(ds_trie_t *trie);

#endif
