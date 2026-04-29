#ifndef DS_BLOOMFILTER_H
#define DS_BLOOMFILTER_H

#include "../ds_types.h"

typedef struct ds_bloomfilter ds_bloomfilter_t;

ds_bloomfilter_t *ds_bloomfilter_create(size_t bit_capacity,
                                        size_t num_hashes,
                                        ds_hash_fn hash1,
                                        ds_hash_fn hash2);
ds_bloomfilter_t *ds_bloomfilter_create_for_rate(size_t expected_items,
                                                 double false_positive_rate,
                                                 ds_hash_fn hash1,
                                                 ds_hash_fn hash2);
void ds_bloomfilter_destroy(ds_bloomfilter_t *filter);

size_t ds_bloomfilter_bit_capacity(const ds_bloomfilter_t *filter);
size_t ds_bloomfilter_hash_count(const ds_bloomfilter_t *filter);
size_t ds_bloomfilter_count(const ds_bloomfilter_t *filter);
bool ds_bloomfilter_is_empty(const ds_bloomfilter_t *filter);

bool ds_bloomfilter_add(ds_bloomfilter_t *filter, const void *value);
bool ds_bloomfilter_may_contain(const ds_bloomfilter_t *filter,
                                const void *value);

double ds_bloomfilter_estimated_false_positive_rate(
    const ds_bloomfilter_t *filter);
void ds_bloomfilter_clear(ds_bloomfilter_t *filter);

#endif
