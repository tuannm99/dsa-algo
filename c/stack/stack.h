#ifndef DS_STACK_H
#define DS_STACK_H

#include "../ds_types.h"

typedef struct ds_stack ds_stack_t;

ds_stack_t *ds_stack_create(size_t initial_capacity, ds_free_fn free_value);
void ds_stack_destroy(ds_stack_t *stack);

size_t ds_stack_size(const ds_stack_t *stack);
bool ds_stack_is_empty(const ds_stack_t *stack);

bool ds_stack_push(ds_stack_t *stack, void *value);
void *ds_stack_pop(ds_stack_t *stack);
void *ds_stack_peek(const ds_stack_t *stack);

void ds_stack_clear(ds_stack_t *stack);
void ds_stack_foreach(ds_stack_t *stack, ds_visit_fn visit, void *ctx);

#endif
