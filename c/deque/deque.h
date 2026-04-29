#ifndef DS_DEQUE_H
#define DS_DEQUE_H

#include "../ds_types.h"

typedef struct ds_deque ds_deque_t;

ds_deque_t *ds_deque_create(size_t initial_capacity, ds_free_fn free_value);
void ds_deque_destroy(ds_deque_t *deque);

size_t ds_deque_size(const ds_deque_t *deque);
bool ds_deque_is_empty(const ds_deque_t *deque);

bool ds_deque_push_front(ds_deque_t *deque, void *value);
bool ds_deque_push_back(ds_deque_t *deque, void *value);
void *ds_deque_pop_front(ds_deque_t *deque);
void *ds_deque_pop_back(ds_deque_t *deque);
void *ds_deque_peek_front(const ds_deque_t *deque);
void *ds_deque_peek_back(const ds_deque_t *deque);

void ds_deque_clear(ds_deque_t *deque);
void ds_deque_foreach(ds_deque_t *deque, ds_visit_fn visit, void *ctx);

#endif
