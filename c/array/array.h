#ifndef DS_ARRAY_H
#define DS_ARRAY_H

#include "../ds_types.h"

typedef struct ds_array ds_array_t;

ds_array_t *ds_array_create(size_t initial_capacity, ds_free_fn free_value);
void ds_array_destroy(ds_array_t *array);

size_t ds_array_size(const ds_array_t *array);
size_t ds_array_capacity(const ds_array_t *array);
bool ds_array_is_empty(const ds_array_t *array);

bool ds_array_reserve(ds_array_t *array, size_t min_capacity);
bool ds_array_shrink_to_fit(ds_array_t *array);
void ds_array_clear(ds_array_t *array);

void *ds_array_get(const ds_array_t *array, size_t index);
bool ds_array_set(ds_array_t *array, size_t index, void *value);

bool ds_array_push(ds_array_t *array, void *value);
void *ds_array_pop(ds_array_t *array);
bool ds_array_insert(ds_array_t *array, size_t index, void *value);
void *ds_array_remove(ds_array_t *array, size_t index);

ssize_t ds_array_index_of(const ds_array_t *array, const void *value,
                          ds_compare_fn compare);
void ds_array_foreach(ds_array_t *array, ds_visit_fn visit, void *ctx);

#endif
