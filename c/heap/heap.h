#ifndef DS_HEAP_H
#define DS_HEAP_H

#include "../ds_types.h"

typedef struct ds_heap ds_heap_t;

ds_heap_t *ds_heap_create(size_t initial_capacity, ds_compare_fn compare,
                          ds_free_fn free_value);
void ds_heap_destroy(ds_heap_t *heap);

size_t ds_heap_size(const ds_heap_t *heap);
bool ds_heap_is_empty(const ds_heap_t *heap);

bool ds_heap_push(ds_heap_t *heap, void *value);
void *ds_heap_pop(ds_heap_t *heap);
void *ds_heap_peek(const ds_heap_t *heap);

bool ds_heap_replace_top(ds_heap_t *heap, void *value, void **old_value);
void ds_heap_clear(ds_heap_t *heap);
void ds_heap_foreach(ds_heap_t *heap, ds_visit_fn visit, void *ctx);

#endif
