#ifndef DS_TYPES_H
#define DS_TYPES_H

#include <sys/types.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

typedef int (*ds_compare_fn)(const void *lhs, const void *rhs);
typedef size_t (*ds_hash_fn)(const void *key);
typedef void (*ds_free_fn)(void *value);
typedef bool (*ds_predicate_fn)(const void *value, void *ctx);
typedef void (*ds_visit_fn)(void *value, void *ctx);
typedef void (*ds_kv_visit_fn)(void *key, void *value, void *ctx);

#endif
