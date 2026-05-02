from dataclasses import dataclass


@dataclass
class Interval:
    start: int
    end: int


def merge_intervals(intervals: list[Interval]) -> list[Interval]:
    if not intervals:
        return []

    intervals.sort(key=lambda item: (item.start, item.end))
    result = [Interval(intervals[0].start, intervals[0].end)]

    for current in intervals[1:]:
        last = result[-1]
        if current.start <= last.end:
            last.end = max(last.end, current.end)
        else:
            result.append(Interval(current.start, current.end))

    return result


def can_attend_meetings(intervals: list[Interval]) -> bool:
    return len(merge_intervals(intervals)) == len(intervals)
