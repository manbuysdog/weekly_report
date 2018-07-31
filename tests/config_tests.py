import pytest
from weekly_report.config import load_config


def test_simple():
    assert(1 == 1)

def test_load_config():
    config = load_config('test')
    assert(config.get('env', 'name') == 'test')