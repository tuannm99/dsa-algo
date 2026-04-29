#ifndef DS_QUEUE_H
#define DS_QUEUE_H

#include "../ds_types.h"

typedef struct ds_queue ds_queue_t;

ds_queue_t *ds_queue_create(size_t initial_capacity, ds_free_fn free_value);
void ds_queue_destroy(ds_queue_t *queue);

size_t ds_queue_size(const ds_queue_t *queue);
bool ds_queue_is_empty(const ds_queue_t *queue);

bool ds_queue_enqueue(ds_queue_t *queue, void *value);
void *ds_queue_dequeue(ds_queue_t *queue);
void *ds_queue_peek(const ds_queue_t *queue);

void ds_queue_clear(ds_queue_t *queue);
void ds_queue_foreach(ds_queue_t *queue, ds_visit_fn visit, void *ctx);

#endif
