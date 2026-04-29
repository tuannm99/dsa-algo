package intervals

import "sort"

type Interval struct {
	Start int
	End   int
}

func MergeIntervals(intervals []Interval) []Interval {
	if len(intervals) == 0 {
		return nil
	}

	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i].Start == intervals[j].Start {
			return intervals[i].End < intervals[j].End
		}
		return intervals[i].Start < intervals[j].Start
	})

	result := []Interval{intervals[0]}
	for i := 1; i < len(intervals); i++ {
		last := &result[len(result)-1]
		cur := intervals[i]
		if cur.Start <= last.End {
			if cur.End > last.End {
				last.End = cur.End
			}
			continue
		}
		result = append(result, cur)
	}
	return result
}

func CanAttendMeetings(intervals []Interval) bool {
	merged := MergeIntervals(intervals)
	return len(merged) == len(intervals)
}
