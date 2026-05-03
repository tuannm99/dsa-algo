from __future__ import annotations

from python.bloomfilter.bloomfilter import Config


def test_bloom_filter_basic_membership(bloom_filter_factory) -> None:
    bloom_filter = bloom_filter_factory(
        Config(
            bit_capacity=64,
            num_hashes=2,
            hash1=hash,
            hash2=lambda value: hash(("alt", value)),
        ))

    assert bloom_filter.is_empty() is True
    assert bloom_filter.add("alpha") is True
    assert bloom_filter.count() == 1
    assert bloom_filter.may_contain("alpha") is True
    assert bloom_filter.may_contain("omega") is False
    assert bloom_filter.bit_capacity() == 64
    assert bloom_filter.hash_count() == 2
    assert bloom_filter.estimated_false_positive_rate() >= 0.0


def test_bloom_filter_clear_resets_state(bloom_filter_factory) -> None:
    bloom_filter = bloom_filter_factory(
        Config(
            bit_capacity=32,
            num_hashes=2,
            hash1=hash,
            hash2=lambda value: hash(("alt", value)),
        ))

    assert bloom_filter.add("beta") is True
    assert bloom_filter.count() == 1
    bloom_filter.clear()
    assert bloom_filter.is_empty() is True
    assert bloom_filter.count() == 0
    assert bloom_filter.may_contain("beta") is False
