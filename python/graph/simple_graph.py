from __future__ import annotations

from typing import Generic, TypeVar, cast

from ..ds_types import KVVisitFunc
from .graph import Config, Graph, Kind

ID = TypeVar("ID")
VertexValue = TypeVar("VertexValue")
EdgeValue = TypeVar("EdgeValue")


class SimpleGraph(Generic[ID, VertexValue, EdgeValue],
                  Graph[ID, VertexValue, EdgeValue]):

    def __init__(self, config: Config[ID, VertexValue, EdgeValue]) -> None:
        self._config = config
        self._vertices: dict[ID, VertexValue] = {}
        self._edges: dict[ID, dict[ID, EdgeValue]] = {}

    def vertex_count(self) -> int:
        return len(self._vertices)

    def edge_count(self) -> int:
        count = sum(len(edges) for edges in self._edges.values())
        return count if self.is_directed() else count // 2

    def is_directed(self) -> bool:
        return self._config.kind == Kind.DIRECTED

    def add_vertex(self, vertex_id: ID, value: VertexValue) -> bool:
        if vertex_id in self._vertices:
            return False
        self._vertices[vertex_id] = value
        self._edges[vertex_id] = {}
        return True

    def set_vertex(self, vertex_id: ID,
                   value: VertexValue) -> tuple[VertexValue, bool]:
        if vertex_id not in self._vertices:
            return cast(VertexValue, None), False
        old = self._vertices[vertex_id]
        self._vertices[vertex_id] = value
        return old, True

    def get_vertex(self, vertex_id: ID) -> tuple[VertexValue, bool]:
        if vertex_id not in self._vertices:
            return cast(VertexValue, None), False
        return self._vertices[vertex_id], True

    def remove_vertex(self, vertex_id: ID) -> tuple[ID, VertexValue, bool]:
        if vertex_id not in self._vertices:
            return cast(ID, None), cast(VertexValue, None), False
        value = self._vertices.pop(vertex_id)
        self._edges.pop(vertex_id, None)
        for edges in self._edges.values():
            edges.pop(vertex_id, None)
        return vertex_id, value, True

    def add_edge(self, from_id: ID, to_id: ID, value: EdgeValue) -> bool:
        if from_id not in self._vertices or to_id not in self._vertices:
            return False
        self._edges[from_id][to_id] = value
        if not self.is_directed():
            self._edges[to_id][from_id] = value
        return True

    def get_edge(self, from_id: ID, to_id: ID) -> tuple[EdgeValue, bool]:
        if from_id not in self._edges or to_id not in self._edges[from_id]:
            return cast(EdgeValue, None), False
        return self._edges[from_id][to_id], True

    def has_edge(self, from_id: ID, to_id: ID) -> bool:
        return from_id in self._edges and to_id in self._edges[from_id]

    def remove_edge(self, from_id: ID, to_id: ID) -> tuple[EdgeValue, bool]:
        if not self.has_edge(from_id, to_id):
            return cast(EdgeValue, None), False
        value = self._edges[from_id].pop(to_id)
        if not self.is_directed():
            self._edges[to_id].pop(from_id, None)
        return value, True

    def out_degree(self, vertex_id: ID) -> int:
        return len(self._edges.get(vertex_id, {}))

    def in_degree(self, vertex_id: ID) -> int:
        return sum(1 for edges in self._edges.values() if vertex_id in edges)

    def for_each_vertex(self, visit: KVVisitFunc[ID, VertexValue]) -> None:
        for key, value in self._vertices.items():
            visit(key, value)

    def for_each_neighbor(self, vertex_id: ID,
                          visit: KVVisitFunc[ID, EdgeValue]) -> None:
        for key, value in self._edges.get(vertex_id, {}).items():
            visit(key, value)
