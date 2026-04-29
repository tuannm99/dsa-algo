#ifndef DS_LINKEDLIST_H
#define DS_LINKEDLIST_H

#include "../ds_types.h"

typedef struct ds_linkedlist ds_linkedlist_t;

ds_linkedlist_t *ds_linkedlist_create(ds_free_fn free_value);
void ds_linkedlist_destroy(ds_linkedlist_t *list);

size_t ds_linkedlist_size(const ds_linkedlist_t *list);
bool ds_linkedlist_is_empty(const ds_linkedlist_t *list);

bool ds_linkedlist_push_front(ds_linkedlist_t *list, void *value);
bool ds_linkedlist_push_back(ds_linkedlist_t *list, void *value);
void *ds_linkedlist_pop_front(ds_linkedlist_t *list);
void *ds_linkedlist_pop_back(ds_linkedlist_t *list);

void *ds_linkedlist_front(const ds_linkedlist_t *list);
void *ds_linkedlist_back(const ds_linkedlist_t *list);
void *ds_linkedlist_get(const ds_linkedlist_t *list, size_t index);
bool ds_linkedlist_insert(ds_linkedlist_t *list, size_t index, void *value);
void *ds_linkedlist_remove_at(ds_linkedlist_t *list, size_t index);
bool ds_linkedlist_remove_value(ds_linkedlist_t *list, const void *value,
                                ds_compare_fn compare, void **old_value);

void ds_linkedlist_reverse(ds_linkedlist_t *list);
void ds_linkedlist_clear(ds_linkedlist_t *list);
void ds_linkedlist_foreach(ds_linkedlist_t *list, ds_visit_fn visit, void *ctx);

#endif
