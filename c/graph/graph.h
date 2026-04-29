#ifndef DS_GRAPH_H
#define DS_GRAPH_H

#include "../ds_types.h"

typedef struct ds_graph ds_graph_t;
typedef struct ds_graph_vertex ds_graph_vertex_t;
typedef struct ds_graph_edge ds_graph_edge_t;

typedef enum ds_graph_kind {
  DS_GRAPH_DIRECTED = 0,
  DS_GRAPH_UNDIRECTED = 1
} ds_graph_kind_t;

ds_graph_t *ds_graph_create(ds_graph_kind_t kind, ds_hash_fn hash_vertex_id,
                            ds_compare_fn compare_vertex_id,
                            ds_free_fn free_vertex_id,
                            ds_free_fn free_vertex_value,
                            ds_free_fn free_edge_value);
void ds_graph_destroy(ds_graph_t *graph);

size_t ds_graph_vertex_count(const ds_graph_t *graph);
size_t ds_graph_edge_count(const ds_graph_t *graph);
bool ds_graph_is_directed(const ds_graph_t *graph);

bool ds_graph_add_vertex(ds_graph_t *graph, void *vertex_id,
                         void *vertex_value);
bool ds_graph_set_vertex(ds_graph_t *graph, const void *vertex_id,
                         void *vertex_value, void **old_value);
void *ds_graph_get_vertex(const ds_graph_t *graph, const void *vertex_id);
bool ds_graph_remove_vertex(ds_graph_t *graph, const void *vertex_id,
                            void **old_id, void **old_value);

bool ds_graph_add_edge(ds_graph_t *graph, const void *from_id,
                       const void *to_id, void *edge_value);
void *ds_graph_get_edge(const ds_graph_t *graph, const void *from_id,
                        const void *to_id);
bool ds_graph_has_edge(const ds_graph_t *graph, const void *from_id,
                       const void *to_id);
bool ds_graph_remove_edge(ds_graph_t *graph, const void *from_id,
                          const void *to_id, void **old_value);

size_t ds_graph_out_degree(const ds_graph_t *graph, const void *vertex_id);
size_t ds_graph_in_degree(const ds_graph_t *graph, const void *vertex_id);

void ds_graph_foreach_vertex(ds_graph_t *graph, ds_kv_visit_fn visit,
                             void *ctx);
void ds_graph_foreach_neighbor(ds_graph_t *graph, const void *vertex_id,
                               ds_kv_visit_fn visit, void *ctx);

#endif
